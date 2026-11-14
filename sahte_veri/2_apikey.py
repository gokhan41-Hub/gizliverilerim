"""2 - Sabit API anahtari ve token (sealbox denemesi icin)."""
import os

API_KEY = os.environ["API_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

print("API_KEY       :", API_KEY)
print("SECRET_KEY    :", SECRET_KEY)
print("BEARER_TOKEN  :", BEARER_TOKEN)
