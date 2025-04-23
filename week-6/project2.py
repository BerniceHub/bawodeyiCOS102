import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    location = location_entry.get().strip().lower()
    weight = float(weight_entry.get())

    if location == "ibeju-lekki":
        if weight >= 10:
            charge = 5000
        else:
            charge = 3500
    elif location == "epe":
        if weight >= 10:
            charge = 10000
        else:
            charge = 5000
    else:
        messagebox.showerror("Error", "Invalid location entered!")
        return


    messagebox.showinfo("Delivery Charge", f"The delivery fee is: N{charge}")

window = tk.Tk()
window.title("Simi Services Delivery Charge Calculator")

tk.Label(window, text="Enter Location (Ibeju-Lekki or Epe):").grid(row=0, column=0, padx=10, pady=10)
location_entry = tk.Entry(window)
location_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Enter Weight (in kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate Charge", command=calculate_charge)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
