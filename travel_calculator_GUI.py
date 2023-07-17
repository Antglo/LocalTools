
import pandas as pd
import tkinter as tk
from tkinter import ttk

path_file = "Mileage Charts Excel.xlsx"
mile_data = pd.read_excel(path_file, index_col=0)
school_names = mile_data.columns.tolist()
row_data = {
        "Barnes":0,"Beddingfield / WAAT":1,"Central Office":2,"Daniels Learning Ctr.":3,"Darden":4,"Elm City Middle":5,
        "Frederick Douglass":6,"Fike":7,"Forest Hills":8,"Gardners":9,"Hearne":10,"Hunt":11,"Jones":12,	
        "Lee Woodard":13,"Lucama":14,"New Hope":15,"Operations Ctr.":16,"Rock Ridge":17,"Speight":18,"Springfield":19,"Stantonsburg":20,	
        "Toisnot":21,"Vick":22,"Vinson-Bynum":23,"Wells":24,"Wilson Early College":25,"Winstead":26
}

# Function to calculate and display the miles
def calculate_miles():
    start_school = start_var.get()
    dest_school = dest_var.get()

    if start_school not in school_names:
        output_label.config(text="Please enter a valid Starting Point!")
    elif dest_school not in school_names:
        output_label.config(text="Please enter a valid Destination!")
    else:
        miles = mile_data.at[dest_school, start_school]
        output_label.config(text=f"{miles} MILES")

# Create the main window
root = tk.Tk()
root.title("School Mileage Calculator")

# Create dropdown menus for start and destination schools
start_var = tk.StringVar(root)
start_var.set("Select Start School")
start_dropdown = ttk.OptionMenu(root, start_var, *school_names)
start_dropdown.grid(row=0, column=0, padx=10, pady=10)

dest_var = tk.StringVar(root)
dest_var.set("Select Destination")
dest_dropdown = ttk.OptionMenu(root, dest_var, *school_names)
dest_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Create button to calculate miles
calculate_button = ttk.Button(root, text="Calculate Miles", command=calculate_miles)
calculate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create label to display output
output_label = ttk.Label(root, text="", font=("Helvetica", 16))
output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()