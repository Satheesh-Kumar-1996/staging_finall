import requests
import openpyxl
import time

# ---- Configuration ----
EXCEL_FILE = "/home/sathish/Desktop/Hindwai.xlsx"
POST_URL = "https://hindawi-api-uat.tnq.co.in/signals/newManuscript"
GET_URL = "http://10.0.5.211/NimbleReports-{{CUSTOMERAPI}}?type=articlemetadata&journal={{JID}}&articleid={{ARTICLEID}}&format=json"
WAIT_TIME = 3 # seconds between POST and GET

# Optional: headers if needed
HEADERS = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer YOUR_TOKEN"
}

# ---- Function to read Excel and convert to payloads ----
def read_payloads_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    payloads = []

    # Assuming first row is header
    headers = [cell.value for cell in sheet[1]]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        payload = dict(zip(headers, row))
        payloads.append(payload)

    return payloads

# ---- Function to send POST and verify with GET ----
def post_and_verify(payload):
    print(f"\nPosting: {payload}")
    post_resp = requests.post(POST_URL, json=payload, headers=HEADERS)
    print("POST Status:", post_resp.status_code)

    # Wait for data to propagate
    time.sleep(WAIT_TIME)

    # GET to verify (example: search by email)
    get_params = {"journal": payload.get("JID")}
    get_resp = requests.get(GET_URL, params=get_params, headers=HEADERS)

    if get_resp.status_code == 200:
        try:
            result = get_resp.json()
            if result and result[0].get("JID") == payload["JID"]:
                print("✅ Verified successfully.")
            else:
                print("❌ Verification failed: Data not found.")
        except Exception as e:
            print("❌ GET response parsing failed:", e)
    else:
        print("❌ GET failed with status:", get_resp.status_code)

# ---- Main Execution ----
if __name__ == "__main__":
    all_payloads = read_payloads_from_excel(EXCEL_FILE)
    for payload in all_payloads:
        post_and_verify(payload)
