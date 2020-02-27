"""
mortgage_rates.py - Retrieve mortgage rate information from utility server.

Copyright (c) 2020 by Thomas J. Daley. Licensed under BSD License.
"""
import re
import requests
import time

from .base_utility import BaseUtility


class MortgageRates(BaseUtility):
    """
    Retrieve historical mortgage rate information.

    Example usage:

    ```python
    from restutil import MortgageRates
    mr = MortgageRates('my_access_key')
    print(mr.average_mortgage_rate(2020, 1, 30))
    >>> 0.0362
    ```
    """
    def average_mortgage_rate(self, year: int, month: int = 6, term: int = 30) -> dict:
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
        response = self._get_response(url)
        return response.json()['data']['response']


def main():
    mr = MortgageRates('my_access_key', '192.168.1.81')
    for i in range(5):
        print(mr.average_mortgage_rate(2010, i+1, 15))


if __name__ == '__main__':
    main()
