import random
import time


# class metodları

class Maca:
    def __init__(self, number, isim="maca_x", simge="Maça"):
        self.number = number
        self.simge = simge
        self.isim = isim
        self.isim = (self.simge + "_" + str(self.number)).upper()

class Sinek:
    def __init__(self, number, isim="sinek_x", simge="Sinek"):
        self.number = number
        self.simge = simge
        self.isim = isim
        self.isim = (self.simge + "_" + str(self.number)).upper()

class Karo:
    def __init__(self, number, isim="karo_x", simge="Karo"):
        self.number = number
        self.simge = simge
        self.isim = isim
        self.isim = (self.simge + "_" + str(self.number)).upper()

class Kupa:
    def __init__(self, number, isim, simge="Kupa"):
        self.number = number
        self.simge = simge
        self.isim = isim
        self.isim = (self.simge + "_" + str(self.number)).upper()

class Yerdekartyok:
    number = 0
    isim = "Yok"

class Player:
    def __init__(self, isim, elindekiler=[], kazanilanKartlar=[]):
        self.isim = isim
        self.elindekiler = elindekiler
        self.kazanilanKartlar = kazanilanKartlar

class Player2:
    def __init__(self, isim, elindekiler=[], kazanilanKartlar=[]):
        self.isim = isim
        self.elindekiler = elindekiler
        self.kazanilanKartlar = kazanilanKartlar

def Deste():
    global deste
    deste = []

    for a in range(1, 14):
        deste.append(Maca(a, "maça"))


    for a in range(1, 14):
        deste.append(Sinek(a, "sinek"))

    for a in range(1, 14):
        deste.append(Karo(a, "karo"))

    for a in range(1, 14):
        deste.append(Kupa(a, "kupa"))

    random.shuffle(deste)
    return deste

def OyuncuGirdi():
    global player1
    global player2
    player1 = Player(input("""
Oyuncu 1 İsim:"""), deste[0:25])
    player2 = Player2(input("""Oyuncu 2 İsim:"""), deste[25:49])
    print("""
kartlar karılıyor....""")
    time.sleep(1)

def gameBaslangic():
    global secimBaslangıc
    global deste
    while True:
        global secimBaslangıc
        print("""
        PİŞTİ OYUNUNA HOŞGELDİNİZ
        *************************
        Başlamak için:S
        Çıkmak için:Q
            """)

        secimBaslangıc = input("Yapmak istediğiniz işlemi seçiniz:")
        if secimBaslangıc == "s":
            break
        elif secimBaslangıc == "q":
            print("oyundan çıkılıyor....")
            break
        else:
            print("Geçerli bir değer giriniz...")

def kartlariTemizle():
    yerdeki_kartlar.clear()
    yerdeki_kartlar.append(Yerdekartyok())

def kartAtPlayer1(a, b, c, d):

    global pisti2
    global pisti1
    global yerdeki_kartlar
    global atilankart
    print("""***************************************************************************************

                             {} OYUNCUSUNUN KARTLARI

        1.KART: {}      2.KART: {}      3.KART: {}      4.KART: {} 
                """.format(player1.isim.upper(), a, b, c, d))
    atilankart = [yerdeki_kartlar[-1]]
    while True:

        secilen_sayi = input("Kart seçiniz:")
        if secilen_sayi == "1":
            if player1Kartlar[0].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 1:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[0])
                del player1.elindekiler[0]

            elif player1Kartlar[0].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[0])
                del player1.elindekiler[0]

            elif player1Kartlar[0].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[0])
                del player1.elindekiler[0]
                atilankart.append(player1Kartlar[0])





        elif secilen_sayi == "2":
            if player1Kartlar[1].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[1])
                del player1.elindekiler[1]


            elif player1Kartlar[1].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[1])
                del player1.elindekiler[1]


            elif player1Kartlar[1].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[1])
                del player1.elindekiler[1]
                atilankart.append(player1Kartlar[1])




        elif secilen_sayi == "3":
            if player1Kartlar[2].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[2])
                del player1.elindekiler[2]


            elif player1Kartlar[2].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[2])
                del player1.elindekiler[2]

            elif player1Kartlar[2].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[2])
                del player1.elindekiler[2]
                atilankart.append(player1Kartlar[2])




        elif secilen_sayi == "4":
            if player1Kartlar[3].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[3])
                del player1.elindekiler[3]
                atilankart.append(Maca(0, "pişti"))

            elif player1Kartlar[3].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[3])
                del player1.elindekiler[3]
                atilankart.append(Maca(0, "pişti"))

            elif player1Kartlar[3].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[3])
                del player1.elindekiler[3]
                atilankart.append(player1Kartlar[3])


        else:
            print("Geçerli bir sayı giriniz")
            continue
        print("Yerdeki Kart: {}".format(yerdeki_kartlar[-1].isim))
        break

