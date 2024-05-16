import sys
from datetime import date, datetime
import matplotlib.pyplot as plt

def handle_plot():
    dates = []
    relative_days = []
    weights = []
    try:
        with open('data.csv', 'r') as file:
            file_data = file.readlines()
            for item in file_data:
                time, weight = item.split(',')
                year, month, day = time.split('-')
                dates.append(datetime(int(year), int(month), int(day)))
                weights.append(float(weight.strip()))

        for d in dates:
            if d == dates[0]:
                relative_days.append(0)
            else:
                relative_days.append(int((d - dates[0]).days))
        
        plt.plot(relative_days, weights)
        plt.xlabel('Days Since Start of Tracking')
        plt.ylabel('Weight in lbs')
        plt.title('Tracked Weight Over Time')
        plt.show()

    except:
        print("No data to plot!")

def handle_cmd_args():
    if len(sys.argv) != 2:
        print("Error: invalid number of args!")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == 'p' or arg == 'plot':
        handle_plot()
        sys.exit(0)

    try:
        weight = float(arg)
    except:
        print(f"Error: invalid input {arg}. Please input a numerical value!")
        sys.exit(1)

    return weight

def handle_file_write(data):
    with open('data.csv', '+a') as file:
        file.write(f"{date.today()},{data}\n")

def handle_status(weight):
    status = ""
    while status != "yes" and status != "y" and status != "no" and status != "n":
        status = input(f"Is input {weight} correct? (yes/no or y/n)\n").strip().lower()

        if status == "yes" or status == "y":
            handle_file_write(weight)
        elif status == "no" or status == "n":
            print("not adding to data.")
        else:
            print(f"Error: unspecified status {status}!")


if __name__ == "__main__":
    weight = handle_cmd_args()
    handle_status(weight)
    