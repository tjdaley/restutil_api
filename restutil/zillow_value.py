"""
zillow_value.py - Retrieve Zillow value information about a property.

Copyright (c) 2020 by Thomas J. Daley. Licensed under BSD License.
"""
import re
import requests
import time
import urllib.parse

from .base_utility import BaseUtility


class Zillow(BaseUtility):
    """
    Retrieve Zillow information about a property.

    Example usage:

    ```python
    from restutil import Zillow
    z = Zillow('my_access_key')
    print(z.info('123 main street', 'dallas, tx 75000'))
    ```
    """

    def info(self, street: str, city_state_zip: str) -> dict:
        """
        Return Zillow information about a property.

        Args:
          street (str): The street address of the property [Required]
          city_state_zip (str): City, state, and ZIP of the property. City and state required. [Required]
        Returns:
          (dict): Dictionary of data about the property.
        """
        url_street = urllib.parse.quote_plus(street)
        url_csz = urllib.parse.quote_plus(city_state_zip.replace(',', ''))
        url = self.urlmaker.url_for('zillow', 'value', street=url_street, city_state_zip=url_csz)
        print(f"URL: {url}")
        response = self._get_response(url)
        return response.json()['data']['response']


def main():
    z = Zillow('my_access_key', '192.168.1.81')
    print(z.info('123 main st', 'dallas tx 7500'))


if __name__ == '__main__':
    main()
