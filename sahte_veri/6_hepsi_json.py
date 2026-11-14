"""6 - Yukaridaki hepsini birlestirip rastgele sahte kayitlari JSON olarak basar."""
import json
import random
import secrets
import string

ISIMLER = ["Ahmet", "Ayse", "Can", "Zeynep", "Emre", "Elif", "Burak", "Selin"]
SOYISIMLER = ["Yilmaz", "Kaya", "Demir", "Sahin", "Yildiz", "Aydin", "Dogan"]
DOMAINLER = ["example.com", "test.org", "ornek.net"]


def kayit():
    ad = random.choice(ISIMLER)
    soyad = random.choice(SOYISIMLER)
    kadi = f"{ad.lower()}.{soyad.lower()}{random.randint(1, 99)}"
    govde = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(24))
    return {
        "ad": ad,
        "soyad": soyad,
        "email": f"{kadi}@{random.choice(DOMAINLER)}",
        "telefon": f"+90 5{random.randint(30,59)} {random.randint(100,999)} {random.randint(1000,9999)}",
        "api_key": f"sk_test_{govde}",
        "token": secrets.token_urlsafe(16),
    }


if __name__ == "__main__":
    veri = [kayit() for _ in range(6)]
    print(json.dumps(veri, indent=2, ensure_ascii=False))
