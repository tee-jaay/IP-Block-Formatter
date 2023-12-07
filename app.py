# v0.0.4
import csv
import tkinter as tk
from tkinter import filedialog

def format_ip_addresses():
    # Get the IP addresses from the text area
    ip_addresses = text_area.get("1.0", tk.END).strip().split('\n')

    # Format the IP addresses with "deny from" prefix
    formatted_data = [['deny from ' + ip.split()[0]] for ip in ip_addresses if ip.strip()]

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

# Create a text area for entering IP addresses
text_area = tk.Text(window, height=10, width=40)
text_area.pack(padx=10, pady=10)

# Create a button to trigger the IP address formatting
format_button = tk.Button(window, text="Format IP Addresses", command=format_ip_addresses)
format_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()