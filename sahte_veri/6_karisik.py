"""6 - Bir arada birkac farkli gizli deger (sealbox denemesi icin)."""
import os

AD_SOYAD = "Zeynep Kaya"
EMAIL = "__SECURE_EMAIL_4976bd5ab5815dbe39ec69cea08c2554__"
API_KEY = os.environ["API_KEY_2"]
TELEFON = "__SECURE_PHONE_034f132b7ed2a6967755befc3047aa36__"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

print("Ad Soyad :", AD_SOYAD)
print("Email    :", EMAIL)
print("API_KEY  :", API_KEY)
print("Telefon  :", TELEFON)
print("GitHub   :", GITHUB_TOKEN)
