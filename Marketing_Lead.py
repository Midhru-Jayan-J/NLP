import requests
import csv

# Apollo API Key
API_KEY = "WCfcMeC-I38f-VD3tbNn4Q"

# API Endpoint (Free Plan Compatible)
URL = "https://api.apollo.io/v1/mixed_companies/search"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "q_keywords": "digital marketing",
    "q_location": "Coimbatore",
    "page": 1,
    "per_page": 10  # Free plans have limitations, keeping it small
}

response = requests.post(URL, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()

    # Save to CSV
    with open("apollo_clients.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Company Name", "Email", "Phone Number", "Requirement"])

        for company in data.get("companies", []):
            name = company.get("name", "N/A")
            email = company.get("email", "N/A")
            phone = company.get("phone", "N/A")
            requirement = "Needs digital marketing"

            writer.writerow([name, email, phone, requirement])

    print("✅ Apollo.io CSV file created successfully!")

else:
    print(f"❌ API Request Failed: {response.status_code}")
    print("Response:", response.text)


