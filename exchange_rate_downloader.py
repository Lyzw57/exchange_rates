from requests import get
from json import loads

# TODO: przebudować w klasę
class CurrencyRateDownloader:
    def get_currency_rate(self, currency: str, date: str) -> float:
        """Gets currency exchange rate from Table 'A' National Polish Bank website.

        Args:
            currency (str): currency code
            date (str): date of currency exchange rate

        Returns:
            float: exchange rate from chosen date and currency
        """
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json"
        response = get(url)
        response_json = loads(response.text)

        return response_json['rates'][-1]['mid']


if __name__ == "__main__":
    downloader = CurrencyRateDownloader()
    currency = input()
    date = input()
    print(downloader.get_currency_rate(currency, date))
