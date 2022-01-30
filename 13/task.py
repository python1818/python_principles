import random
sayi = random.randint(1, 10)
#print(sayi)
can = int(input("Kaç kerede bilebilirsin? : "))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahminini gir :"))
    if sayi == tahmin:
        print(
            f"Tebrikler {sayac}. defada bildin. Puanın: {100 - ((100/can)*(sayac-1)) } ")
        break
    elif sayi > tahmin:
        print("Yukari ")

    else:
        print("Aşağı ")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı : {sayi} idi.")

print("Oyundan çıkılıyor")