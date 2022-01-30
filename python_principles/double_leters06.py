import re


def double_leters(a):
    b=""
    
    for i in a:
        b = i
        b.insert(i)
        print(b)
        if b==i:
            return True
        else:
    return False
        c=+1

          

print(double_leters("assda"))