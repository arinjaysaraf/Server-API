import time 
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token:str):  # returns generated tokens(JWTs)
    return {
        "access token":token
    }

def signJWT(userID:str):
    payload = {         
        "userID" : userID,
        "expiry" : time.time() + 600 
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM) # encode everything inside his method
    return token_response(token)


def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}