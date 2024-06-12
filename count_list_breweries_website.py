""""
Visit the url-https://www.openbrewerydb.org/documentation/ write a python script which will do a the following
4.) Count and list how many breweries have websites in the states of Alaska,Maine and New York
"""

import requests
import json

class Brewery:
    def __init__(self, states):
        self.states = states
        self.base_url = "https://api.openbrewerydb.org/breweries"
        self.breweries_with_websites = {}

    def fetch_breweries(self):
        for state in self.states:
            response = requests.get(f"{self.base_url}?by_state={state}&per_page=3")
            if response.status_code == 200:
                breweries_data = response.json()
                self.breweries_with_websites[state] = [brewery['name'] for brewery in breweries_data if brewery['website_url']]
            else:
                print(f"Failed to fetch breweries for {state}")
                self.breweries_with_websites[state] = []

    def websites_to_json(self):
        return json.dumps(self.breweries_with_websites, indent=4)

    def websites_count_to_json(self):
        websites_count = {state: len(self.breweries_with_websites[state]) for state in self.breweries_with_websites}
        return json.dumps(websites_count, indent=4)


states = ["Alaska", "Maine", "New York"]

brewery = Brewery(states)

brewery.fetch_breweries()

websites_json = brewery.websites_to_json()
print("Breweries with Websites :\n", websites_json)

websites_count_json = brewery.websites_count_to_json()
print("Counts of Breweries with Websites :\n", websites_count_json)
