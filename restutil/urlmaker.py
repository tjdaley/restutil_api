"""
urlmaker.py - Class for creating URLS based on what the server says it can do.

Copyright (c) 2020 by Thomas J. Daley, J.D. All Rights Reserved.
"""
import re
import requests


class UrlMaker(object):
    def __init__(self, host: str = 'localhost', port: int = 8081):
        self.__pattern_cache = {}
        self.__url = f'http://{host}:{port}'

    def url_for(self, service: str, query: str, **kwargs):
        params = kwargs

        # Define the basic URL that we will query
        url = f'{self.__url}/sitemap/{service}/{query}/'

        # See if we have asked the destination sitemap for this
        # url before. If so, used the cached response. If not, then
        # query the sitemap for matching URLs.
        patterns = self.__from_cache(url)
        if patterns is None:
            patterns = self.__get_service_patterns(url)
        if patterns is None:
            raise Exception(f"No patterns exist for {service} {query}")

        # The form of URL for retrieving data..
        url = f'{self.__url}/{service}/{query}/'

        # Of the patterns returned by the sitemap (or cache), see
        # which our query params (in kwargs) matches the best.
        pattern, pattern_params = self.__select_service_pattern(patterns, params)

        # If we found a good URL to query, do the query. Otherwise
        # raise an exception and quit.
        if pattern:
            if params is not None:
                url = self.__make_url(url, pattern_params, params)
                return url
            return f'{self.__url}{pattern}'
        raise Exception(f"No url available for {url}")

    def __from_cache(self, url):
        return self.__pattern_cache.get(url, None)

    def __to_cache(self, url, patterns):
        self.__pattern_cache[url] = patterns

    def __clear_cache(self):
        self.__pattern_cache = {}

    @staticmethod
    def __get_service_patterns(url):
        response = requests.get(url)
        patterns = response.json()
        return patterns

    @staticmethod
    def __get_pattern_params(pattern):
        """
        For a given pattern that we received from the sitemap,
        extract the parameters it takes.
        """
        url_params = re.findall(r'(<.*:.*>)', pattern)
        if not url_params:
            return []
        url_params = url_params[0].split('/')
        result = []
        for url_param in url_params:
            param_name = re.findall(r'<.*:(.*)>', url_param)
            if param_name:
                result.append(param_name[0])
        return result

    @staticmethod
    def __pattern_has_all_params(pattern, param_keys):
        for param in param_keys:
            if f':{param}>' not in pattern:
                return False
        return True

    @staticmethod
    def __request_has_all_params(pattern_params, request_params):
        for p in pattern_params:
            if p not in request_params:
                return False
        return True

    @staticmethod
    def __select_service_pattern(patterns, params):
        keys = params.keys()
        for pattern in patterns:
            if UrlMaker.__pattern_has_all_params(pattern, keys):
                pattern_params = UrlMaker.__get_pattern_params(pattern)
                if UrlMaker.__request_has_all_params(pattern_params, keys):
                    return pattern, pattern_params
        return None, None

    @staticmethod
    def __make_url(url, pattern_params, query_params):
        for p in pattern_params:
            url += f'{query_params[p]}/'
        return url
