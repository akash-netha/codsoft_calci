import tkinter as tk

# Function to update the input field when a button is clicked
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Input field
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place buttons in the grid
row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 18", padx=20, pady=20)
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main event loop
root.mainloop()
