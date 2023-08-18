import csv

def read_original_data(filename):
    mileage = []
    price = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        
        for row in reader:
            mileage.append(float(row[0]))
            price.append(float(row[1]))

    return mileage, price

def generate_underfit_data(mileage, price):
    # We'll simply take every 4th data point to generate a sparser dataset
    underfit_mileage = mileage[::4]
    underfit_price = price[::4]
    
    return underfit_mileage, underfit_price

def save_to_csv(filename, mileage, price):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['km', 'price'])
        for m, p in zip(mileage, price):
            writer.writerow([m, p])

def main():
    original_mileage, original_price = read_original_data("data.csv")
    
    underfit_mileage, underfit_price = generate_underfit_data(original_mileage, original_price)
    
    save_to_csv("data_underfit.csv", underfit_mileage, underfit_price)
    print("data_underfit.csv generated!")

if __name__ == "__main__":
    main()
