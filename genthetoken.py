import requests
import json
import jwt
import time

# Fill in with Firebase Offline Token Gen data
CLIENT_ID = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"
PROJECT_ID = "aichat-4fb19"

# Fill in with the endpoint URL and request parameters
ENDPOINT_URL = "https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot"
PROMPT = "Your Message "

# Generate the Firebase token
now = int(time.time())
exp = now + (3600 * 24)  # Token expires in 24 hours
payload = {
    "iss": CLIENT_ID,
    "sub": CLIENT_ID,
    "aud": "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
    "iat": now,
    "exp": exp,
    "uid": "123",
    "claims": {
        "project_id": PROJECT_ID,
    },
}
token = jwt.encode(payload, None, algorithm="HS256")

# Send the POST request
headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "User-Agent": "Chat%20Bot/3.2",
}
data = {
    "token": token.decode("utf-8"),
    "prompt": PROMPT,
}
response = requests.post(ENDPOINT_URL, headers=headers, data=json.dumps(data))

print(response.text)
