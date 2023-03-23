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
    print("Tahmin Hakkı =", tahmin_hakkı," \n ")
    tahmin = input("Tahmininizi girin:")
    if str(tahmin) == "q":
        print("Oyundan çıkılıyor....")
        time.sleep(1)
        break
    elif tahmin_hakkı == 1:
        print("Tahmin hakkınız kalmadı.\nSayınız:",rastgele_sayi,"\nKaybettiniz...")
        time.sleep(1)
        break
    elif str(tahmin) == "l":
        print("Sayı:",rastgele_sayi)
        time.sleep(1)
        print("Tekrar başlanıyor")
        time.sleep(1)

        rastgele_sayi = random.randint(1, 40)
        tahmin_hakkı = 5
    elif (int(tahmin) < rastgele_sayi):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha yüksek bir sayı söyleyin.")
        print("Tahmin Hakkı:", tahmin_hakkı)
    elif (int(tahmin) > rastgele_sayi):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha düşük bir sayı söyleyin.")
        print("Tahmin Hakkı:", tahmin_hakkı)
    elif str(tahmin) == "r":
        print("Tekrar başlanıyor")
        time.sleep(1)
        rastgele_sayi = random.randint(1, 40)
        tahmin_hakkı = 5

    elif 0<int(tahmin)<40:

        if rastgele_sayi==tahmin:
            print("Tebrikler doğru bildiniz.")
            time.sleep(1)
            break
        else:
            print("Tekrar deneyiniz")
            time.sleep(1)
            tahmin_hakkı -= 1
    else:
        print("Geçerli bir sayı giriniz.")























