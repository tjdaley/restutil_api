"""
base_utility.py - Retrieve information from utility server.

Copyright (c) 2020 by Thomas J. Daley. Licensed under BSD License.
"""
import re
import requests
import time

from .urlmaker import UrlMaker


class BaseUtility(object):
    """
    Retrieve information from our utility server.
    """
    def __init__(self, api_key: str, host: str = 'localhost'):
        """
        Class initializer.

        Args:
            api_key (str): Unique key assigned to your application.
            host (str): Host that is serving the information we seek.
        """
        self.urlmaker = UrlMaker(api_key, host=host)
        self.auth = (api_key, None)

    def _get_response(self, url: str):
        """
        Retrieve response from server, with retry logic.

        Args:
            url (str): URL to retrieve.
        Returns:
            requests.response if OK otherwise an exception.
        """
        rate_limit_retries_remaining = 5
        while rate_limit_retries_remaining > 0:
            response = requests.get(url, auth=self.auth)
            if response.status_code == 401:
                raise Exception(response.text)
            response_json = response.json()
            if response_json['success'] is True:
                return response
            if response_json['code'] == 'ERR_RATE_LIMIT' and rate_limit_retries_remaining > 0:
                time.sleep(1)
                rate_limit_retries_remaining -= 1
        message = f"{response_json['message']} ({response_json['code']})"
        raise Exception(message)
