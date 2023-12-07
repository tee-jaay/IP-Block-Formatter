# v0.0.3
import csv
import tkinter as tk
from tkinter import filedialog

def format_ip_addresses():
    # Open the text file containing the IP addresses
    file_path = filedialog.askopenfilename(title="Select IP Addresses File")
    if not file_path:
        return

    with open(file_path, 'r') as txt_file:
        # Read the contents of the file
        data = txt_file.read()

    # Split the data by lines
    lines = data.split('\n')

    # Extract only the IP address from each line
    ip_addresses = [line.split()[0] for line in lines if line.strip()]

    # Convert the list of IP addresses to a set to remove duplicates
    unique_ip_addresses = set(ip_addresses)

    # Format the IP addresses with "deny from" prefix
    formatted_data = [['deny from ' + ip] for ip in unique_ip_addresses]

    # Save the formatted data to a CSV file
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not save_path:
        return

    with open(save_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(formatted_data)

    print("Formatted IP addresses written to", save_path)

# Create the Tkinter GUI window
window = tk.Tk()
window.title("IP Address Formatter")

# Create a button to trigger the IP address formatting
format_button = tk.Button(window, text="Format IP Addresses", command=format_ip_addresses)
format_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()