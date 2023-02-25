import firebase_admin
from firebase_admin import credentials, auth

# Load the Firebase configuration and offline token gen data from the JSON file
import json
with open('firebase_data.json') as f:
    data = json.load(f)

# Initialize Firebase Admin SDK with the credentials and configuration
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, data['firebase_config'])

# Generate an ID token using the offline token gen data
custom_token = auth.create_custom_token(uid='user_id', developer_claims=data['offline_token_gen_data'])

# Exchange the custom token for an ID token
id_token = auth.exchange_custom_token(custom_token)

# Print the generated ID token
print(id_token)
