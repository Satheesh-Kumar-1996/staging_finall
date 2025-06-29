import requests
import time
import json

# Base URLs for integration tool (example placeholders)
POST_URL = "https://hindawi-api-uat.tnq.co.in/signals/newManuscript"
GET_URL = "http://10.0.5.211/NimbleReports-HINDAWI?type=articlemetadata&journal=AESS&articleid=1111&format=json"

# Sample payload for POST
post_payload = {"signalType":"newManuscript","journalCode":"AESS","manuscriptID":1111,"fileName":"CRIHEM_5125740_New.zip","datetimeNewManuscript":"2025-06-11 11:20:07","round":0}

# Send POST request
post_response = requests.post(POST_URL, json=post_payload)
print("POST Status Code:", post_response.status_code)
print("POST Response:", post_response.text)

# Optional: wait for data to sync if tool takes time
time.sleep(5)

# Use GET to verify if the data was inserted
# This assumes GET accepts query parameters like email or user

get_response = requests.get(GET_URL)
print("GET Status Code:", get_response)

# Verify the inserted data
try:
    data = get_response.json()
    print(data)
except Exception as e:
    print("❌ Failed to parse GET response:", e)