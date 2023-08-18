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

def plot_data(mileage, price, color, label):
    plt.scatter(mileage, price, color=color, label=label)

def main():
    original_mileage, original_price = read_csv("data.csv")
    underfit_mileage, underfit_price = read_csv("data_underfit.csv")

    plot_data(original_mileage, original_price, color='blue', label='Original Data')
    plot_data(underfit_mileage, underfit_price, color='orange', label='Underfit Data')
    
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Comparison between Original and Underfit Datasets')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
