import requests
import json

# set up the API endpoint and JSON data
url = 'https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot'
headers = {'Content-Type': 'application/json'}
data = {"token": "eyJhbGciOiJIUzI1NiIsInR5cC161kpXVCJ9.eyJhdWQiOiJBSXphU31DbTk5ZmswdkRRbGdYTWdUTTlmemxx
WG1RV0hWZE9NS0EiLCJpYXQiOjE2Nzcy0Tc3MTIsImV4CCI6MTY3NzMwMTMxMiwiaXNzIjoiaHR0cHM6Ly9zZ
WN1cmV0b2tlbi5nb29nbGUuY29tL2FpY2hhdC00ZmIxOSIsInNlYiI6InRlc3RAZXhhbXBsZS5jb20iLCJ1aW
QiOiJleGFtcGxldWlkIiwiY2xhaW1zIjp7ImNsaWVudF9pZCI6IjU2ODkYODk1NzUyMS1tNTdvaWw4bGZuZjJ
xbHE2am5xNGJscDFsamNxNGJjOC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImNsaWVudF90eXBlIjoz
LCJhbmRyb21kX3BhY2thZ2VfbmFtZSI6ImNvbS5wYi5jaGF0Z3B0bWFjIiwiZ2NtX3NlbmRlc19pZCI6IjU20
DkyODk1NzUyMSIsImlvc19idW5kbGVfaWQiOiJjb20ucGIuY2hhdGdwdG1hYyIsInByb2plY3RfaWQiOiJhaW
NoYXQtNGZiMTkiLCJzdG9yYWdlX2J1Y2tldCI6ImFpY2hhdC00ZmIxOS5hcHBzcG90LmNvbSIsImdvb2dsZV9
hcHBfaWQiOiIxOjU20DkyODk1NzUyMTppb3M6MTRjY2JmODVhNDY0MTM3ZjczZjQ3MCIsInNlcnZpY2VfYWNj
b3VudCI6ImFpY2hhdC00ZmIxOUBhcHBzcG90LmdzZXJ2aWNlYWNjb3VudC5jb20ifX0.pfPkoJJOesofJA126
5zpXKkG9Yo4neGYzzSb6y1VNCY", "prompt": "Your Message "}

# loop until the user decides to exit
while True:
    # prompt the user for input
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # add the user's input to the JSON data
    data['prompt'] = user_input

    # send a POST request to the API endpoint
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # print the chat bot's response
    response_json = response.json()
    if response_json.get('response'):
        print("Chat Bot:", response_json['response'])
    else:
        print("Error: Invalid API response")
