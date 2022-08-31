
from time import sleep as bekle
import random
import time

while True:

 banner = """

 ŞİFRE YARATMA

 """
 print(banner)

 ifadeler = 'abcçdefgğhıijklmnoöprsştuüvyz1234567890ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@#$%^&*'
 numara = input("<<<<<Oluşturmak İstediğiniz Şifre Sayısını Giriniz>>>>>  ")
 numara = int(numara)
 karakter = input("<<<<<Kaç Tane Karakterden Oluşturmak İstiyorsunuz>>>>>  ")
 karakter = int(karakter)
 time.sleep(5)
 print ("*****Şifreniz hazırlanıyor*****")
 for i in range(3):
  print(".")
 bekle(1)
 for Password in range(numara):
     Şifreniz = ''
     for char in range(karakter):
        Şifreniz += random.choice (ifadeler)
     print(" (+)Şifreniz: ",     Şifreniz)

 Devam = int(input("devam etmek istiyorsanız 1 değilse 2: "))

 if Devam == 1:
   continue


 if Devam  == 2:
  print("<<<Çıkış Yapılıyor!!!!!>>>")
 time.sleep(5)
 for i in range(3):
    print(".")
 bekle(2)
 break



