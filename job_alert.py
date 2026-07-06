import os
import requests

# Target Anglo-Eastern API
URL = "https://apply.workable.com/api/v3/accounts/angloeastern/jobs"

# Bulletproof payload structure to avoid structural 400 bad request rejections
PAYLOAD = {
    "query": ""
}

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print("Checking for new jobs at Anglo-Eastern...")

try:
    # Send a POST request to the updated Workable backend
    response = requests.post(URL, json=PAYLOAD, headers=HEADERS)
    response.raise_for_status()
    
    # Process the returned data
    data = response.json()
    jobs = data.get("results", [])
    
    if not jobs:
        print("No active job postings found right now.")
    else:
        print(f"Found {len(jobs)} active jobs:")
        for job in jobs:
            title = job.get("title")
            shortcode = job.get("shortcode")
            job_url = f"https://apply.workable.com/angloeastern/j/{shortcode}/"
            
            print(f"- {title}")
            print(f"  Link: {job_url}")
            
except Exception as e:
    print(f"An error occurred while running the script: {e}")
    raise e
