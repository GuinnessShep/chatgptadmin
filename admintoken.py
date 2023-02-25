import requests
import json

# Firebase configuration
client_id = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"
reversed_client_id = "com.googleusercontent.apps.568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8"
api_key = "AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA"
gcm_sender_id = "568928957521"
bundle_id = "com.pb.chatgptmac"
project_id = "aichat-4fb19"
storage_bucket = "aichat-4fb19.appspot.com"
google_app_id = "1:568928957521:ios:14ccbf85a464137f73f470"

# Endpoint to generate a Firebase token
url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={api_key}"

# Payload for the request
payload = {
    "token": None,
    "returnSecureToken": True
}

# Custom token for unrestricted access to the chat bot
custom_token = {
    "iss": f"https://securetoken.google.com/{project_id}",
    "aud": project_id,
    "iat": 0,
    "exp": 9999999999,
    "uid": "unrestricted"
}

# Generate the Firebase token using the custom token
response = requests.post(url, json={"token": custom_token}).json()

# Check if the response contains an error message
if "error" in response:
    print(f"Error: {response['error']['message']}")
else:
    # Extract the Firebase token from the response
    firebase_token = response.get("idToken")

    # Check if the Firebase token is present
    if firebase_token:
        print(firebase_token)
    else:
        print("Firebase token not found in response.")
