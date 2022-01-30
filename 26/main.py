#   myList=["Trier","Eskişehir","Manheim"]

#  for i in myList:
#      print(i)
    
    
# myDict={"name":"Burhan","surname":"Altintop","phone":{"home":"123","Work":"321"},"favCities":["Trier","Manheim","Eskişehir"]}
# artists = [
#     {"name":"Burhan","surname":"Altintop","phone":{"home":"123","Work":"321"},"favCities":["Trier","Manheim","Eskişehir"]},
#     {"name":"kemal","surname":"Sunal","phone":{"home":"123","Work":"321"}, "favCities":["Trier","Manheim","Eskişehir"]},
#     {"name":"ayse","surname":"kara","phone":{"home":"123","Work":"321"},"favCities":["Trier","Manheim","Eskişehir"]}
# ]
# for i in artists:
#     print(i["name"])
#     for city in i["favCities"]:
#         print(city)
import json
import requests

r = requests.get("https://restcountries.com/v3.1/name/turkey")
r2 = r.text
r3 = json.loads(r2)

print(r3[0]["region"])
print(r3[0]["flags"]["png"])
print(r3[0]["independent"])
print(r3[0]["borders"][-2])
True
True

myDict ={"independent":True}

data= json.dumps(myDict)

print (data)