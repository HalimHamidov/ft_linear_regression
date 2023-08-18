def compute_rmse(mileage, price, theta0, theta1):
    m = len(mileage)
    total_error = 0

    for i in range(m):
        predicted_value = theta0 + theta1 * mileage[i]
        total_error += (predicted_value - price[i]) ** 2

    mse = total_error / m
    rmse = mse ** 0.5

    return rmse
