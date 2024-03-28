import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Excel dosyasını okuma
df = pd.read_csv('../../PycharmProjects/Neval/studentscores.csv')

#Ortalama fonksiyonu
def Aritmetik_ortalama(veri):
    toplam= 0
    sayac= 0
    for deger in veri:
        toplam += deger
        sayac += 1
    return toplam / sayac

#Medyan(Ortanca) fonksiyonu
def Medyan(veri):
    sorted_data = sorted(veri)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

#Mod(Tepe Değeri) fonksiyonu
def Mod(veri):
    sayac = {}
    for deger in veri:
        sayac[deger] = sayac.get(deger, 0) + 1
    mod = max(sayac, key=sayac.get)
    return mod

#Ortalama mutlak sapma fonksiyonu
def Mutlak_sapma(veri, medyan):
    sapmalar = []
    for deger in veri:
        sapmalar.append(abs(deger - medyan))
    return Aritmetik_ortalama(sapmalar)

#Varyans fonksiyonu
def Varyans(veri, aritmetik_ortalama):
    karesel_sapmalar = []
    for deger in veri:
        karesel_sapmalar.append((deger - aritmetik_ortalama) ** 2)
    return Aritmetik_ortalama(karesel_sapmalar)

#Standart sapma fonksiyonu
def Standart_sapma(varyans):
    return varyans ** 0.5

#Her sayısal değişken için kutu çizimi
for column in df.columns:
    if df[column].dtype in ['int64', 'float64']:  # Sayısal değişkenleri seç
        plt.figure(figsize=(6,4))
        plt.boxplot(df[column], vert=False)
        plt.title(column + " Boxplot")
        plt.xlabel("Değer")
        plt.show()

        #Aykırı değerleri bulma
        Q1 = np.percentile(df[column], 25)
        Q3 = np.percentile(df[column], 75)
        IQR = Q3 - Q1
        alt_sinir = Q1 - 1.5 * IQR
        ust_sinir = Q3 + 1.5 * IQR
        aykiridegerler = df[(df[column] < alt_sinir) | (df[column] > ust_sinir)][column]
        print("Aykırı Değerler - {}: {}".format(column, list(aykiridegerler)))

        #Merkezi eğilim ve merkezi dağılım ölçümlerini hesaplama
        aritmetik_ortalama = Aritmetik_ortalama(df[column])
        medyan = Medyan(df[column])
        mod = Mod(df[column])
        degisim_araligi = df[column].max() - df[column].min()
        mutlak_sapma = Mutlak_sapma(df[column], medyan)
        varyans = Varyans(df[column], aritmetik_ortalama)
        standart_sapma = Standart_sapma(varyans)
        degisim_katsayisi = standart_sapma / aritmetik_ortalama
        ceyrekler_acikligi = np.percentile(df[column], 75) - np.percentile(df[column], 25)

        #Sonuçları ekrana yazdırma
        print("\nMerkezi Eğilim ve Merkezi Dağılım Ölçümleri - {}".format(column))
        print("Aritmetik Ortalama:", aritmetik_ortalama)
        print("Ortanca (Medyan):", medyan)
        print("Tepe Değer (Mod):", mod)
        print("Değişim Aralığı:", degisim_araligi)
        print("Ortalama Mutlak Sapma:", mutlak_sapma)
        print("Varyans:", varyans)
        print("Standart Sapma:", standart_sapma)
        print("Değişim Katsayısı:", degisim_katsayisi)
        print("Çeyrekler Açıklığı:", ceyrekler_acikligi)
        print("\n")

        #Sonuçları sonuc.txt dosyasına yazma
        with open("../../PycharmProjects/Neval/sonuc.txt", "a") as file:
            file.write("\nMerkezi Egilim ve Merkezi Dagilim Olcumleri - {}\n".format(column))
            file.write("Aritmetik Ortalama:{}\n".format(aritmetik_ortalama))
            file.write("Ortanca(Medyan):{}\n".format(medyan))
            file.write("Tepe Deger(Mod):{}\n".format(mod))
            file.write("DEgisim Araligi:{}\n".format(degisim_araligi))
            file.write("Ortalama Mutlak Sapma:{}\n".format(mutlak_sapma))
            file.write("Varyans:{}\n".format(varyans))
            file.write("Standart Sapma:{}\n".format(standart_sapma))
            file.write("Degisim Katsayisi:{}\n".format(degisim_katsayisi))
            file.write("Ceyrekler Acikligi:{}\n".format(ceyrekler_acikligi))