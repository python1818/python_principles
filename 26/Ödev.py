import requests

import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")
r2 = r.text
r3 = json.loads(r2)

# for i in r3:
#     if i == 1 :
#         print(i) 

print(r3[0])
print(r3[1])
print(r3[2])
print(r3[3])
print(r3[4])
print(r3[5])
print(r3[6])
print(r3[7])
print(r3[8])
print(r3[9])
print(r3[10])
print(r3[11])
print(r3[12])
print(r3[13])
print(r3[14])
print(r3[15])
print(r3[16])
print(r3[17])
print(r3[18])
print(r3[19])
