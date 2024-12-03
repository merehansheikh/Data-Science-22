import numpy as np
import random

def calculate_entropy(data, target_col):
    # Extract the target values
    target_values = [row[target_col] for row in data]

    # Count the occurrences of each unique value
    value_counts = np.unique(target_values, return_counts=True)

    # Calculate the probabilities of each value
    probabilities = value_counts[1] / len(target_values)

    # Calculate the entropy
    entropy = -np.sum(probabilities * np.log2(probabilities))

    return entropy

def calculate_information_gain(data, attribute, target_col):
    """
    Calculates the information gain for a given attribute in the dataset.

    Args:
        data: The dataset as a list of lists.
        attribute: The index of the attribute to calculate information gain for.
        target_col: The index of the target column.

    Returns:
        The information gain of the attribute.
    """

    # Calculate the entropy of the entire dataset
    parent_entropy = calculate_entropy(data, target_col)

    # Get unique values of the attribute
    unique_values = set(row[attribute] for row in data)

    # Calculate weighted entropy for each unique value
    weighted_entropy = 0
    for value in unique_values:
        subset = [row for row in data if row[attribute] == value]
        subset_entropy = calculate_entropy(subset, target_col)
        weighted_entropy += len(subset) / len(data) * subset_entropy

    # Calculate information gain
    information_gain = parent_entropy - weighted_entropy

    return information_gain

def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    """
    Recursively builds a decision tree using entropy and information gain.

    Args:
        data: The dataset as a list of lists.
        attributes: A list of attribute indices to consider.
        target_col: The index of the target column.
        depth: The current depth of the tree.
        max_depth: The maximum depth of the tree.

    Returns:
        A decision tree as a nested dictionary.
    """

    # Base cases:
    # 1. If all labels are the same, return that label
    if len(set(row[target_col] for row in data)) == 1:
        return data[0][target_col]

    # 2. If the dataset is empty or we've reached the maximum depth, return the most common label
    if not data or depth == max_depth or not attributes:
        return max(set(row[target_col] for row in data), key=[row[target_col] for row in data].count)

    # Select the best attribute to split on
    best_attribute = max(attributes, key=lambda x: calculate_information_gain(data, x, target_col))

    # Create a tree with the best attribute as the root
    tree = {best_attribute: {}}

    # Create a copy of the attributes list and remove the best attribute from it
    remaining_attributes = attributes.copy()
    remaining_attributes.remove(best_attribute)

    # Create branches for each value of the best attribute
    for value in set(row[best_attribute] for row in data):
        subset = [row for row in data if row[best_attribute] == value]
        subtree = build_tree(subset, remaining_attributes, target_col, depth + 1, max_depth)
        tree[best_attribute][value] = subtree

    return tree

def predict(tree, data_point):
    """
    Traverses the tree to predict the class for a given data point.

    Args:
        tree: The decision tree.
        data_point: A list representing the data point.

    Returns:
        The predicted class.
    """

    current_node = tree
    while isinstance(current_node, dict):
        attribute = list(current_node.keys())[0]
        value = data_point[attribute]
        if value in current_node[attribute]:
            current_node = current_node[attribute][value]
        else:
            return None  # Return None if the value is not in the tree

    return current_node

def build_random_forest(data, attributes, target_col, n_trees=2):
    """
    Builds a Random Forest by generating multiple decision trees.

    Args:
        data: The dataset as a list of lists.
        attributes: A list of attribute indices to consider.
        target_col: The index of the target column.
        n_trees: The number of trees in the forest.

    Returns:
        A list of decision trees.
    """

    forest = []
    for _ in range(n_trees):
        # Sample a subset of the data
        sample = random.choices(data, k=len(data))

        # Sample a subset of the attributes
        sampled_attributes = random.sample(attributes, int(len(attributes) ** 0.5))

        # Build a decision tree on the sampled data and attributes
        tree = build_tree(sample, sampled_attributes, target_col)
        forest.append(tree)

    return forest

if __name__ == "__main__":
    # Sample dataset
    dataset = [
        ['Sunny', 'Hot', 'No'],
        ['Overcast', 'Hot', 'Yes'],
        ['Rainy', 'Mild', 'Yes'],
        ['Sunny', 'Mild', 'No'],
        ['Overcast', 'Mild', 'Yes'],
        ['Rainy', 'Hot', 'No'],
    ]

    # Define attributes and target column
    attributes = [0, 1]
    target_col = 2

    # Build a Random Forest
    forest = build_random_forest(dataset, attributes, target_col)

    # Test the model
    test_data = [['Sunny', 'Hot']]
    prediction = predict(forest[0], test_data[0])  # Using the first tree for example
    print("Prediction for", test_data[0], ":", prediction)

    # Analyze the decision tree structure
    print("Decision Tree 1:")
    print(forest[0])
