import random

def addCustomer():
    customerNum =random.randint(1000,10000)
    name = input("New customer name ?")
    surname = input("New customer surname ?")
    phone = input("New customer phone number ?")
    balance = int(input("New customer balance ?"))
    newCustomer={"customerNum":customerNum,"name":name,"surname":surname,"phone":phone,"balance":balance}
    with open("contacts.txt","r+", encoding="utf-8") as file :
        textList = file.readlines()
        textList.append("\n"+ str(newCustomer))
        file.seek(0)
        file.writelines(textList)
        
        

addCustomer()