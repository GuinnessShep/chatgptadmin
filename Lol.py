import requests

import jwt

import time

import json

def generate_token(client_id, gcm_sender_id, project_id, api_key):

    now = int(time.time())

    exp_seconds = 3600  # Token valid for 1 hour

    exp_time = now + exp_seconds

    # Create the token payload

    payload = {

       "aud": api_key,

      "iss": client_id,

    "sub": reversed_client_id,

    "gcm.sender": gcm_sender_id,

    "iat": 0,

    "exp": 0xFFFFFFFF,

    "iss": project_id,

    "auth_time": 0,

    "sub": bundle_id,

    "firebase": {

        "identities": {},

        "sign_in_provider": "custom",

        "storage_bucket": storage_bucket

            "kid": "p256",

            "alg": "RS256",

            "typ": "JWT"

        }

    }

    # Sign the token using the API key

    token = jwt.encode(payload, api_key, algorithm="HS256")

    return token

def send_message(token, message):

    headers = {

        "Content-Type": "application/json",

        "Authorization": f"Bearer {token}"

    }

    # Create the request body

    data = {

        "token": token,

        "prompt": message

    }

    # Send the request

    response = requests.post("https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot", headers=headers, data=json.dumps(data))

    return response.text

if __name__ == "__main__":

    # Fill in your Firebase Offline Token Gen data here

    client_id = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"

    gcm_sender_id = "568928957521"

    project_id = "aichat-4fb19"

    api_key = "AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA"

    # Generate a token

    token = generate_token(client_id, gcm_sender_id, project_id, api_key)

    print(f"Generated token: {token}")

    # Send a message using the token

    message = "Hello, ChatGPT!"

    response = send_message(token, message)

    print(response)
