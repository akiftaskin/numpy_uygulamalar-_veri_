import numpy as np
import matplotlib.pyplot as plt

#BÖLÜM 1: Şirket Maaş Analizi

#---GÖREV 1---

# 500 çalışanın maaşlarını rastgele belirle (3000 TL - 15000 TL)
np.random.seed(42)  # Sonuçların tekrar üretilebilir olması için
maaslar = np.random.randint(3000, 15001, 500)

# Temel istatistikleri hesapla
ortalama_maas = np.mean(maaslar)
maksimum_maas = np.max(maaslar)
minimum_maas = np.min(maaslar)

print("Şirket Maaş Analizi")
print(f"Ortalama Maaş: {ortalama_maas:.2f} TL")
print(f"En Yüksek Maaş: {maksimum_maas} TL")
print(f"En Düşük Maaş: {minimum_maas} TL")

# Maaş dağılımını görselleştir
plt.figure(figsize=(10,5))
plt.hist(maaslar, bins=15, edgecolor="black", alpha=0.7)
plt.xlabel("Maaş Aralıkları (TL)")
plt.ylabel("Çalışan Sayısı")
plt.title("Şirket Maaş Dağılımı")
plt.grid(True)
plt.show()

#---GÖREV 2---

# 500 çalışanı rastgele 3 departmana ata
departmanlar = np.random.randint(1, 4, 500)  # 1: Mühendislik, 2: Muhasebe, 3: Pazarlama

# Her departmandaki maaşları ayır
muhendislik_maas = maaslar[departmanlar == 1]
muhasebe_maas = maaslar[departmanlar == 2]
pazarlama_maas = maaslar[departmanlar == 3]

# Her departmanın ortalama maaşını hesapla
print("\n Departman Bazında Maaş Analizi")
print(f"Mühendislik Ortalama Maaşı: {np.mean(muhendislik_maas):.2f} TL")
print(f"Muhasebe Ortalama Maaşı: {np.mean(muhasebe_maas):.2f} TL")
print(f"Pazarlama Ortalama Maaşı: {np.mean(pazarlama_maas):.2f} TL")

#BÖLÜM 2

#---GÖREV 3---

# 365 günlük sıcaklık verisi oluştur (-10°C ile 40°C arasında)
sicakliklar = np.random.randint(-10, 41, 365)

# Temel istatistikler
ortalama_sicaklik = np.mean(sicakliklar)
maksimum_sicaklik = np.max(sicakliklar)
minimum_sicaklik = np.min(sicakliklar)

print("\n Hava Durumu Analizi")
print(f"Ortalama Sıcaklık: {ortalama_sicaklik:.2f}°C")
print(f"En Sıcak Gün: {maksimum_sicaklik}°C")
print(f"En Soğuk Gün: {minimum_sicaklik}°C")

# Sıcaklık değişimlerini görselleştir
plt.figure(figsize=(12, 5))
plt.plot(sicakliklar, color='red', linewidth=1)
plt.xlabel("Gün")
plt.ylabel("Sıcaklık (°C)")
plt.title("Yıllık Sıcaklık Değişimi")
plt.grid(True)
plt.show()

#BÖLÜM 3 

#---GÖREV 4---

urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
gunluk_satislar = np.random.randint(10, 101, (5, 30))  # 5 ürün, 30 gün

toplam_satislar = np.sum(gunluk_satislar, axis=1)
ortalama_satislar = np.mean(gunluk_satislar, axis=1)

print("\n Ürün Satış Analizi")
for i, urun in enumerate(urunler):
    print(f"{urun} - Toplam Satış: {toplam_satislar[i]}, Ortalama Günlük Satış: {ortalama_satislar[i]:.2f}")

# Çubuk grafiği çiz
plt.figure(figsize=(7, 4))
plt.bar(urunler, toplam_satislar, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel(" Ürünler")
plt.ylabel("Toplam Satış")
plt.title("Ürün Bazında Satış Analizi")
plt.grid(axis="y")
plt.show()

