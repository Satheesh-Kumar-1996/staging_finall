import requests

GET_URL = "http://10.0.5.211/NimbleReports-HINDAWI?type=articlemetadata&journal=AESS&articleid=1111&format=json"
# Make GET request
response = requests.get(GET_URL)

if response.status_code == 200:
    try:
        data = response.json()
        

        if isinstance(data, list):
            for i, item in enumerate(data):
                print(f"Record {i + 1} => JID: {item.get('jid')}, AID: {item.get('aid')}, Status: {item.get('status')}")
        elif isinstance(data, dict):
            print("JID:", data.get("jid"))
            print("AID:", data.get("aid"))
            print("status:", data.get("status"))
        else:
            print("Unsupported JSON format:", data)

    except Exception as e:
        print("JSON parsing error:", e)
else:
    print("Request failed with status:", response.status_code)
