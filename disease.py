import requests
import json
import requests

# Replace with your Database REST API URL
Database_REST_API = 'https://query.dropbase.io/kkBkXojaa8xcgbrN4dsDUN'

# Table you wish to query with postgREST
Table_to_Query = 'countries'

# Acess key generated. Make sure you set the correct expiration time, in hour or days
Access_Key = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoia2tCa1hvamFhOHhjZ2JyTjRkc0RVTiIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IkhDWEdiWGZoOFBFRk1oMWc5djJzQTlkTUs2cE1qTnJJWUVJNFVDSU00S2tjRndReDd0eGRlVkdOTGhNQldseE8iLCJpYXQiOjE2MTA4NDgzNDIsImV4cCI6MTYxMDk0OTE0MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJoZHVEckxDN3VoWDhRakNybk5CQ0JrIn0.ZeO3qEL60YIQWH6dHSPWleBJoBw2IZLPMxl1-HE0XVU'




def get_worse_disease(country: str):
    # getting a list of all the countries
    countries_url = 'https://query.dropbase.io/kkBkXojaa8xcgbrN4dsDUN/countries?select=country'
    countries_response = requests.get(countries_url, headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoia2tCa1hvamFhOHhjZ2JyTjRkc0RVTiIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IkhDWEdiWGZoOFBFRk1oMWc5djJzQTlkTUs2cE1qTnJJWUVJNFVDSU00S2tjRndReDd0eGRlVkdOTGhNQldseE8iLCJpYXQiOjE2MTA4NDgzNDIsImV4cCI6MTYxMDk0OTE0MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJoZHVEckxDN3VoWDhRakNybk5CQ0JrIn0.ZeO3qEL60YIQWH6dHSPWleBJoBw2IZLPMxl1-HE0XVU"})
    
    countries_response_json = countries_response.json()
    print(type(countries_response_json))
    
    countries_list = [c["country"] for c in countries_response_json]

    if country in not countries_list:
        return -1

    # getting the endpoint
    wd_url = 'https://query.dropbase.io/kkBkXojaa8xcgbrN4dsDUN/countries?country=eq.' + country
    # making the request
<<<<<<< Updated upstream
    x = requests.get(url, headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoia2tCa1hvamFhOHhjZ2JyTjRkc0RVTiIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IkhDWEdiWGZoOFBFRk1oMWc5djJzQTlkTUs2cE1qTnJJWUVJNFVDSU00S2tjRndReDd0eGRlVkdOTGhNQldseE8iLCJpYXQiOjE2MTA4NDgzNDIsImV4cCI6MTYxMDk0OTE0MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJoZHVEckxDN3VoWDhRakNybk5CQ0JrIn0.ZeO3qEL60YIQWH6dHSPWleBJoBw2IZLPMxl1-HE0XVU"})
    response_json = x.json()             # JSON format of query
    country = response_json[0]           # getting the first entry
=======
    wd_response = requests.get(wd_url, headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoia2tCa1hvamFhOHhjZ2JyTjRkc0RVTiIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IkhDWEdiWGZoOFBFRk1oMWc5djJzQTlkTUs2cE1qTnJJWUVJNFVDSU00S2tjRndReDd0eGRlVkdOTGhNQldseE8iLCJpYXQiOjE2MTA4NDgzNDIsImV4cCI6MTYxMDk0OTE0MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJoZHVEckxDN3VoWDhRakNybk5CQ0JrIn0.ZeO3qEL60YIQWH6dHSPWleBJoBw2IZLPMxl1-HE0XVU"})
    wd_response_json = wd_response.json()                           # JSON format of query
    # print("\n" + json.dumps(wd_response_json, indent=4) + "\n")
    country = wd_response_json[0]                                   # getting the first entry
>>>>>>> Stashed changes
    return country['largest_disease']


print(get_worse_disease('Afghanistan'))




