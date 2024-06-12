""""
Visit the url-https://www.openbrewerydb.org/documentation/ write a python script which will do a the following
3.) Count the number of types of breweries present in individual cities of the state
"""

import requests
import json
from collections import defaultdict

class Brewery:
    def __init__(self,states):
        self.states=states
        self.url="https://api.openbrewerydb.org/v1/breweries?"
        self.city_brewery_types=defaultdict(lambda: defaultdict(int))

    def fetch_brewery(self):
        for state in self.states:
            response=requests.get(f"{self.url}by_state={state}&per_page=3")
            if response.status_code==200:
                breweries_data=response.json()
            
                for brewery in breweries_data:
                    city=brewery['city']   
                    brewery_type=brewery['brewery_type']
                    self.city_brewery_types[city][brewery_type]+=1

            else:
                print(f"failed to fetch breweries for {state}")
    
    def to_json(self):
        return json.dumps(self.city_brewery_types,indent=4)
    

states=["Alaska","Maine","New York"]

brewery=Brewery(states)
brewery.fetch_brewery()
city_brwery_type=brewery.to_json()

print("Number of types of breweries present in individual cites of states \n",city_brwery_type)



