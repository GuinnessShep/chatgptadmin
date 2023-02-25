import time
import jwt
import requests

# Firebase project configuration
client_id = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"
gcm_sender_id = "568928957521"
project_id = "aichat-4fb19"
api_key = "AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA"

# Function to generate the Firebase token
def generate_token(client_id, gcm_sender_id, project_id, api_key):
    now = int(time.time())
    exp = now + 3600  # Token expires in 1 hour
    payload = {
        "aud": project_id,
        "iss": client_id,
        "iat": now,
        "exp": exp,
        "sub": gcm_sender_id,
        "android": {"packageName": "com.pb.chatgptmac"}
    }
    token = jwt.encode(payload, api_key, algorithm="HS256")
    return token.decode()

# Generate the Firebase token
token = generate_token(client_id, gcm_sender_id, project_id, api_key)

# Send a message using the token
url = "https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot"
headers = {"Content-Type": "application/json"}
data = {"token": token, "prompt": "Your Message"}
response = requests.post(url, headers=headers, json=data)
print(response.text)
