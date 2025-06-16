import tkinter as tk
from tkinter import messagebox

def calculate_tip_split():
    try:
        num_people = int(entry_people.get())
        receipt_amt = float(entry_receipt.get())
        tip_percent = float(entry_tip.get())

        tip_amt = receipt_amt * (tip_percent / 100)
        total_amt = receipt_amt + tip_amt
        per_person = total_amt / num_people

        result_text = (
            f"🧾 Receipt: ${receipt_amt:.2f}\n"
            f"💰 Tip ({tip_percent}%): ${tip_amt:.2f}\n"
            f"🪙 Total: ${total_amt:.2f}\n"
            f"👯 Each Pays: ${per_person:.2f}"
        )
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

# Setup GUI
root = tk.Tk()
root.title("Tip & Split Calculator 🍽️")

# Labels & Entries
tk.Label(root, text="👥 Number of People:").grid(row=0, column=0, sticky="e")
entry_people = tk.Entry(root)
entry_people.grid(row=0, column=1)

tk.Label(root, text="🧾 Receipt Amount ($):").grid(row=1, column=0, sticky="e")
entry_receipt = tk.Entry(root)
entry_receipt.grid(row=1, column=1)

tk.Label(root, text="💸 Tip Percentage (%):").grid(row=2, column=0, sticky="e")
entry_tip = tk.Entry(root)
entry_tip.grid(row=2, column=1)

# Calculate Button
tk.Button(root, text="🧮 Calculate Tip & Split", command=calculate_tip_split).grid(row=3, column=0, columnspan=2, pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
