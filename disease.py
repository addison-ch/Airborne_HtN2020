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
    # getting the endpoint
    url = 'https://query.dropbase.io/kkBkXojaa8xcgbrN4dsDUN/countries?country=eq.' + country
    # making the request
    x = requests.get(url, headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoia2tCa1hvamFhOHhjZ2JyTjRkc0RVTiIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IkhDWEdiWGZoOFBFRk1oMWc5djJzQTlkTUs2cE1qTnJJWUVJNFVDSU00S2tjRndReDd0eGRlVkdOTGhNQldseE8iLCJpYXQiOjE2MTA4NDgzNDIsImV4cCI6MTYxMDk0OTE0MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJoZHVEckxDN3VoWDhRakNybk5CQ0JrIn0.ZeO3qEL60YIQWH6dHSPWleBJoBw2IZLPMxl1-HE0XVU"})
    response_json = x.json()             # JSON format of query
    country = response_json[0]           # getting the first entry
    return country['largest_disease']


print(get_worse_disease('Afghanistan'))