def kartAtPlayer1_2(a, b, c, d):

    global pisti2
    global pisti1
    global yerdeki_kartlar
    global atilankart
    print("""***************************************************************************************

                             {} OYUNCUSUNUN KARTLARI

        1.KART: {}      2.KART: {}      3.KART: {}      4.KART: {} 
                """.format(player1.isim.upper(), a, b, c, d))
    while True:
        secilen_sayi = input("Kart seçiniz:")
        if secilen_sayi == "1":
            if player1Kartlar[0].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[0])
                del player1.elindekiler[0]

            elif player1Kartlar[0].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[0])
                del player1.elindekiler[0]
                atilankart.append(Maca(0, "pişti"))
            elif player1Kartlar[0].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[0])
                del player1.elindekiler[0]
                atilankart.append(player1Kartlar[0])




        elif secilen_sayi == "2":
            if player1Kartlar[0].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[1])
                del player1.elindekiler[1]


            elif player1Kartlar[1].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[1])
                del player1.elindekiler[1]

            elif player1Kartlar[0].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[1])
                del player1.elindekiler[1]



        elif secilen_sayi == "3":
            if player1Kartlar[0].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[2])
                del player1.elindekiler[2]



            elif player1Kartlar[2].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[2])
                del player1.elindekiler[2]


            elif player1Kartlar[0].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[2])
                del player1.elindekiler[2]
                atilankart.append(player1Kartlar[2])




        elif secilen_sayi == "4":
            if player1Kartlar[0].number == atilankart[-1].number:
                if len(yerdeki_kartlar) ==2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti1 +=1
                    kartlariTemizle()
                else:
                    player1.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player1.kazanilanKartlar.append(player1.elindekiler[3])
                del player1.elindekiler[3]


            elif player1Kartlar[3].number == 11:
                player1.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player1.kazanilanKartlar.append(player1.elindekiler[3])
                del player1.elindekiler[3]


            elif player1Kartlar[3].number != atilankart[-1].number:
                yerdeki_kartlar.append(player1.elindekiler[3])
                del player1.elindekiler[3]
                atilankart.append(player1Kartlar[3])

        else:
            print("Geçerli bir sayı giriniz")
            continue
        print("Yerdeki Kart: {}".format(yerdeki_kartlar[-1].isim))
        break

def kartAtPlayer2(a, b, c, d):
    global pisti2
    global pisti1
    global yerdeki_kartlar
    global atilankart
    print("""***************************************************************************************

                            {} OYUNCUSUNUN KARTLARI

        1.KART: {}      2.KART: {}      3.KART: {}      4.KART: {} 
            """.format(player2.isim.upper(), a, b, c, d))
    while True:
        secilen_sayi = input("Kart seçiniz:")
        if secilen_sayi == "1":
            if player2.elindekiler[0].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti2 +=1
                    kartlariTemizle()
                else:
                    player2.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player2.kazanilanKartlar.append(player2.elindekiler[0])
                del player2.elindekiler[0]

            elif player2.elindekiler[0].number == 11:
                player2.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player2.kazanilanKartlar.append(player2.elindekiler[0])
                del player2.elindekiler[0]

            elif player2.elindekiler[0].number != atilankart[-1].number:
                yerdeki_kartlar.append(player2.elindekiler[0])
                del player2.elindekiler[0]
                atilankart.append(player2Kartlar[0])






        elif secilen_sayi == "2":
            if player2.elindekiler[1].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti2 +=1
                    kartlariTemizle()

                else:
                    player2.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player2.kazanilanKartlar.append(player2.elindekiler[1])
                del player2.elindekiler[1]

            elif player2.elindekiler[1].number == 11:
                player2.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player2.kazanilanKartlar.append(player2.elindekiler[1])
                del player2.elindekiler[1]

            elif player2.elindekiler[1].number != atilankart[-1].number:
                yerdeki_kartlar.append(player2.elindekiler[1])
                del player2.elindekiler[1]
                atilankart.append(player2Kartlar[1])




        elif secilen_sayi == "3":
            if player2.elindekiler[2].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti2 +=1
                    kartlariTemizle()
                else:
                    player2.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player2.kazanilanKartlar.append(player2.elindekiler[2])
                del player2.elindekiler[2]


            elif player2.elindekiler[2].number == 11:
                player2.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player2.kazanilanKartlar.append(player2.elindekiler[2])
                del player2.elindekiler[2]

            elif player2.elindekiler[2].number != atilankart[-1].number:
                yerdeki_kartlar.append(player2.elindekiler[2])
                del player2.elindekiler[2]
                atilankart.append(player2Kartlar[2])



        elif secilen_sayi == "4":
            if player2.elindekiler[3].number == atilankart[-1].number:
                if len(yerdeki_kartlar) == 2:
                    print("Tebrikler Pişti Yaptınız.")
                    pisti2 +=1
                    kartlariTemizle()
                else:
                    player2.kazanilanKartlar.extend(yerdeki_kartlar)
                    kartlariTemizle()
                    player2.kazanilanKartlar.append(player2.elindekiler[3])
                del player2.elindekiler[3]

            elif player2.elindekiler[3].number == 11:
                player2.kazanilanKartlar.extend(yerdeki_kartlar)
                kartlariTemizle()
                player2.kazanilanKartlar.append(player2.elindekiler[3])
                del player2.elindekiler[3]

            elif player2.elindekiler[3].number != atilankart[-1].number:
                yerdeki_kartlar.append(player2.elindekiler[3])
                del player2.elindekiler[3]
                atilankart.append(player2Kartlar[3])

        else:
            print("Geçerli bir sayı giriniz")
        print("Yerdeki Kart: {}".format(yerdeki_kartlar[-1].isim))
        break

