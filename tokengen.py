import time
import jwt

def generate_token(client_id, gcm_sender_id, project_id, api_key):
    now = int(time.time())
    exp_time = now + 3600  # Token expires in one hour
    payload = {
        "aud": project_id,
        "iat": now,
        "exp": exp_time,
        "sub": client_id,
        "gmc_id": gcm_sender_id,
        "iss": api_key,
        "android": {
            "package_name": "com.pb.chatgptmac"
        }
    }
    token = jwt.encode(payload, None, algorithm="HS256")
    return token.encode()

client_id = "568928957521-m57oil8lfnf2qlq6jnq4blp1ljcq4bc8.apps.googleusercontent.com"
gcm_sender_id = "568928957521"
project_id = "aichat-4fb19"
api_key = "AIzaSyCm99fk0vDQlgXMgTM9fzlqXiQWHpdOMKA"

token = generate_token(client_id, gcm_sender_id, project_id, api_key)
print(token.decode())
