a="10011010000000000110"

def consecutive_zeros(a):
    mylist=a.split("1")
    lenList=[]
    for i in mylist:
        lenList.append(len(i))
    return max(lenList)

print(consecutive_zeros(a))
        
        