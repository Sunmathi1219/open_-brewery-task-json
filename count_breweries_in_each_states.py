""""
Visit the url-https://www.openbrewerydb.org/documentation/ write a python script which will do a the following
2.) What is the count of breweries in each of the states 
"""

import requests
import json

class Brewery:
    def __init__(self,states):
        self.states=states
        self.url="https://api.openbrewerydb.org/v1/breweries?"
        self.count_of_breweries={}

    def fetch_breweries(self):
        for state in self.states:
            response=requests.get(f"{self.url}by_state={state}&per_page=3")
            if response.status_code==200:
                breweries_data=response.json()
                brewery_names=[brewery['name'] for brewery in breweries_data]
                self.count_of_breweries[state]=len(brewery_names)

            else:
                print(f"failed to fetch breweries for {state}")
                self.count_of_breweries[state]=0

    def to_json(self):
        return json.dumps(self.count_of_breweries,indent=4)
    
states=["Alaska","Maine","New York"]

brewery=Brewery(states)
brewery.fetch_breweries()
counts=brewery.to_json()
print("Brewery Counts :\n",counts)
