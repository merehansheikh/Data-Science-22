import numpy as np
import matplotlib.pyplot as plt

# Hardcoded dataset
X = np.array([[0.1, 1.1], [1.2, 0.9], [1.5, 1.6], [2.0, 1.8], [2.5, 2.1], 
              [0.5, 1.5], [1.8, 2.3], [0.2, 0.7], [1.9, 1.4], [0.8, 0.6]])
y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])

# Standardize the features
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std

# Visualize the data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('Feature 1 (X1)')
plt.ylabel('Feature 2 (X2)')
plt.title('Data Distribution')
plt.show()

def sigmoid(z):
    """Compute the sigmoid of z."""
    return 1 / (1 + np.exp(-z))

def cross_entropy_loss(y_true, y_pred):
    """Compute binary cross-entropy loss."""
    m = y_true.shape[0]
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    loss = -1/m * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

def gradient_descent(X, y, weights, learning_rate, iterations):
    """Perform gradient descent."""
    m = len(y)
    losses = []
    for i in range(iterations):
        z = np.dot(X, weights)
        y_pred = sigmoid(z)
        dw = (1/m) * np.dot(X.T, (y_pred - y))
        weights = weights - learning_rate * dw
        loss = cross_entropy_loss(y, y_pred)
        losses.append(loss)
        if i % 100 == 0:
            print(f"Iteration {i}: Loss = {loss}")
    return weights, losses

def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    """
    Fit logistic regression model using gradient descent.

    Args:
        X: Input features (numpy array).
        y: True labels (numpy array).
        learning_rate: Learning rate for gradient descent (float).
        iterations: Number of iterations for gradient descent (int).

    Returns:
        weights: Trained weights (numpy array).
        losses: List of losses during training.
    """
    # Add a bias term (intercept) to X
    X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)  # Add a column of ones

    # Initialize weights
    weights = np.zeros(X.shape[1]) 

    # Perform gradient descent
    weights, losses = gradient_descent(X, y, weights, learning_rate, iterations)

    return weights, losses

# Train the model with different learning rates
learning_rates = [0.01, 0.1]
for lr in learning_rates:
    weights, losses = logistic_regression(X, y, learning_rate=lr, iterations=1000)
    print(f"Learning Rate: {lr}")
    print("Trained Weights:", weights)
    print("Final Loss:", losses[-1])
    print("-"*20)

def predict(X, weights):
    """
    Predict class labels for given input features using logistic regression.

    Args:
        X: Input features (numpy array).
        weights: Trained weights (numpy array).

    Returns:
        predictions: Predicted class labels (numpy array of 0s and 1s).
    """
    # Add a bias term (intercept) to X for prediction
    X_with_bias = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1) 
    z = np.dot(X_with_bias, weights) 
    probabilities = sigmoid(z)
    predictions = (probabilities >= 0.5).astype(int)  # Convert probabilities to 0 or 1
    return predictions

def evaluate(y_true, y_pred):
    """
    Calculate the accuracy of predictions.

    Args:
        y_true: True labels (numpy array).
        y_pred: Predicted labels (numpy array).

    Returns:
        accuracy: The accuracy score (float).
    Raises:
        ValueError: If the input arrays have different lengths.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("True and predicted labels must have the same length.")

    correct_predictions = np.sum(y_true == y_pred)
    total_predictions = len(y_true)
    accuracy = correct_predictions / total_predictions
    return accuracy

# Make predictions
y_pred = predict(X, weights)

# Evaluate the model
accuracy = evaluate(y, y_pred)
print("Accuracy:", accuracy)

# Plot the decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))

Z = predict(np.c_[xx.ravel(), yy.ravel()], weights)
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.2)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('Feature 1 (X1)')
plt.ylabel('Feature 2 (X2)')
plt.title('Decision Boundary')
plt.show()

