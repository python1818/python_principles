kilo = int(input("kilonuzu girin: "))
boy = int(input("boyunuzu cm cinsinden girin: "))
kilo_boy_endeksi = kilo*10000/boy**2
if  0 < kilo_boy_endeksi <=18.5 :
  print("zayıfsınız")
elif  18.5 < kilo_boy_endeksi <= 25 :
  print("kilonuz normal")
elif  25.0 < kilo_boy_endeksi <= 30 :
  print("kilolusunuz")
elif 30< kilo_boy_endeksi :
  print("obezsiniz")
else:
  print("yanlis girdiniz")
