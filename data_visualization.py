# data_visualization.py
import matplotlib.pyplot as plt

def plot_data(mileage, price):
    plt.scatter(mileage, price, color='blue', label='Data points')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Car Mileage vs Price')
    plt.legend()

def plot_regression_line(mileage, theta0, theta1):
    x = list(range(int(min(mileage)), int(max(mileage))))
    y = [theta0 + theta1 * val for val in x]
    
    plt.plot(x, y, color='red', label='Linear regression')
    plt.legend()

def display_graph():
    plt.show()
