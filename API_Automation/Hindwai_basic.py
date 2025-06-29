import requests

url ="https://hindawi-api-uat.tnq.co.in/signals/newManuscript"
payload = {"signalType":"newManuscript","journalCode":"CRIHEM","manuscriptID":5125740,"fileName":"CRIHEM_5125740_New.zip","datetimeNewManuscript":"2025-06-11 11:20:07","round":0}

headers = {
    "Content-Type": "application/json"}
# Send the POST request
response = requests.post(url, json=payload, headers=headers,auth=())

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())