import csv
import os
from data_visualization import plot_data, plot_regression_line, display_graph
# Assuming the RMSE function is in evaluation_metrics.py
from evaluation_metrics import compute_rmse

def read_csv(filename):
    mileage = []
    price = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        
        for row in reader:
            mileage.append(float(row[0]))
            price.append(float(row[1]))

    return mileage, price

def normalize(lst):
    mean = sum(lst) / len(lst)
    std_dev = (sum([(i - mean) ** 2 for i in lst]) / len(lst)) ** 0.5
    return [(i - mean) / std_dev for i in lst], mean, std_dev

def gradient_descent(mileage, price, theta0, theta1, learningRate, iterations):
    m = len(mileage)
    
    for _ in range(iterations):
        tmp_theta0_adjustment = (1/m) * sum( (theta0 + theta1 * mileage[i] - price[i]) for i in range(m) )
        tmp_theta1_adjustment = (1/m) * sum( (theta0 + theta1 * mileage[i] - price[i]) * mileage[i] for i in range(m) )
        
        # Simultaneous update
        theta0 -= learningRate * tmp_theta0_adjustment
        theta1 -= learningRate * tmp_theta1_adjustment

    return theta0, theta1

def main():
    filename = "data.csv"
    
    # Read and normalize data
    mileage, price = read_csv(filename)
    mileage_normalized, mileage_mean, mileage_std = normalize(mileage)
    price_normalized, price_mean, price_std = normalize(price)
    
    theta0, theta1 = 0, 0
    learningRate = 0.1
    iterations = 1000
    
    theta0, theta1 = gradient_descent(mileage_normalized, price_normalized, theta0, theta1, learningRate, iterations)
    
    # Denormalizing the theta values
    theta0 = price_mean - (theta1 * mileage_mean) / mileage_std
    theta1 = theta1 * price_std / mileage_std

    print(f"Trained model parameters: theta0={theta0}, theta1={theta1}")
    
    # After training your model and getting theta0 and theta1
    # Load original mileage and price for evaluation
    rmse = compute_rmse(mileage, price, theta0, theta1)
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

    # Save theta0 and theta1 to a file for future predictions
    with open("model_parameters.txt", "w") as f:
        f.write(f"{theta0}\n")
        f.write(f"{theta1}\n")

    # Visualization block
    plot_data(mileage, price)  # Plot the original data
    plot_regression_line(mileage, theta0, theta1)  # Plot the regression line
    display_graph()

if __name__ == "__main__":
    main()