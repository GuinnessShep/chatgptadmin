import jwt

client_id = '568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com'
reversed_client_id = 'com.googleusercontent.apps.568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8'
api_key = 'AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA'
gcm_sender_id = '568928957521'
bundle_id = 'com.pb.chatgptmac'
project_id = 'aichat-4fb19'
storage_bucket = 'aichat-4fb19.appspot.com'
google_app_id = '1:568928957521:ios:14ccbf85a464137f73f470'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

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
    }
}

token = jwt.encode(payload, api_key, algorithm='HS256', headers=header)

print(token.decode())