def gameIlkEl():
    global player1Kartlar
    global player2Kartlar
    global atilankart
    global deste
    print("""
Desteden 4 kart ortaya açıldı... 
EN ÜSTTEKİ KART: {}""".format(deste[51].isim.upper()))
    atilankart = deste[51]
    deste = deste[:48]
    tursayisi = 0
    while True:
        player1Kartlar = player1.elindekiler[0:4]
        player2Kartlar = player2.elindekiler[0:4]
        kartAtPlayer1(player1Kartlar[0].isim, player1Kartlar[1].isim, player1Kartlar[2].isim, player1Kartlar[3].isim)
        kartAtPlayer2(player2Kartlar[0].isim, player2Kartlar[1].isim, player2Kartlar[2].isim, player2Kartlar[3].isim)
        player1Kartlar = player1.elindekiler[0:3]
        player2Kartlar = player2.elindekiler[0:3]
        kartAtPlayer1_2(player1Kartlar[0].isim, player1Kartlar[1].isim, player1Kartlar[2].isim, "Kart Atıldı")
        kartAtPlayer2(player2Kartlar[0].isim, player2Kartlar[1].isim, player2Kartlar[2].isim, "Kart Atıldı")
        player1Kartlar = player1.elindekiler[0:2]
        player2Kartlar = player2.elindekiler[0:2]
        kartAtPlayer1_2(player1Kartlar[0].isim, player1Kartlar[1].isim, "Kart Atıldı", "Kart Atıldı")
        kartAtPlayer2(player2Kartlar[0].isim, player2Kartlar[1].isim, "Kart Atıldı", "Kart Atıldı")
        player1Kartlar = player1.elindekiler[0:1]
        player2Kartlar = player2.elindekiler[0:1]
        kartAtPlayer1_2(player1Kartlar[0].isim, "Kart Atıldı", "Kart Atıldı", "Kart Atıldı")
        kartAtPlayer2(player2Kartlar[0].isim, "Kart Atıldı", "Kart Atıldı", "Kart Atıldı")
        tursayisi += 1
        if tursayisi == 6:
            time.sleep(0.5)
            print("""
Oyun Bitti Puanlamaya Geçiliyor...
***************************************************************************************""")
            time.sleep(1)
            break
        else:
            print("""
                                              TUR BİTTİ""")
            time.sleep(0.5)
            print("                                       KAĞITLAR DAĞITILIYOR....")
            time.sleep(1)

def puanlama():
    player1puanlanacak = []
    player2puanlanacak = []
    player1Puan = 0
    player2Puan = 0

    for c in player1.kazanilanKartlar:
        player1puanlanacak.append(c.isim)
    if len(player1puanlanacak) == 0:
        print("{} hiç kart alamadı...".format(player1.isim.upper()))
    else:
        print("{} Kazandığı Kartlar: {}".format(player1.isim.upper(),player1puanlanacak))



    for d in player2.kazanilanKartlar:
        player2puanlanacak.append(d.isim)
    if len(player2puanlanacak) == 0:
        print("""{} hiç kart alamadı...
        """.format(player2.isim.upper()))
        time.sleep(1)
    else:
        print("""{} kazandığı kartlar: {}
        """.format(player2.isim.upper(),player2puanlanacak))
        time.sleep(1)



    for a in player1.kazanilanKartlar:
        if a.number == 1 or a.number == 11:
            player1Puan += 1
        elif a.isim == "MAÇA_2":
            player1Puan += 2
    player1Puan += 10*pisti1
    player2Puan += 10*pisti2
    if player1Puan == 0:
        print("{} hiç puan kazanamadı...".format(player1.isim.upper()))
        time.sleep(1)
    else:
        print("{} {} puan kazandı.".format(player1.isim.upper(),player1Puan))
        time.sleep(1)



    for b in player2.kazanilanKartlar:
        if b.number == 1 or b.number == 11:
            player2Puan += 1

        elif b.isim == "MAÇA_2":
            player2Puan += 2
    if player2Puan == 0:
        print("{} hiç puan kazanamadı...".format(player2.isim.upper()))
        time.sleep(1)
    else:
        print("{} {} puan kazandı.".format(player2.isim.upper(),player2Puan))
        time.sleep(1)

    if player1Puan > player2Puan:
        print("{} KAZANDI".format(player1.isim.upper()))
    else:
        print("{} KAZANDI".format(player2.isim.upper()))


# oyun çalıştıracak fonksiyonlar
while True:
    pisti1 = 0
    pisti2 = 0
    Deste()
    yerdeki_kartlar = deste[48:52]
    gameBaslangic()
    if secimBaslangıc == "s":
        print("")
    else:
        break
    OyuncuGirdi()
    gameIlkEl()
    puanlama()
    break

