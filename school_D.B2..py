from tabulate import tabulate
students = [
    {"sNumber": 101, "name": "Ali", "surname": "Ak", "phone": "12345","wallet":1000},
    {"sNumber": 102, "name": "Ayşe", "surname": "Al", "phone": "99999","wallet":500},
    {"sNumber": 103, "name": "Tina", "surname": "Schwarz", "phone": "1312345","wallet":1000},
    {"sNumber": 104, "name": "Hans", "surname": "Wolter", "phone": "993199","wallet":500},
]




def saveStudent(sNumber, name, surname, sPhone,wallet):
    sNumberlist=[]
    for i in students:
        sNumberlist.append(i["sNumber"])

    sNumberlist.sort()
    if sNumber in sNumberlist:
        print(f"there is a student with student number{sNumber}")
        print(f"student could not added to Datebase")
        print(f"last student number is:{sNumberlist[-1]}")
    else:
        students.append({"sNumber":sNumber,"name":name,
                    "surname":surname,"phone":sPhone,"wallet":wallet})
    
    
    
    # students.append({"sNumber": sNumber, "name": name,
    #                 "surname": surname, "phone": sPhone, "wallet":wallet})


def listStudents():
    print(tabulate(students,headers="keys"))


def addMoneyToWallet(sNumber, amount):
    for i in students:
        if i["sNumber"] == sNumber:
            i["wallet"]+=amount




print("\n")
print("*".center(50, "-"))
print("Welcome to our School Database".center(50, "-"))

while True:
    print("To see student list, type '1': ")
    print("To add new student, type '2': ")
    print("To add balance to a student wallet type '3': ")
    print("To quit, type 'q': ")
    choice = input("Type your choice : ")
    if choice == "q":
        break
    elif choice == "1":
        listStudents()
    elif choice == "2":
        sNumber = int(input("Student Number : "))
        name = input("Student Name : ")
        surname = input("Student Surname: ")
        sPhone = input("Student Phone : ")
        wallet = int(input("wallet balence:"))
        saveStudent(sNumber, name, surname, sPhone, wallet)
    elif choice == "3":
        sNumber = int(input("Student Number :"))
        amount =int(input("Balence to add :"))
        addMoneyToWallet(sNumber,amount)
    else:
        continue

    print("\n \n ")  # new line