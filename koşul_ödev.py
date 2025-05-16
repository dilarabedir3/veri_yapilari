# -*- coding: utf-8 -*-
"""
Created on Fri May 16 22:39:18 2025

@author: HUAWEI
"""

#Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. 
#Kullanıcının geliri;10000 ve altındaysa maaşından %5 kesinti olur. 
#25000 ve altındaysa maaşından %10 kesinti olur.
#45000 ve altındaysa maaşından %25 kesinti olur.
#Diğer koşullarda %30 kesinti olur. Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

maas = int(input("Maaş bilginizi giriniz: "))

if 0 < maas <= 10000:
    net_maas = maas - maas*0.05
    
if 10000 < maas <= 25000:
    net_maas = maas - maas*0.10


if 25000 < maas <= 45000:
    net_maas = maas - maas*0.15
    
else:
    net_25000maas = maas - maas*0.30

print("Net maaş:", net_maas )


#Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir.
#Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
#altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. 
#(Sadece koşul kullanılması yeterli.)

kullanici_adi = input("Kullanıcı adınızı yazınız: ")
sifre = input("Şifrenizi yazınız: ")

if len(sifre) >= 6:
    print("Hesabınız Oluşturuldu")

else:
    print("Yeni Şifre Belirleyiniz!")


#Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
#Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
#Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
#Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder

kullanici_adi = input("Kullanıcı adınızı yazınız: ")
sifre = input("Şifrenizi yazınız: ")

while True:

    if 5 < len(sifre)<10:
        print("Hesabınız Oluşturuldu")
        break
    else:
        print("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")
        

#Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
#Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
#Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
#Tercihe göre kalan hak bilgisi verilir.

kullanici_adi = input("Kullanıcı adınızı yazınız: ")
dogru_sifre="245825"
hak=3

while hak > 0:
    sifre = input("Şifrenizi yazınız: ")

    # Şifre doğruysa giriş yapılır
    if sifre == dogru_sifre:
        print("Giriş yapıldı.")
        break 
    else:
        hak -= 1  
        print("Yanlış şifre girildi!")

       
        if hak > 0:
            print(f"Kalan hakkınız: {hak}")
        else:
            print("Üç yanlış denemede şifreyi bilemediniz. Program sonlandırılıyor.")
    


