import re
import json
import requests

class Github():

    base_api_url = "https://api.github.com/"

    def __init__(self):
        # TODO Set User-Agent, client_secret:key
        pass

    def search(self, query_str, query_lang=None):

        api_query = self.base_api_url + "search/repositories?q=" + query_str

        # Add optional language filter
        if query_lang:
            api_query += f"language:{query_lang}"

        print("Query:", api_query)

        resp = requests.get(api_query)
        return json.loads(resp.text)

    def get_contents(self, query):

        # Remove instructional tokens
        query = re.sub(r"\{.*\}", "", query)
        print("Query:", query)

        resp = requests.get(query)
        return json.loads(resp.text)

    def get_raw(self, query):

        print("Query:", query)

        resp = requests.get(query)
        return resp.text

