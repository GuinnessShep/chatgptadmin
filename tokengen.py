import time
import jwt

# Replace with your own values
CLIENT_ID = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"
GCM_SENDER_ID = "568928957521"
PROJECT_ID = "aichat-4fb19"
BUNDLE_ID = "com.pb.chatgptmac"
API_KEY = "AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA"

payload = {
    "aud": API_KEY,
    "iss": GCM_SENDER_ID,
    "iat": int(time.time()),
    "exp": int(time.time()) + 60 * 60, # Token is valid for 1 hour
    "sub": BUNDLE_ID,
    "gcm.n.acl": {
        PROJECT_ID: {
            "admin": True
        }
    }
}
# Encode the payload and sign with the server key
token = jwt.encode(payload, algorithm="HS256")
# Convert token to string
token_str = token.decode("utf-8")

# Format the POST data
post_data = {
    "token": token_str,
    "prompt": "Your message"
}

# Send POST request to chatbot endpoint
import requests
response = requests.post("https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot", json=post_data)

# Print the response
print(response.text)
