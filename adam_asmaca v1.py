import random
kelimeler = ["Ahmet","Ahmetimsi","Ahmetcan"]
a = random.choice(kelimeler)
b = len(a)
print(f"bulmanız gereken kelime {b} harflidir")

d = 0
while d < 5:
    c = input("Kelimeyi Giriniz:  ")
    if a == c:
        print("Kelimeyi Doğru bildiniz")
        break
    else:
        print("Kelimeyi yanlış buldunuz")
        d = d + 1

if d == 5:
    print("Öldünüz")
else:
    print("Kazandınız")