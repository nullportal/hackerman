import re
import json
import requests

class Github():

    base_api_url = "https://api.github.com/"

    def __init__(self):
        # TODO Set User-Agent, client_secret:key
        pass

    def search(self, query):

        query = self.base_api_url + "search/repositories?q=hack&language=" + query
        print("Query:", query)

        resp = requests.get(query)
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

