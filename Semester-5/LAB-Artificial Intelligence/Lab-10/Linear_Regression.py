def calculate_mean(values):
    if not values:
        return None  # Handle empty list case

    total = sum(values)
    count = len(values)
    mean = total / count
    return mean

def calculate_slope(X, Y, mean_X, mean_Y):
    n = len(X)
    numerator = sum([(X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)])
    denominator = sum([(X[i] - mean_X) ** 2 for i in range(n)])
    slope = numerator / denominator
    return slope

def calculate_intercept(mean_X, mean_Y, slope):
    intercept = mean_Y - slope * mean_X
    return intercept

def predict(X, theta_0, theta_1):
    Y_pred = [theta_0 + theta_1 * x for x in X]
    return Y_pred

def calculate_mse(Y_true, Y_pred):
    n = len(Y_true)
    mse = sum([(Y_true[i] - Y_pred[i])**2 for i in range(n)]) / n
    return mse

def fit_linear_regression(X, Y):
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