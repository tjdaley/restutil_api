import re
import requests

from urlmaker import UrlMaker


class RestUtil(object):
    def __init__(self):
        self.urlmaker = UrlMaker(host='192.168.1.81')

    def average_mortage_rate(self, year: int, month: int = 6, term: int = 30) -> dict:
        """
        Return average mortgage interest rate per Federal Reserve
        of St. Louis.

        Args:
          year (int): Year, e.g. 1999 [Required]
          month (int): Month where 1=January, 12=December, etc. [Default=6]
          term (int): Term of the loan in years. Must be one of 5, 15, or 30. [Default=30]
        Returns:
          (dict): Result Set the interest rate
        """
        url = self.urlmaker.url_for('fred', 'historical_rate', year=year, month=month, term=term)
        response = requests.get(url)
        return response.text


def main():
    ru = RestUtil()
    print(ru.average_mortage_rate(2010))
    print(ru.average_mortage_rate(2010, 10))
    print(ru.average_mortage_rate(2010, 10, 15))


if __name__ == '__main__':
    main()
