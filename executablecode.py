import os
import requests

def provision_user(email, department):
    """Provisions a new user in the enterprise directory and assigns MDM policies."""
    
    api_token = os.environ.get("DIRECTORY_API_KEY")
    if not api_token:
        raise ValueError("Critical Security Error: API token not found.")
    
    # 1. The Destination (URL)
    api_endpoint = "https://api.your-enterprise-software.com/v1/users"
    
    # 2. The ID Badge (Headers)
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    # 3. The Data (Payload)
    user_data = {
        "email_address": email,
        "department": department,
        "role": "standard_user"
    }
    
    # 4. Making the Request
    print(f"Attempting to provision {email}...")
    response = requests.post(api_endpoint, headers=headers, json=user_data)
    
    # 5. Verifying the Result
    if response.status_code == 201:
        print(f"Success! {email} was created securely.")
    else:
        print(f"Failed to create user. Error Code: {response.status_code}")
        print(f"System Response: {response.text}")

if __name__ == "__main__":
    provision_user("new.hire@example.com", "Engineering")
