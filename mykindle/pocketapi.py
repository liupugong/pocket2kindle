from __future__ import absolute_import, print_function, unicode_literals, with_statement

import sys

#import webbrowser
from collections import OrderedDict

import requests

from .consts import Consts

try:
    import ConfigParser as configparser
except ImportError:
    import configparser
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


class PocketAPI(object):
    def __init__(self):
        self._consumer_key = None
        self._request_token = None
        self._access_token = None
        self._username = None


    @property
    def credentials(self):
        return {
            'access_token': self._access_token,
            'username': self._username,
        }

    def obtain_request_token(self):
        payload = {
            'consumer_key': Consts.POCKET_COSUME_KEY,
            'redirect_uri': Consts.RETURN_URL,
        }
        req = Network.post_request(Consts.REQUEST_TOKEN_URL, payload)
        info = urlparse.parse_qs(req.text)

        self._request_token = info['code'][0]
        return self._request_token

    def obtain_access_token(self):
        payload = {
            'consumer_key': self._consumer_key,
            'code': self._request_token,
        }
        req = Network.post_request(Consts.ACCESS_TOKEN_URL, payload)
        info = urlparse.parse_qs(req.text)

        self._access_token = info['access_token'][0]
        self._username = info['username'][0]
        return self._access_token


class Network(object):
    """
    Safe POST Request, with error-handling
    """

    @staticmethod
    def post_request(link, payload):
        req = requests.post(link, json=payload)

        if req.status_code != 200:
            # print_bug_report('API Error {0} ! : {1}'.format(
            #     req.headers.get('X-Error-Code'),
            #     req.headers.get('X-Error'),
            # ))
            # to do: add log
            sys.exit(1)
        else:
            try:  # preserve json response ordering, as per API
                req.api_json = req.json(object_pairs_hook=OrderedDict)
            except ValueError:
                req.api_json = {}
            finally:
                return req


class Browser(object):
    """
    Silently open browser windows/tabs
    """

    @classmethod
    def open_new_window(cls, link):
        cls.open(link, new=1)

    @classmethod
    def open_new_tab(cls, link):
        cls.open(link, new=2)