OPENAI CHATGPT + FIREBASE LEAK


Use any Python, GO or whatever you're familiar with Firebase to generate a token based on the info below.
#
#
Firebase Offline Token Gen data:

CLIENT_ID: 568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com

REVERSED_CLIENT_ID: com.googleusercontent.apps.568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8

API_KEY: AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA

GCM_SENDER_ID: 568928957521

BUNDLE_ID: com.pb.chatgptmac

PROJECT_ID: aichat-4fb19

STORAGE_BUCKET: aichat-4fb19.appspot.com -> :))))

GOOGLE_APP_ID: 1:568928957521:ios:14ccbf85a464137f73f470
#
#
#
Then POST to the chatbot, us-central1-chatbot-e10c8.cloudfunctions.net/chatbot using the JSON POST Data Format bellow as an example:
#
#
POST /chatbot HTTP/2

Host: us-central1-chatbot-e10c8.cloudfunctions.net

Accept: */*

Content-Type: application/json

Accept-Encoding: gzip, deflate

User-Agent: Chat%20Bot/3.2 

Content-Length: 51

Accept-Language: en-US,en;q=0.9

{"token":"XXXXXXXXXXXXXXXX","prompt":"Your Message "}

