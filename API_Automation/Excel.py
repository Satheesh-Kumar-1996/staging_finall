import json

import openpyxl
import requests

wb = openpyxl.load_workbook("/home/sathish/Desktop/Hindwai.xlsx")
sheet = wb.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    post_url = row[0]
    raw_payload = row[1]
    try:
        payload = json.loads(raw_payload)
    except json.JSONDecodeError as e:
        print(f" Invalid JSON payload in row: {row}")
        continue
    print(f"Sending POST to: {post_url}")
    print(f" Payload: {payload}")
    try:
        response = requests.post(post_url, json=payload)
        print(f" POST Status: {response.status_code}")
        print(" Response:", response.json())
    except Exception as e:
        print(f" Request failed: {e}")
        continue

        # Optional: Extract values for GET
    param_id = payload.get("journalCode")
    param_type = payload.get("manuscriptID")


    # Construct GET URL
    get_url = f"http://10.0.5.211/NimbleReports-HINDAWI?type=articlemetadata&journal={param_id}&articleid={param_type}&format=json"  # Adjust GET base URL
    print(f" Sending GET to: {get_url}")
    get_response = requests.get(get_url)

    print(f" GET Status: {get_response.status_code}")
    print(" GET Response:", get_response.json())
    
