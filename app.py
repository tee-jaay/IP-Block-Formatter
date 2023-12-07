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

# Join the unique IP addresses back together with each address on a separate line, prefixed with "deny from"
formatted_data = '\n'.join('deny from ' + ip for ip in unique_ip_addresses)

# Print the formatted data
print(formatted_data)