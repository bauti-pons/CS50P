import sys
import requests


def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    # Try to convert the argument to a float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Attempt to get the Bitcoin price and calculate the cost
    try:
        cost = bitcoin_price(num_bitcoins)
        print(f"${cost:,.4f}")
    except requests.RequestException:
        sys.exit("Failed to fetch the Bitcoin Price Index")


def bitcoin_price(num_bitcoins):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    return price_per_bitcoin * num_bitcoins


if __name__ == "__main__":
    main()
