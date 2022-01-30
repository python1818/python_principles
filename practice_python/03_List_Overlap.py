a = [1, 1, 2, 3, 5, 8, 13, 34,21,  55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =[]
for i in a:
    if i in b:
        if i in c:
            continue
        else:
            c.append(i)
        
print(c)
       