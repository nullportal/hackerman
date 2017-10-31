import re
import json
import requests

class Github():

    base_api_url = "https://api.github.com/"

    def __init__(self, client_credentials):
        # Init with our credentials, or just use anauthenticated
        try:
            self.client_id, self.client_secret = client_credentials.split(':')
        except:
            self.client_id, self.client_secret = None, None

    def search(self, query_str, query_lang=None):

        api_query = self._authenticate_req(self.base_api_url + "search/repositories?q=" + query_str)

        # Add optional language filter
        if query_lang:
            api_query += f"language:{query_lang}"

        print("Query:", api_query)

        resp = requests.get(api_query)
        return json.loads(resp.text)

    def get_contents(self, query):

        # Remove instructional tokens
        query = self._authenticate_req(re.sub(r"\{.*\}", "", query))
        print("Query:", query)

        resp = requests.get(query)
        return json.loads(resp.text)

    def get_raw(self, query):

        query = self._authenticate_req(query)
        print("Query:", query)

        resp = requests.get(query)
        return resp.text

    def get_limit(self):
        query = self._authenticate_req(self.base_api_url + "rate_limit")
        print("Query:", query)

        resp = requests.get(query)
        return json.loads(resp.text)

    def _authenticate_req(self, q):
        """ Add client secret/id to given query """
        authenticated_query_url = q

        # Append properly depending on what's already there
        if self.client_id is not None and self.client_secret is not None:
            if '?' in q or '&' in q:
                authenticated_query_url = f"{q}&client_id={self.client_id}&client_secret={self.client_secret}"
            else:
                authenticated_query_url = f"{q}?client_id={self.client_id}&client_secret={self.client_secret}"

        return authenticated_query_url
