def calculate_mean(values):
    """
    This function takes a list (or numpy array) of values and returns their
    mean.
    Used for calculating the mean of X and Y.
    """
    if not values:
        return None  # Handle empty list case
    
    total = sum(values)
    count = len(values)
    mean = total / count
    return mean

def calculate_slope(X, Y, mean_X, mean_Y):
    """
    This function calculates the slope (theta_1) of the regression line.
    The slope is computed using the formula that relates covariance of X
    and Y to variance of X.
    """
    n = len(X)
    numerator = sum([(X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)])
    denominator = sum([(X[i] - mean_X) ** 2 for i in range(n)])
    slope = numerator / denominator
    return slope

def calculate_intercept(mean_X, mean_Y, slope):
    """
    This function calculates the intercept (theta_0) of the regression
    line.
    The intercept is the value of Y when X = 0.
    """
    intercept = mean_Y - slope * mean_X
    return intercept

def predict(X, theta_0, theta_1):
    """
    This function predicts the target values (Y) based on the learned
    model.
    It uses the formula: Y = theta_0 + theta_1 * X
    """
    Y_pred = [theta_0 + theta_1 * x for x in X]
    return Y_pred

def calculate_mse(Y, Y_pred):
    """
    This function calculates the Mean Squared Error (MSE) between the true
    target values Y and the predicted values Y_pred.
    MSE is used to evaluate the performance of the regression model.
    """
    n = len(Y)
    mse = sum([(Y[i] - Y_pred[i])**2 for i in range(n)]) / n
    return mse

def gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations):
    """
    This function adjusts the weights (theta_0 and theta_1) using 
    gradient descent to minimize the Mean Squared Error.
    The function iteratively updates the weights to reduce the 
    prediction error.
    """
    n = len(X)
    
    for _ in range(iterations):
        # Compute predictions
        Y_pred = predict(X, theta_0, theta_1)
        
        # Calculate the gradients
        gradient_theta_0 = (-2/n) * sum(Y[i] - Y_pred[i] for i in range(n))
        gradient_theta_1 = (-2/n) * sum((Y[i] - Y_pred[i]) * X[i] for i in range(n))
        
        # Update the parameters (theta_0 and theta_1)
        theta_0 -= learning_rate * gradient_theta_0
        theta_1 -= learning_rate * gradient_theta_1
    
    return theta_0, theta_1

def fit_linear_regression(X, Y, learning_rate=0.01, iterations=1000):
    """
    This function fits the linear regression model by first calculating 
    the slope and intercept,
    then applying gradient descent to adjust the weights (theta_0 and 
    theta_1).
    It returns the optimal values for theta_0 and theta_1.
    """
    # Calculate the mean of X and Y
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)

    # Calculate the initial slope (theta_1) and intercept (theta_0)
    theta_1 = calculate_slope(X, Y, mean_X, mean_Y)
    theta_0 = calculate_intercept(mean_X, mean_Y, theta_1)

    # Apply gradient descent to fine-tune the parameters
    theta_0, theta_1 = gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations)

    return theta_0, theta_1

def test_model(X, Y):
    """
    This function tests the linear regression model using a given dataset.
    It calculates the model parameters, makes predictions, and evaluates
    performance using MSE.
    """
    # Fit the linear regression model
    theta_0, theta_1 = fit_linear_regression(X, Y)
    
    # Make predictions
    Y_pred = predict(X, theta_0, theta_1)

    # Calculate Mean Squared Error
    mse = calculate_mse(Y, Y_pred)

    print("Slope (theta_1):", theta_1)
    print("Intercept (theta_0):", theta_0)
    print("Mean Squared Error:", mse)

if __name__ == "__main__":
    # Hardcoded dataset (Experience, Salary)
    X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Experience
    Y = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]  # Salary

    # Test the model
    test_model(X, Y)