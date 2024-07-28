## pip install requests
import requests

url = "https://restcountries.com/v3.1/all"
r1 = requests.get(url)
r1
print(r1.json())

# question 1,2,3,4
# fetch all json data,diaplay the name of cuntries,currencies,and currency symbols

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def display_country_info(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})

        if currencies:
            print(f"Country: {name}")
            print("Currencies:")

            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')

                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")

            print("\n")


# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_country_info(countries_data)
else:
    print("Failed to fetch data.")

# question 5-create a method to display the name of countries which have the DOLLAR as its curency.

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def display_countries_with_dollar_currency(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})

        # Check if the currency is "Dollar"
        if any(currency_code.lower() == 'usd' for currency_code in currencies):
            print(f"Country: {name}")
            print("Currencies:")

            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')

                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")

            print("\n")


# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_countries_with_dollar_currency(countries_data)
else:
    print("Failed to fetch data.")

# question-6-Display the countries which have EURO as its curency

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def display_countries_with_euro_currency(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})

        # Check if the currency is "Euro"
        if any(currency_code.lower() == 'eur' for currency_code in currencies):
            print(f"Country: {name}")
            print("Currencies:")

            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')

                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")

            print("\n")


# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_countries_with_euro_currency(countries_data)
else:
    print("Failed to fetch data.")

