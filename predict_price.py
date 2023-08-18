import os
import pickle

def load_trained_parameters():
    with open("model_parameters.txt", "r") as f:
        theta0 = float(f.readline().strip())
        theta1 = float(f.readline().strip())
    return theta0, theta1


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def main():
    theta0, theta1 = load_trained_parameters()
    
    while True:
        try:
            mileage = float(input("Enter the mileage of the car: "))

            # Check for extreme numbers and notify the user
            if mileage > 1e6:
                print("Warning: The entered mileage is extremely high and the prediction may not be accurate.")

            price = estimate_price(mileage, theta0, theta1)

            # Clip the price if it goes below 0
            if price < 0:
                price = 0
                print(f"The predicted price for the car with {mileage} km mileage is less than 0. Clipping to 0.")
            else:
                print(f"Estimated price for the car with {mileage:.2f} km mileage: {price:.2f}")

            another = input("Do you want to predict another price? (yes/no): ").strip().lower()
            if another != 'yes':
                break
        except ValueError:
            print("Please enter a valid mileage.")

if __name__ == "__main__":
    main()
