import os
import tkinter as tk
from tkinter import messagebox

def shutdown_timer(minutes, action):
    seconds = minutes * 60
    if action.lower() == "shutdown":
        os.system(f"shutdown -s -t {seconds}")
        messagebox.showinfo("Shutdown Timer", f"Your computer will shutdown in {minutes} minutes.")
    elif action.lower() == "restart":
        os.system(f"shutdown -r -t {seconds}")
        messagebox.showinfo("Shutdown Timer", f"Your computer will restart in {minutes} minutes.")
    else:
        messagebox.showerror("Shutdown Timer", "Invalid action. Please choose 'shutdown' or 'restart'.")

def on_submit():
    try:
        minutes = int(minutes_entry.get())
        action = action_var.get()
        shutdown_timer(minutes, action)
    except ValueError:
        messagebox.showerror("Shutdown Timer", "Invalid input. Please enter a valid number of minutes.")

# Create the main window
window = tk.Tk()
window.title("Shutdown Timer")

# Minutes entry
minutes_label = tk.Label(window, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(window)
minutes_entry.pack()

# Action selection
action_label = tk.Label(window, text="Action:")
action_label.pack()
action_var = tk.StringVar(window, value="shutdown")
shutdown_radio = tk.Radiobutton(window, text="Shutdown", variable=action_var, value="shutdown")
shutdown_radio.pack()
restart_radio = tk.Radiobutton(window, text="Restart", variable=action_var, value="restart")
restart_radio.pack()

# Submit button
submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

# Start the GUI event loop
window.mainloop()
