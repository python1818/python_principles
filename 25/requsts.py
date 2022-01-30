
import requests  
import json

# r = requests.get("https://restcountries.com/v3.1/name/turkey")
# result = r.text
# result2 = json.loads(result)
# print(result2[0]["region"])
# print(result2[0]["popultion"])
# print(result2[0]["capital"])

# ₺
# print(result[0]["capital"])
# print(result[1]["capital"])
# print(result[246]["capital"])

# counter = 0
# for i in result:
#     counter += 1
#     print( counter, i ["name"]["official"])

# r= requests.get("https://api.frankfurter.app/latest")
# result = r.text
# result = json.loads(result)
# USD = (result["rates"]["USD"])
# TRY = (result["rates"]["TRY"])

# print("1 Euro ",TRY,"TLdir")
# print("1 Euro",USD, "Dolardır ")

# r= requests.get("https://api.genelpara.com/embed/doviz.json")
# result = r.text
# print(result)
# # result = json.loads(result)
# # print(result["USD"]["alis"])





r= requests.get("https://raw.githubusercontent.com/ozanerturk/covid19-turkey-api/master/dataset/timeline.json")
result = r.text
result =json.loads(result)

# for i in result:
#     print(i)

for i in result.items():
    print(i[0])