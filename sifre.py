import random
karakterler="1234567890*-qwertyuopasdfghjklizxcvbnm."
uzunluk=int(input("Parola kaç karakter uzunluğunda olacak?"))
sifre=""
for i in range(uzunluk):
    sifre += random.choice(karakterler)
print(sifre)
