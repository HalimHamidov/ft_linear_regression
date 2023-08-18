import csv
import random

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

def generate_noisy_data(mileage, price, noise_level=0.1):
    noisy_mileage = [m + random.uniform(-m * noise_level, m * noise_level) for m in mileage]
    noisy_price = [p + random.uniform(-p * noise_level, p * noise_level) for p in price]
    return noisy_mileage, noisy_price

def write_to_csv(filename, mileage, price):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["km", "price"])  # header
        for m, p in zip(mileage, price):
            writer.writerow([m, p])

def main():
    filename_original = "data.csv"
    filename_noisy = "data_overfit.csv"
    
    mileage, price = read_csv(filename_original)
    noisy_mileage, noisy_price = generate_noisy_data(mileage, price)
    
    # Combine original and noisy data
    combined_mileage = mileage + noisy_mileage
    combined_price = price + noisy_price
    
    write_to_csv(filename_noisy, combined_mileage, combined_price)

if __name__ == "__main__":
    main()
