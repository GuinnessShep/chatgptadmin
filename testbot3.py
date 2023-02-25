import requests

# Define the endpoint URL
url = "https://us-central1-chatbot-e10c8.cloudfunctions.net/chatbot"

# Define the POST data as a dictionary
data = {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cC161kpXVCJ9.eyJpc3MiOiI1Njg5Mjg5NTc1MjEtbTUзb21s0GxmbmYycWxxNmpucTRibHAxbGpjcTRiYzguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIlNjg5Mjg5NTc1MjEtbTU3b21s0GxmbmYycWxxNmpucTRibHAxbGpjcTRiYzguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiJodHRwczovL21kZW50aXR5dG9vbGtpdC5nb29nbGVhcG1zLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdH10b29sa210LnYxLklkZW50aXR5VG9vbGtpdCIsIm1hdCI6MTY3NzI5MzU4NywiZXhwIjoxNjc3Mjk3MTg3LCJ1aWQiOiIxIiwiY2xhaWlzIjp7ImtpZCI6InAyNTYiLCJhbGci0iJSUzI1NiIsInR5cCI6IkpXVCJ9fQ.sXy252MRJ9TOXLZpqH_sEx59yr6Dm8UyM72DBuu9ycY",
    "prompt": ""
}

# Start an interactive chat session
while True:
    # Get user input
    prompt = input("You: ")

    # Set the prompt value in the POST data
    data["prompt"] = prompt

    # Send a POST request to the chatbot endpoint with the POST data
    response = requests.post(url, json=data)

    try:
        # Parse the response JSON and print the chatbot's response
        response_data = response.json()
        print("Chatbot:", response_data["response"])
    except ValueError:
        # Handle any JSON decoding errors
        print("Error parsing JSON response:", response.text)
