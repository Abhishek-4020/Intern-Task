import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = (value * 9/5) + 32
            k = value + 273.15
            result.set(f"{value:.2f}°C = {f:.2f}°F\n{value:.2f}°C = {k:.2f}K")
        elif unit == "Fahrenheit":
            c = (value - 32) * 5/9
            k = (value - 32) * 5/9 + 273.15
            result.set(f"{value:.2f}°F = {c:.2f}°C\n{value:.2f}°F = {k:.2f}K")
        elif unit == "Kelvin":
            c = value - 273.15
            f = (value - 273.15) * 9/5 + 32
            result.set(f"{value:.2f}K = {c:.2f}°C\n{value:.2f}K = {f:.2f}°F")
        else:
            messagebox.showerror("Unit Error", "Please select a valid unit.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid numeric temperature.")

def clear_fields():
    entry_temp.delete(0, tk.END)
    result.set("")
    unit_dropdown.current(0)

root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("400x300")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

# Fonts
font_title = ("Arial", 16, "bold")
font_text = ("Arial", 12)

# Title
tk.Label(root, text="Temperature Converter", font=font_title, bg="#f0f8ff", fg="#2c3e50").pack(pady=10)

# Entry
frame_input = tk.Frame(root, bg="#f0f8ff")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Enter Temperature:", font=font_text, bg="#f0f8ff").grid(row=0, column=0, padx=10)
entry_temp = tk.Entry(frame_input, font=font_text, width=15)
entry_temp.grid(row=0, column=1)

# Unit dropdown
tk.Label(frame_input, text="Select Unit:", font=font_text, bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10)
unit_var = tk.StringVar()
unit_dropdown = ttk.Combobox(frame_input, textvariable=unit_var, font=font_text, state="readonly",
                             values=["Celsius", "Fahrenheit", "Kelvin"])
unit_dropdown.grid(row=1, column=1)
unit_dropdown.current(0)

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f8ff")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Convert", font=font_text, bg="#3498db", fg="white", command=convert_temperature).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Clear", font=font_text, bg="#e74c3c", fg="white", command=clear_fields).grid(row=0, column=1, padx=10)

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=font_text, bg="#f0f8ff", fg="#2c3e50", justify="center").pack(pady=10)

# Start the GUI
root.mainloop()
