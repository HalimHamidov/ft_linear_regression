import csv
import matplotlib.pyplot as plt

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

def fit_linear_regression(mileage, price):
    mean_mileage = sum(mileage) / len(mileage)
    mean_price = sum(price) / len(price)
    
    # Calculate the slope (theta1) and intercept (theta0)
    numerator = sum([(mileage[i] - mean_mileage) * (price[i] - mean_price) for i in range(len(mileage))])
    denominator = sum([(mileage[i] - mean_mileage)**2 for i in range(len(mileage))])
    
    theta1 = numerator / denominator
    theta0 = mean_price - theta1 * mean_mileage
    return theta0, theta1

def plot_data_and_regression_line(mileage, price, theta0, theta1):
    plt.scatter(mileage, price, color='blue', label='Quadratic data points')
    plt.plot(mileage, [theta0 + theta1*m for m in mileage], color='red', label='Linear regression')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Underfitting Example: Quadratic Data vs Linear Fit')
    plt.legend()
    plt.show()

def main():
    filename = "data_underfit.csv"
    
    mileage, price = read_csv(filename)
    theta0, theta1 = fit_linear_regression(mileage, price)
    
    plot_data_and_regression_line(mileage, price, theta0, theta1)

if __name__ == "__main__":
    main()
