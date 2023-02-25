import firebase_admin
from firebase_admin import credentials, auth
import requests

# Initialize the Firebase SDK with the provided configuration data
cred = credentials.Certificate('/path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'apiKey': 'AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA',
    'authDomain': 'aichat-4fb19.firebaseapp.com',
    'databaseURL': 'https://aichat-4fb19.firebaseio.com',
    'projectId': 'aichat-4fb19',
    'storageBucket': 'aichat-4fb19.appspot.com',
    'messagingSenderId': '568928957521',
    'appId': '1:568928957521:ios:14ccbf85a464137f73f470',
    'measurementId': 'G-ABCDEFG123'
})

# Authenticate the user anonymously
user = auth.anonymous_user()

# Retrieve an authentication token for the user
token = auth.create_custom_token(user.uid)

# Send a POST request to the chatbot API with the token and prompt data
url = 'https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot'
data = {'token': token.decode('utf-8'), 'prompt': 'Your Message'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=data, headers=headers)

print(response.text)
