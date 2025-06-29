import requests

# Step 1: Define your JSON payload for POST
post_payload = {"signalType":"newManuscript","journalCode":"AESS","manuscriptID":1111,"fileName":"CRIHEM_5125740_New.zip","datetimeNewManuscript":"2025-06-11 11:20:07","round":0}

# Step 2: Send POST request
post_url = "https://hindawi-api-uat.tnq.co.in/signals/newManuscript"
post_response = requests.post(post_url, json=post_payload)

print(f"POST Status: {post_response.status_code}")
print("POST Response:", post_response.json())

# Step 3: Extract parameters (from payload or POST response)
param_id = post_payload["journalCode"]
param_type = post_payload["manuscriptID"]



# Step 4: Construct GET URL with extracted params
GET_URL = f"http://10.0.5.211/NimbleReports-HINDAWI?type=articlemetadata&journal={param_id}&articleid={param_type}&format=json"
# Step 5: Send GET request
response = requests.get(GET_URL)
#print(response.json())

if response.status_code == 200:
    data = response.json()

    JID = data.get("jid")
    AID = data.get('articleid')
    status = data.get("status")
    print(f"{data}")
    print(JID)

else:
    print("Request failed with status:", response.status_code)

