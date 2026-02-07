import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2018_simple.csv'


def load_weather_data():
    """Load dates, highs, and lows from the CSV file."""
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                continue

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_temps(dates, temps, color, title):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def main():
    dates, highs, lows = load_weather_data()

    while True:
        print("\n--- Sitka Weather Menu ---")
        print("1) High Temperatures")
        print("2) Low Temperatures")
        print("3) Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            plot_temps(dates, highs, "red", "Daily High Temperatures - 2018")

        elif choice == "2":
            plot_temps(dates, lows, "blue", "Daily Low Temperatures - 2018")

        elif choice == "3":
            print("\nExiting program. Goodbye!\n")
            sys.exit()

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


main()
