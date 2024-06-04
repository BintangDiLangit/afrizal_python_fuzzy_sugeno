
import pandas as pd
import tkinter as tk
from tkinter import ttk

data_ranges = {
    "Jumlah Koin": {
        "Sangat Sedikit": "0-15",
        "Sedikit": "10-25",
        "Sedang": "20-35",
        "Banyak": "30-45",
        "Sangat Banyak": "40-50"
    },
    "Jumlah Nyawa": {
        "Sangat Sedikit": "0-30",
        "Sedikit": "25-50",
        "Sedang": "45-75",
        "Banyak": "70-90",
        "Sangat Banyak": "85-100"
    },
    "Skor": {
        "Sangat Rendah": "0-30",
        "Rendah": "25-50",
        "Sedang": "45-75",
        "Tinggi": "70-90",
        "Sangat Tinggi": "85-100"
    },
    "Waktu": {
        "Sangat Cepat": "0-15",
        "Cepat": "10-25",
        "Sedang": "20-35",
        "Lama": "30-45",
        "Sangat Lama": "40-50"
    },
}

# Initialize a dictionary to store the maximum values
max_values = {
    "Jumlah Koin": {"value": 0, "attribute": ""},
    "Jumlah Nyawa": {"value": 0, "attribute": ""},
    "Skor": {"value": 0, "attribute": ""},
    "Waktu": {"value": 0, "attribute": ""}
}

inputs = {
    "Jumlah Koin": 10,
    "Jumlah Nyawa": 30,
    "Skor": 25,
    "Waktu": 10
}


def membership_function(input, range):
    # Extract the lower and upper bounds from the range
    lower, upper = map(int, range.split('-'))

    # Calculate the degree of membership
    if input < lower:
        return 0
    elif input > upper:
        return 0
    elif lower <= input <= upper:
        return (input - lower) / (upper - lower)


def get_max_value(data_ranges, inputs):
    # Loop through the outer dictionary
    for key, value in data_ranges.items():
        # Loop through the inner dictionary
        for inner_key, inner_value in value.items():
            # Apply the membership function to each range
            membership_value = membership_function(inputs[key], inner_value)
            # print(f"{key} - {inner_key}: {membership_value}")

            # If this membership value is greater than the current maximum for this key, update the maximum
            if membership_value > max_values[key]["value"]:
                max_values[key]["value"] = membership_value
                max_values[key]["attribute"] = inner_key

    # Print the maximum values and corresponding attributes
    for key, value in max_values.items():
        print(
            f"Final value for {key}: {value['value']} | {value['attribute']}")

    print("\n")
    # Load a sheet into a DataFrame by index
    xl = pd.ExcelFile('only_rules.xlsx')

    # Load a sheet into a DataFrame by its name
    df1 = xl.parse('Sheet1')

    # Iterate over the rows of the DataFrame
    for index, row in df1.iterrows():
        # Compare the values in the columns with the maximum values and corresponding attributes
        if (row['Jumlah Koin'] == max_values['Jumlah Koin']['attribute'] and
            row['Jumlah Nyawa'] == max_values['Jumlah Nyawa']['attribute'] and
            row['Skor'] == max_values['Skor']['attribute'] and
                row['Waktu'] == max_values['Waktu']['attribute']):
            # If all values match, print the rule and feedback
            print(f"Matching rule: {row['Rules']}")
            print(f"Feedback: {row['Umpan Balik']}")


def calculate():
    # Get the inputs from the entry fields
    inputs = {
        "Jumlah Koin": int(entry_jumlah_koin.get()),
        "Jumlah Nyawa": int(entry_jumlah_nyawa.get()),
        "Skor": int(entry_skor.get()),
        "Waktu": int(entry_waktu.get())
    }

    # Calculate the maximum values and corresponding attributes
    # ...

    # Display the results in the text field
    text_output.delete(1.0, tk.END)
    for key, value in max_values.items():
        text_output.insert(
            tk.END, f"Max value for {key}: {value['value']} | {value['attribute']}\n")


# Create a window
window = tk.Tk()

# Create labels and entry fields for the inputs
ttk.Label(window, text="Jumlah Koin:").grid(row=0, column=0)
entry_jumlah_koin = ttk.Entry(window)
entry_jumlah_koin.grid(row=0, column=1)

ttk.Label(window, text="Jumlah Nyawa:").grid(row=1, column=0)
entry_jumlah_nyawa = ttk.Entry(window)
entry_jumlah_nyawa.grid(row=1, column=1)

ttk.Label(window, text="Skor:").grid(row=2, column=0)
entry_skor = ttk.Entry(window)
entry_skor.grid(row=2, column=1)

ttk.Label(window, text="Waktu:").grid(row=3, column=0)
entry_waktu = ttk.Entry(window)
entry_waktu.grid(row=3, column=1)

# Create a button that will calculate the results when clicked
button_calculate = ttk.Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2)

# Create a text field for the output
text_output = tk.Text(window, height=10, width=50)
text_output.grid(row=5, column=0, columnspan=2)

# Start the main loop
window.mainloop()
