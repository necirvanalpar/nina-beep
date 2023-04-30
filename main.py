import requests
import winsound
import json

# Nina Sunucusu ve bölge numarasi (ARS)
ninaBaseUrl = "https://warnung.bund.de/api31"
arsNo="150030000000"

# Belirtilen tehlike seviyesinde alarm calisir
tehlike_seviyesi = "Immediate"

# Json data dosya adi
filename = "tehlike_durumlari.json"

# Uyarı ID'lerinin bulunduğu dosyayı aç veya oluştur
try:
    with open(filename, "r") as f:
        gecmis_uyarilar = json.load(f)
except FileNotFoundError:
    gecmis_uyarilar = []

# ARS numarasiyla toplanan bölgedeki bilgiler
response_Ars = requests.get(ninaBaseUrl+"/dashboard/"+arsNo+".json")

# Eger basarili bir sekilde response aldiysak devam ediyoruz
if response_Ars.status_code == 200:
    # Uyarilarin ayrintilarini ayiklama
    uyarilar = response_Ars.json()
    for uyari in uyarilar:
        id = uyari["payload"]["id"]
        uyariDetaylari = requests.get(ninaBaseUrl+"/warnings/"+id+".json").json()
        # Uyarı tehlikeli olarak sınıflandırılırsa, bir alarm bip sesi calar ve döngü sona erer
        if uyariDetaylari["info"][0]["urgency"] == tehlike_seviyesi and id not in gecmis_uyarilar:
            for i in range(10):
                winsound.Beep(1000, 200) # winsound.Beep(1000, 1000), winsound.Beep(1000, 200)
            gecmis_uyarilar.append(id)
else:
    print("Hata response 200 vermedi")

# Dosyayı güncelle
with open(filename, "w") as f:
    json.dump(gecmis_uyarilar, f)