def calculate_mean(values):
    """Calculates the mean (average) of a list of values.

    Args:
        values: A list of numerical values.

    Returns:
        The mean of the values.
    """

    if not values:
        return None  # Handle empty list case

    total = sum(values)
    count = len(values)
    mean = total / count
    return mean

def calculate_slope(X, Y, mean_X, mean_Y):
    """Calculates the slope (theta_1) of the linear regression line.

    Args:
        X: A list of independent variable values.
        Y: A list of dependent variable values.
        mean_X: The mean of the independent variable values.
        mean_Y: The mean of the dependent variable values.

    Returns:
        The calculated slope.
    """

    n = len(X)
    numerator = sum([(X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)])
    denominator = sum([(X[i] - mean_X) ** 2 for i in range(n)])
    slope = numerator / denominator
    return slope

def calculate_intercept(mean_X, mean_Y, slope):
    """Calculates the intercept (theta_0) of the linear regression line.

    Args:
        mean_X: The mean of the independent variable values.
        mean_Y: The mean of the dependent variable values.
        slope: The calculated slope of the regression line.

    Returns:
        The calculated intercept.
    """

    intercept = mean_Y - slope * mean_X
    return intercept

def predict(X, theta_0, theta_1):
    """Makes predictions using the learned linear regression model.

    Args:
        X: A list of independent variable values.
        theta_0: The intercept of the regression line.
        theta_1: The slope of the regression line.

    Returns:
        A list of predicted dependent variable values.
    """

    Y_pred = [theta_0 + theta_1 * x for x in X]
    return Y_pred

def calculate_mse(Y_true, Y_pred):
    """Calculates the Mean Squared Error (MSE) between true and predicted values.

    Args:
        Y_true: A list of true dependent variable values.
        Y_pred: A list of predicted dependent variable values.

    Returns:
        The calculated Mean Squared Error.
    """

    n = len(Y_true)
    mse = sum([(Y_true[i] - Y_pred[i])**2 for i in range(n)]) / n
    return mse

def fit_linear_regression(X, Y):
    """Fits a linear regression model to the given data.

    Args:
        X: A list of independent variable values.
        Y: A list of dependent variable values.

    Returns:
        A tuple containing the calculated slope (theta_1) and intercept (theta_0).
    """

    # Calculate the mean of X and Y
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)

    # Calculate the slope (theta_1)
    theta_1 = calculate_slope(X, Y, mean_X, mean_Y)

    # Calculate the intercept (theta_0)
    theta_0 = calculate_intercept(mean_X, mean_Y, theta_1)

    return theta_0, theta_1

if __name__ == "__main__":
    # Sample dataset
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 7, 8]

    # Fit the linear regression model
    theta_0, theta_1 = fit_linear_regression(X, Y)

    # Make predictions
    Y_pred = predict(X, theta_0, theta_1)

    # Calculate Mean Squared Error
    mse = calculate_mse(Y, Y_pred)

    print("Slope (theta_1):", theta_1)
    print("Intercept (theta_0):", theta_0)
    print("Mean Squared Error:", mse)