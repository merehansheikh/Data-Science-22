from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import math

def calculate_entropy(data, target_col):
  """
  Calculates the entropy of a given dataset.

  Args:
    data: The dataset as a pandas DataFrame.
    target_col: The name of the target column.

  Returns:
    The entropy of the dataset.
  """

  # Count the occurrences of each class in the target column
  class_counts = data[target_col].value_counts()

  # Calculate the probability of each class
  class_probs = class_counts / len(data)

  # Calculate entropy using the formula:
  # Entropy = - Σ p(i) * log2(p(i))
  entropy = -sum(p * math.log2(p) for p in class_probs)

  return entropy

def calculate_information_gain(data, attribute, target_col):
  """
  Calculates the information gain of an attribute.

  Args:
    data: The dataset as a pandas DataFrame.
    attribute: The name of the attribute.
    target_col: The name of the target column.

  Returns:
    The information gain of the attribute.
  """

  # Calculate the entropy of the entire dataset
  total_entropy = calculate_entropy(data, target_col)

  # Group the data by the attribute and calculate the weighted entropy
  weighted_entropy = 0
  for value, group in data.groupby(attribute):
    group_entropy = calculate_entropy(group, target_col)
    weighted_entropy += len(group) / len(data) * group_entropy

  # Calculate information gain
  information_gain = total_entropy - weighted_entropy

  return information_gain

def build_tree(data, attributes, target_col):
  """
  Recursively builds a decision tree.

  Args:
    data: The dataset as a pandas DataFrame.
    attributes: A list of attributes to consider.
    target_col: The name of the target column.

  Returns:
    The root node of the decision tree.
  """

  # Base case: If all data points belong to the same class, return a leaf node
  if len(data[target_col].unique()) == 1:
    return data[target_col].iloc[0]

  # If no more attributes to consider, return the majority class
  if len(attributes) == 0:
    return data[target_col].mode()[0]

  # Find the best attribute to split on
  best_attribute = max(attributes, key=lambda x: calculate_information_gain(data, x, target_col))

  # Create a tree with the best attribute as the root
  tree = {best_attribute: {}}

  # Remove the best attribute from the list of attributes
  attributes.remove(best_attribute)

  # For each value of the best attribute, create a branch
  for value in data[best_attribute].unique():
    subtree = build_tree(data[data[best_attribute] == value], attributes.copy(), target_col)
    tree[best_attribute][value] = subtree

  return tree

def predict(tree, data_point):
  """
  Predicts the class for a given data point.

  Args:
    tree: The decision tree.
    data_point: A dictionary containing the attribute-value pairs of the data point.

  Returns:
    The predicted class.
  """

  current_node = tree

  while isinstance(current_node, dict):
    attribute = list(current_node.keys())[0]
    value = data_point[attribute]
    current_node = current_node[attribute][value]

  return current_node


def generate_weather_dataset(num_samples):
  """
  Generates a random dataset for weather prediction.

  Args:
    num_samples: Number of samples in the dataset.

  Returns:
    A pandas DataFrame containing the generated dataset.
  """

  weather_conditions = ["Sunny", "Overcast", "Rainy"]
  temperatures = ["Hot", "Mild", "Cool"]

  # Generate random weather conditions and temperatures
  weather = np.random.choice(weather_conditions, num_samples)
  temperature = np.random.choice(temperatures, num_samples)

  # Create a DataFrame
  data = pd.DataFrame({"Weather": weather, "Temperature": temperature})

  # Generate random target values (Play or No Play)
  target_values = np.random.choice(["Play", "No Play"], num_samples)
  data["Play"] = target_values

  return data

def test_tree(tree, test_data, target_col):
  """
  Tests the decision tree on a test dataset.

  Args:
    tree: The decision tree.
    test_data: The test dataset as a pandas DataFrame.
    target_col: The name of the target column.

  Returns:
    The accuracy of the predictions.
  """

  correct_predictions = 0
  total_predictions = len(test_data)

  for index, row in test_data.iterrows():
    data_point = row.to_dict()
    predicted_class = predict(tree, data_point)
    actual_class = row[target_col]

    if predicted_class == actual_class:
      correct_predictions += 1

  accuracy = correct_predictions / total_predictions
  return accuracy



# Generate a random weather dataset
weather_data = generate_weather_dataset(100)

# Specify the target column
target_col = "Play"

# Get the list of attributes
attributes = list(weather_data.columns)
attributes.remove(target_col)

# Build the decision tree
tree = build_tree(weather_data, attributes, target_col)

# Print the decision tree (for visualization)
print(tree)

# Create a new data point to test
new_data_point = {"Weather": "Rainy", "Temperature": "Mild"}

# Predict the class for the new data point
predicted_class = predict(tree, new_data_point)
print("Predicted class:", predicted_class)

# Split the data into training and testing sets
train_data, test_data = train_test_split(weather_data, test_size=0.2, random_state=42)

# Test the tree on the test dataset
accuracy = test_tree(tree, test_data, target_col)
print("Accuracy:", accuracy)

# Example usage:

