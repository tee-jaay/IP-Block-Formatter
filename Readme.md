# IP Block Formatter

This app takes the "Top 5 IPs Blocked" input from Wordfence or any data with the same structure and formats it to be added to the ".htaccess" file for IP blocking.

## Features

- Accepts input data in the format of "Top 5 IPs Blocked" from Wordfence or similar structured data.
- Formats the IP addresses with the necessary directives to block them in the .htaccess file.
- Removes duplicates and ensures each IP address is only included once.
- Provides an easy way to generate the formatted IP addresses for blocking.

## How to Use

1. Prepare the input data in the format of "Top 5 IPs Blocked" from Wordfence or similar structured data.
2. Run the app and provide the input data.
3. The app will format the IP addresses and generate the necessary directives for blocking in the .htaccess file.
4. Copy the formatted output and add it to your .htaccess file to block the specified IP addresses.

## Requirements

- Python 3.10 or above
- Dependencies: python3-tk (ubuntu)

## Installation

1. Clone this repository.
2. Run the app using the command: **python app.py**

## License

MIT License

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
