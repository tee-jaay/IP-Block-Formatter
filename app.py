import csv

# Open the text file containing the IP addresses
with open('ip_addresses.txt', 'r') as txt_file:
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

# Write the formatted data to a CSV file
with open('formatted_ip_addresses.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(formatted_data)

print("Formatted IP addresses written to 'formatted_ip_addresses.csv'")