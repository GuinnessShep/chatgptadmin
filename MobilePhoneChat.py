import webbrowser
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

# Construct the URL for the chat interface
base_url = 'https://us-central1-chatbot-e10c8.cloudfunctions.net/ui'
url = f'{base_url}?token={token.decode("utf-8")}'

# Open the chat interface in the default browser
webbrowser.open(url)

# Prompt the user for input and send it to the chatbot API
while True:
    message = input('You: ')
    data = {'token': token.decode('utf-8'), 'prompt': message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(base_url, json=data, headers=headers)
    print('AI: ' + response.text)
