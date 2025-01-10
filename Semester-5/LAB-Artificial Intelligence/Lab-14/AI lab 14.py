import numpy as np
import matplotlib.pyplot as plt

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Initialize weights and biases
def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(42)  # For reproducibility
    weights = {
        'W1': np.random.randn(input_size, hidden_size) * 0.01,
        'b1': np.zeros((1, hidden_size)),
        'W2': np.random.randn(hidden_size, output_size) * 0.01,
        'b2': np.zeros((1, output_size))
    }
    return weights

# Forward propagation
def forward_propagation(X, weights):
    W1, b1, W2, b2 = weights['W1'], weights['b1'], weights['W2'], weights['b2']
    
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    
    cache = {'Z1': Z1, 'A1': A1, 'Z2': Z2, 'A2': A2}
    return A2, cache

# Compute binary cross-entropy loss
def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    loss = -1 / m * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

# Backward propagation
def backward_propagation(X, y, weights, cache):
    m = X.shape[0]
    A1, A2 = cache['A1'], cache['A2']
    W2 = weights['W2']
    
    dZ2 = A2 - y.reshape(-1, 1)
    dW2 = 1 / m * np.dot(A1.T, dZ2)
    db2 = 1 / m * np.sum(dZ2, axis=0, keepdims=True)
    
    dZ1 = np.dot(dZ2, W2.T) * A1 * (1 - A1)
    dW1 = 1 / m * np.dot(X.T, dZ1)
    db1 = 1 / m * np.sum(dZ1, axis=0, keepdims=True)
    
    gradients = {'dW1': dW1, 'db1': db1, 'dW2': dW2, 'db2': db2}
    return gradients

# Update weights using gradient descent
def update_parameters(weights, gradients, learning_rate):
    weights['W1'] -= learning_rate * gradients['dW1']
    weights['b1'] -= learning_rate * gradients['db1']
    weights['W2'] -= learning_rate * gradients['dW2']
    weights['b2'] -= learning_rate * gradients['db2']
    return weights

# Train the neural network
def train_network(X, y, hidden_size, learning_rate, epochs):
    input_size = X.shape[1]
    output_size = 1
    weights = initialize_parameters(input_size, hidden_size, output_size)
    
    for epoch in range(epochs):
        y_pred, cache = forward_propagation(X, weights)
        loss = compute_loss(y, y_pred)
        gradients = backward_propagation(X, y, weights, cache)
        weights = update_parameters(weights, gradients, learning_rate)
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")
    
    return weights

# Plot decision boundary
def plot_decision_boundary(X, y, weights):
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z = np.c_[xx.ravel(), yy.ravel()]
    preds, _ = forward_propagation(Z, weights)
    Z = (preds > 0.5).astype(int).reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.Paired)
    plt.title("Decision Boundary")
    plt.show()

# Dataset
X = np.array([
    [0.1, 0.6],
    [0.15, 0.71],
    [0.25, 0.8],
    [0.35, 0.45],
    [0.5, 0.5],
    [0.6, 0.2],
    [0.65, 0.3],
    [0.8, 0.35]
])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])  # Labels

# Hyperparameters
hidden_size = 3
learning_rate = 0.1
epochs = 1000

# Train the network
trained_weights = train_network(X, y, hidden_size, learning_rate, epochs)

# Visualize decision boundary
plot_decision_boundary(X, y, trained_weights)
