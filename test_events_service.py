import requests

events_store_url = "http://127.0.0.1:8020"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
user_id = "1127794"

resp = requests.post(events_store_url + "/get", 
                     headers=headers, 
                     params={"user_id": user_id, "k": 3})
print(resp.json()) 