import tkinter as tk
from tkinter import filedialog

def upload_file():
    file_path = filedialog.askopenfilename()
    print(f"File selected: {file_path}")

# Create the main application window
root = tk.Tk()
root.title("Healthcare Dashboard")
root.geometry("600x400")

# Set a background color or image
root.configure(bg="#b3d9ff")  # Light blue background

# Add a title label
title_label = tk.Label(root, text="HEALTHCARE DASHBOARD", font=("Arial", 16, "bold"), bg="black", fg="white")
title_label.pack(fill=tk.X)

# Create a frame to hold form inputs
form_frame = tk.Frame(root, bg="#e6f2ff", bd=2, relief=tk.GROOVE, padx=10, pady=10)
form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=250)

# Name label and entry
name_label = tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#e6f2ff")
name_label.grid(row=0, column=0, pady=5, sticky=tk.W)
name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
name_entry.grid(row=0, column=1, pady=5)

# Age label and entry
age_label = tk.Label(form_frame, text="Age:", font=("Arial", 12), bg="#e6f2ff")
age_label.grid(row=1, column=0, pady=5, sticky=tk.W)
age_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
age_entry.grid(row=1, column=1, pady=5)

# File upload label and button
file_label = tk.Label(form_frame, text="Upload File:", font=("Arial", 12), bg="#e6f2ff")
file_label.grid(row=2, column=0, pady=5, sticky=tk.W)
upload_button = tk.Button(form_frame, text="Choose File", font=("Arial", 10), command=upload_file)
upload_button.grid(row=2, column=1, pady=5, sticky=tk.W)

# Submit button
submit_button = tk.Button(form_frame, text="Submit", font=("Arial", 12), bg="#99ccff", fg="black")
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
