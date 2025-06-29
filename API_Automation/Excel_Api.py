import time
import requests
import json
import openpyxl
import datetime



html_rows = []
html_rows.append("<html><body><h2>API  Results</h2><table border='1'>")
html_rows.append("<tr><th>JID</th><th>AID</th><th>Status</th><th>POST URL</th><th>GET URL</th><th>GET Status</th><th>GET Response</th></tr>")

# --- Load Input Excel ---
input_file = "/home/sathish/PythonProject/API_Automation/Inputdata//Hindwai.xlsx"
wb = openpyxl.load_workbook(input_file)
sheet = wb.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    post_url = row[0]
    raw_payload = row[1]


    if not post_url or not raw_payload:
        continue

    try:
        payload = json.loads(raw_payload)
        print(payload)
    except json.JSONDecodeError as e:

        print(f"Invalid JSON: {e}")
        continue

    # POST request
    try:
        requests.post(post_url, json=payload)
    except Exception as e:
        print(f" POST failed: {e}")
        continue

    # Extract values for GET
    param_id = payload.get("journalCode")
    param_type = payload.get("manuscriptID")
    if not param_id or not param_type:
        continue

    time.sleep(5)
    get_url = f"http://10.0.5.211/NimbleReports-HINDAWI?type=articlemetadata&journal={param_id}&articleid={param_type}&format=json"
    get_response = requests.get(get_url)
    status_code = get_response.status_code
    response_json = get_response.json()
    #to extract the data from get message
    record = response_json.get("data", [])[0]
    JID =record.get("jid")
    AID =record.get("articleid")
    Status =record.get("status")

      # Write to HTML
    html_rows.append(f"<tr><td>{JID}</td><td>{AID}</td><td>{Status}</td><td>{post_url}</td><td>{get_url}</td><td>{status_code}</td><td><pre>{json.dumps(response_json, indent=2)}</pre></td></tr>")

# Finalize HTML
html_rows.append("</table></body></html>")

# --- Save Outputs ---
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_html_path = f"/home/sathish/PythonProject/API_Automation/results/Results_{timestamp}.html"

with open(output_html_path, "w") as f:
    f.write("\n".join(html_rows))

print(f"✅ HTML saved to: {output_html_path}")
