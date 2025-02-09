# Bitcoin Price Calculator

## About the Project
This project is a simple command-line tool that calculates the equivalent value of US dollars (USD) in Bitcoin (BTC) using real-time data from the CoinDesk API.

## How It Works
The script takes a USD amount as a command-line argument, fetches the current Bitcoin price from the CoinDesk API, and calculates the corresponding Bitcoin value.

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone the repository:

git clone https://github.com/BernardoMarta/Bitcoin_price
cd Bitcoin_price

### Usage
Run the script from the command line, providing the USD amount as an argument.

python bitcoin.py <USD_amount>

Replace `<USD_amount>` with the amount in USD you want to convert.

## Example

**Input:**
To calculate the Bitcoin equivalent of $100 USD, run:

python bitcoin.py 100


**Output:**
The script will output the equivalent value in Bitcoin, formatted to four decimal places.

## Features
- Fetches real-time Bitcoin price from CoinDesk API
- Converts USD to Bitcoin
- Formats output for readability
- Handles invalid input gracefully

## Contributing
Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/Bitcoin_price)!

## License
This project is licensed under the MIT License.

## Acknowledgments
Thanks to CoinDesk for providing the API used in this project.
