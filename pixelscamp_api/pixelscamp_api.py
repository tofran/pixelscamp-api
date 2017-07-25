import json
import requests

ENDPOINT = 'https://api.pixels.camp'

class PixelsAPI:
    """
    Pixels camp API wrapper for python
    by tofran https://github.com/tofran/PixelsCamp-API
    """

    def __init__(self, api_key=None, session=None):
        self.login = None
        if api_key is not None:
            self.auth(api_key)
        elif session is not None:
            self.session = session

    def auth(self, api_key):
        """Authentication"""
        resp = requests.post(ENDPOINT + '/user/auth',  headers={'Authorization': api_key})
        if resp.status_code == 200:
            self.session = resp.cookies['sessionid']
            self.login = None
        else:
            raise Exception("Authentication failed!")
        return self.session

    def me(self):
        """Private user information (Authenticated)"""
        self.auth_check()
        resp = requests.get(ENDPOINT + '/user/me',  cookies={'sessionid': self.session})
        return resp.json()

    def users(self, count=None, offset=None):
        """List users (Non authenticated)"""
        resp = requests.get(ENDPOINT + '/users/', params={'count': count, 'offset': offset})
        return resp.json()

    def user(self, login):
        """User public data (Non authenticated)"""
        resp = requests.get(ENDPOINT + '/users/' + login)
        return resp.json()

    def badges_list(self):
        """List badges (Non authenticated )"""
        resp = requests.get(ENDPOINT + '/badges/list')
        return resp.json()

    def badges_owners(self, badge_type):
        """List badges owners (Non authenticated)"""
        resp = requests.get(ENDPOINT + '/badges/owners/' + str(badge_type))
        return resp.json()

    def badges_redeem(self, redeem_code, login = None):
        """Redeem a badge (Authenticated"""
        self.auth_check()
        if login is None and self.login is None:
            login = self.login = self.me()['login']
        resp = requests.get(ENDPOINT + '/badges/redeem/' + login + '/' + str(redeem_code), cookies={'sessionid': self.session})
        return resp.json()

    def auth_check(self):
        if self.session is None:
            raise Exception("Not authenticated!")
