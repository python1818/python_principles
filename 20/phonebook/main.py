def addContacts():
    id = int(input("Contact Id : "))
    name = input("Contact Name : ")
    surname = input("Contact Surname : ")
    phone = input("Contact Phone : ")
    address = input("Contact Adress : ")
    contact = {"id": id, "name": name, "surname": surname,
               "phone": phone, "address": address}
    print(contact)
    with open("contacts.txt", "r+", encoding="utf-8") as f:
        textList = f.readlines()
        print(textList)
        textList.insert(-1, str(contact) + ",\n")
        f.seek(0)
        f.writelines(textList)


addContacts()
