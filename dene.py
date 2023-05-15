import time
def giris():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for x in dosya:
            time.sleep(1)
            kullanici, sifre_ = x.strip().split(",")
            if kullanici == kullanici_adi and sifre == sifre_:
                print("Giriş yapıldı.")
                return

    print("Kullanıcı adı veya şifre hatalı.")

giris()