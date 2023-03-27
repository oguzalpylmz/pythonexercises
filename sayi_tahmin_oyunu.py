import random
import time

print("""***************************************
Tahmin Oyunu
1 ile 40 arasındaki sayıyı tahmin edin.
Çıkmak için:Q
Sayıyı Öğrenmek İçin:L
Tekrar Başlamak İçin:R
***************************************
""")

rastgele_sayi = random.randint(1, 40)
tahmin_hakkı = 5
while True:
    try:
        print("Tahmin Hakkı =", tahmin_hakkı, " \n ")
        tahmin = input("Tahmininizi girin:")
        if str(tahmin) == "q":
            print("Oyundan çıkılıyor....")
            time.sleep(1)
            break
        elif str(tahmin) == "l":
            print("Sayınız: "+ str(rastgele_sayi))
            time.sleep(1)
            break
        elif not 1 < int(tahmin) < 40:
            print("Geçerli aralıkta sayı giriniz.")
        elif int(tahmin) == int(rastgele_sayi):
            print("Tebrikler doğru bildiniz.")
            time.sleep(1)
            break
        elif tahmin_hakkı == 1:
            print("Tahmin hakkınız kalmadı.\nSayınız:", rastgele_sayi, "\nKaybettiniz...")
            time.sleep(1)
            break
        elif int(tahmin) < int(rastgele_sayi):
            print("daha büyük bir sayı gir")
            tahmin_hakkı -= 1
        elif int(tahmin) > int(rastgele_sayi):
            print("daha küçük sayı gir")
            tahmin_hakkı -= 1
        else:
            print("Geçerli bir sayı giriniz.")
            break
    except:
        print("Geçerli bir değer giriniz")
