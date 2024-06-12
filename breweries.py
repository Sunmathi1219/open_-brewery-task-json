""""
Visit the url-https://www.openbrewerydb.org/documentation/ write a python script which will do a the following
1.) List the names of all breweries present in the states of Alaska,Maine and New Work
"""

import requests
import json

class Brewery:
    def __init__(self,states):
        self.states=states
        self.url="https://api.openbrewerydb.org/v1/breweries?"
        self.breweries={}

    def fetch_breweries(self):
        for state in self.states:
            response=requests.get(f"{self.url}by_state={state}&per_page=3")
            if response.status_code==200:
                breweries_data=response.json()
                self.breweries[state]=[brewery['name'] for brewery in breweries_data]

            else:
                print(f"Failed to fetch breweries {state}")

    def to_json(self):
        return json.dumps(self.breweries,indent=4)                

states=["Alaska","Maine","New York"]

brewery=Brewery(states)
brewery.fetch_breweries()
brewery_json=brewery.to_json()

print(brewery_json)
