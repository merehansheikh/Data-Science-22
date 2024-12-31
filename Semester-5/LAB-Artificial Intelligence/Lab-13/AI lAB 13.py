import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

# Perceptron Implementation
def perceptron(X, y, learning_rate=0.1, epochs=100):
    weights = np.zeros(X.shape[1])
    bias = 0

    for _ in range(epochs):
        for i in range(len(X)):
            linear_output = np.dot(X[i], weights) + bias
            y_pred = 1 if linear_output > 0 else 0
            update = learning_rate * (y[i] - y_pred)
            weights += update * X[i]
            bias += update
    return weights, bias

# Plot Decision Boundary for Perceptron
def plot_perceptron_boundary(X, y, weights, bias):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    grid = np.c_[xx.ravel(), yy.ravel()]
    predictions = np.dot(grid, weights) + bias > 0
    plt.contourf(xx, yy, predictions.reshape(xx.shape), alpha=0.7, cmap='coolwarm')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k')
    plt.title("Perceptron Decision Boundary (Linear)")
    plt.show()

# Train XOR Neural Network
def train_xor_nn(X, y):
    model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000, activation='relu', solver='adam', random_state=42)
    model.fit(X, y)
    return model

# Visualize Decision Boundary for XOR Neural Network
def visualize_xor_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    grid = np.c_[xx.ravel(), yy.ravel()]
    predictions = model.predict(grid)
    plt.contourf(xx, yy, predictions.reshape(xx.shape), alpha=0.7, cmap='coolwarm')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k')
    plt.title("XOR Neural Network Decision Boundary (Non-Linear)")
    plt.show()

# Main Function to Execute Both Tasks
def main():
    # Dataset for AND (Perceptron)
    X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_and = np.array([0, 0, 0, 1])  # AND operation
    weights, bias = perceptron(X_and, y_and)
    print("Perceptron Weights:", weights)
    print("Perceptron Bias:", bias)
    plot_perceptron_boundary(X_and, y_and, weights, bias)

    # Dataset for XOR (Neural Network)
    X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_xor = np.array([0, 1, 1, 0])  # XOR operation
    xor_model = train_xor_nn(X_xor, y_xor)
    visualize_xor_boundary(xor_model, X_xor, y_xor)

if __name__ == "__main__":
    main()
