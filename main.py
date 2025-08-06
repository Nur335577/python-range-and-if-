#if (ŞART VAR) - elif (ŞART VAR) - else (ŞART YOK)
"""
x = int(input("sayı girirniz?"))
if(x>0):
    print("sayı pozitif")
elif (x<0):
    print("sayı negatif")
else : # elif(x==0):
    print("sayı sıfır.")
# sürekli if ile de devam eden projeler olabilir.
"""
#OPERATÖRLER -->
"""
       ==       eşittir
       <
       >
       >=
       <=
       !=       eşit değil
"""


#örnek 1    --- En Büyük Sayıyı Bulma (2 seçenek)
"""
sayi1 = int(input("1. sayıyı giriniz :"))
sayi2 = int(input("2. sayıyı giriniz :"))

if (sayi1>sayi2):
    print("En büyük sayı :",sayi1)
elif(sayi2>sayi1):
    print("En büyük sayı :",sayi2)
else :
    print("sayılar eşittir")
"""
#örnek 2  --- Basit Hesap Makinası
"""
sayi1 = float(input("1. sayıyı giriniz :"))
sayi2 = float(input("2. sayıyı giriniz :"))
secim = input ("işlem seçiniz :")

if (secim == "+"):
    print(f"{sayi1+sayi2:.2f}")
elif (secim == "-"):
    print(f"{sayi1 - sayi2 :.2f}")
elif(secim == "/"):
    print(f"{sayi1/sayi2 :.2f}")
elif (secim == "*"):
    print("{sayi1*sayi2 :.2f}")
#print ("işlem sonucu : {0:.2f}".format(sonuc))  printleri tekrar yazdrmadan her birine sonuc atayıp (sonuc=sayi1+sayi2) en son bu şekide 1 printle atama yapabiliriz...
# üste sonuc=0 yazarsam print(sonuc) ram bellekte sadece 1 tane yer tutar. onun dışında sürekle tekrar ettiği için arka plada defalarca döner.
"""
#örnek 3

# örnek 3 birleştirilmiş yöntem  --- En Büyük Sayıyı Bulma (3 seçenek)
"""
sayi1 = int(input("1. sayıyı giriniz :"))
sayi2 = int(input("2. sayıyı giriniz :"))
sayi3 = int(input("3. sayıyı giriniz :"))

if (sayi1>sayi2 and sayi1>sayi3):
    print("En Büyük Sayı :", sayi1)
if (sayi2>sayi1 and sayi2>sayi3):
    print("En Büyük Sayı :", sayi2)
if (sayi3>sayi1 and sayi3>sayi2):
    print("En Büyük Sayı :", sayi3)
"""
#örmek 3 ayrılmış yöntem  --- En Büyük Sayıyı Bulma (3 seçenek)
"""
sayi1 = int(input("1. sayıyı giriniz :"))
sayi2 = int(input("2. sayıyı giriniz :"))
sayi3 = int(input("3. sayıyı giriniz :"))

if (sayi1>sayi2):
    if(sayi1>sayi3):
        print("En Büyük Sayı :", sayi1)

if (sayi2>sayi1):
    if(sayi2>sayi3):
        print("En Büyük Sayı :", sayi2)

if (sayi3>sayi2):
    if(sayi3>sayi1):
        print("En Büyük Sayı :", sayi3)
"""
#örnek 4 --- Bom Oyunu
"""
sayi = int(input("Bir Sayı Giriniz:"))
if (sayi % 5 == 0) :
    print("BOM")
else :
    print(sayi)
"""
#KARMAŞIK SAYILAR
"""
komplexSayi1 = 7+8j
komplexSayi2 = 6+5j
komplexToplam = komplexSayi1 + komplexSayi2
print("toplam :",komplexToplam)
"""
#
"""
a = 3
b = 4
if (a==b):              #parantezsiz de yazılabilir ama python dışındaki dillerde hata verir.
    print("Eşittir")
elif a!=b:
    print("eşit değil") # print bir fonksiyondur --> satırın sonu iki nokta ile bitmiyor ve parantez ile kapanıyorsa fonksiyondur.
"""
#DÖNGÜLER
"""
for i in range (5):          # range bir fonksiyon türüdür. sondaki iki nokta for'a ait
    print("merhaba dünya")


for i in range (5):        #for döngüsünde tek parametreli yöntemde sıra numarası 0 dan başlar ve bitiş değeri -1 alır
    print(i,"merhaba dünya")
    print(i+1, "merhaba dünya")
"""
#Range Notları
"""
for i in range (bitişDeğeri):                                        #tek parametreli yöntem
for i in range (başlangıçDeğeri,bitişDeğeri)                         #bitişdeğeri + 1 
for i in range (başlangıçDeğeri,bitişDeğeri,adım/artış miktarı değeri)
"""
#örnek 1
"""
mesaj = input("Mesajı Giriniz")
adet = int(input("kaç adet gönderilsin?"))
for i in range(1,adet+1):
    print(i,mesaj)
"""
#örnek2
"""
basla = int(input("Başlangıç Değerini Girin :"))
son = int(input("Bitiş Değerini Girin"))

for i in range (basla,son+1) :
    print(i)
"""
#örnek 3
"""
basla = int(input("Başlangıç Değerini Girin :"))
son = int(input("Bitiş Değerini Girin"))
toplam = 0
for i in range (basla,son+1) :
    print(i)
    toplam+=i
print("sayıların Toplamı :",toplam)
"""
#örnek 4
"""
basla = int(input("Başlangıç Değerini Girin :"))
son = int(input("Bitiş Değerini Girin"))
artıs = int(input("Artış miktarını giriniz :"))
toplam = 0
for i in range (basla,son+1,artıs) :
    print(i)
    toplam+=i
print("sayıların toplamı :",toplam)
"""
#örnek 5
"""
basla = int(input("Başlangıç Değerini Girin :"))
son = int(input("Bitiş Değerini Girin"))
toplam =0
for i in range (basla,son+1) :
    if (i % 2 == 0) :
        print(i)
        toplam+=i
print("sayıların toplamı",toplam)
"""
#örnek 6
"""
basla = int(input("Başlangıç Değerini Girin :"))
son = int(input("Bitiş Değerini Girin"))

for i in range (basla,son+1) :
    if (i%5 == 0):
        print("BOM")
    else:
        print(i)
"""
#örnek 7
"""
basla = int(input("Başlangıç Değerini Girin :"))
son = int(input("Bitiş Değerini Girin"))

for i in range (basla,son+1) :

    if (i%2==0 and i%9==0):
        print("OBEB")
    elif (i%9==0):
        print("dokuzun katı")
    elif (i%2==0):
        print("ikinin katı")
    else :
        print(i)
"""
#örnek 8
"""
for i in range (0,19+1):
    if (i%2==0):
        continue
    else:
        print(i)
"""
#örnek 9
"""
sayi =int(input("Bir Sayı Giriniz:"))
carpım = 1
for i in range (1,sayi+1):
    carpım*=i
print(sayi,"faktöriyel :", carpım)
"""
#örnek 10
taban = int(input("Taban Giriniz :"))
kuvvet =int(input("Kuvvet Giriniz :"))
sonuc= 1
for i in range (kuvvet):
    sonuc*= taban
print( f"{taban}^{kuvvet} = {sonuc}")

