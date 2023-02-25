import jwt
import time

client_id = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"
reversed_client_id = "com.googleusercontent.apps.568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8"
api_key = "AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA"
gcm_sender_id = "568928957521"
bundle_id = "com.pb.chatgptmac"
project_id = "aichat-4fb19"
storage_bucket = "aichat-4fb19.appspot.com"
google_app_id = "1:568928957521:ios:14ccbf85a464137f73f470"
now = int(time.time())

data = {
    "aud": api_key,
    "iat": now,
    "exp": now + 3600,
    "iss": "https://securetoken.google.com/" + project_id,
    "sub": "test@example.com",
    "uid": "exampleuid",
    "claims": {
        "client_id": client_id,
        "client_type": 3,
        "android_package_name": bundle_id,
        "gcm_sender_id": gcm_sender_id,
        "ios_bundle_id": bundle_id,
        "project_id": project_id,
        "storage_bucket": storage_bucket,
        "google_app_id": google_app_id,
        "service_account": f"{project_id}@appspot.gserviceaccount.com"
    }
}

# Create the Firebase token
firebase_token = jwt.encode(data, api_key, algorithm="HS256")

print(firebase_token)
