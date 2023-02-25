import requests

# Define the request headers and body
url = 'https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot'
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Chat Bot/3.2'
}
data = {
    'token': id_token,
    'prompt': 'Your Message'
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Print the response content
print(response.content)
