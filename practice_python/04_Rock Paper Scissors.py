



a = "Kagıt"
b = "makas"
c = "tas"
d = input ("a = Kagıt b = makas  c = tas, lutfen birinci oyuncu hangı hamleyi oynamak istiyorsa sıkkı girin ")
e = input ("a = Kagıt b = makas  c = tas, lutfen ikincı oyuncuhangı hamleyi oynamak istiyorsa sıkkı girin " )

dPuan= 0
ePuan= 0
if d == a and e == a :
    print ("esit hamle")

elif d == a and e == b:
    print("ikinci oyuncu kazandı")
    ePuan + 10

elif d== a and e == c :
    print("birinci oyuncu kazandi")
    dPuan+10

elif d== b and e == a :
    print("birinci oyuncu kazandi")
    dPuan+10

elif d== b and e == b:
    print ("esit hamle")

elif d==b and e == c :
    ("ikinci oyuncu kazandı")
    ePuan + 10

elif d==c: