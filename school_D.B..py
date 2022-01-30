



from tabulate import tabulate

students = [
    {"sNumber": 101, "name": "Ali", "surname": "Ak",
        "phone": "12345", "wallet": 1000},
    {"sNumber": 102, "name": "Ayşe", "surname": "Al",
        "phone": "99999", "wallet": 0},
    {"sNumber": 103, "name": "Zeynep", "surname": "Ak",
        "phone": "12345", "wallet": 2000},
    {"sNumber": 104, "name": "Ahmet", "surname": "Al",
        "phone": "99999", "wallet": 1500},
]

# # # # # listede gösterilen şekilde bir okul öğrenci kayıt veritabanı oluşturun.
# # # # # öğrenci kaydı için bir fonksiyon yazın
# # # # # öğrencileri listeleyip bilgilerini görüntülemek için bir fonksiyon yazın
# # # # # bir menü yazarak öğrenci kaydı, öğrenci listeleme, ve quit seçeneklerini ekleyin
# # # # bütün öğrencilerin bilgilerine cüzdan ekleyiniz
# # # # cüzdana para ekleme fonksiyonu yazınız,
# # # # uygulama menusune para ekleme seçeneği ekleyiniz
# # # öğrenci kaydında aynı öğrenci numarası ile iki öğrenci olmasını engelleyiniz
# # # öğrenci kantinden alışveriş yapsın, hesabından para düşsün
# # schoolDB için seçilen öğrencinin bilgilerini güncelleme fonksiyonu ekleyiniz.
# # Menüye "öğreci bilgisini güncelle" seçeneği ekleyiniz.
# SchoolDB için bir menu() fonksiyonu oluşturarak bütün menüyü menu() fonksiyonuna
#  taşıyın programın bu şekilde çalışmasını sağlayın


def menu():
    while True:

        choice = input("""
            1- List all students
            2- Add new student
            3- Add balance to a student
            4- Shopping from cantine
            5- Edit a student

            To quit, type 'q'
            please choose an option from menu : """)

        if choice == "q":
            break
        num = int(choice)
        if num == 1:
            listStudents()
        elif num == 2:
            sNumber = int(input("Student number :"))
            name = input("Student name :")
            surname = input("Student surname :")
            sPhone = input("Student phone :")
            wallet = int(input("Wallet Balance :"))
            saveStudent(name, surname, sNumber, sPhone, wallet)
        elif num == 3:
            sNumber = int(input("Student number :"))
            amount = int(input("Balance to add :"))
            addMoneyToWallet(sNumber, amount)
        elif num == 4:
            sNumber = int(input("Student number :"))
            info = input("Information : ")
            amount = int(input("Balance to deduct : "))
            shoppingFromCantine(sNumber, info, amount)
        elif num == 5:
            sNumber = int(input("Student number to update :"))
            updateStudent(sNumber)
        else:                                       #
            continue


def saveStudent(name, surname, sNumber, sPhone, wallet):
    sNumberList = []
    for i in students:
        sNumberList.append(i["sNumber"])

    sNumberList.sort()
    if sNumber in sNumberList:
        print(f"There is a student with student number {sNumber} ")
        print(f"Student could not added to DataBase ")
        print(f"Last student number is : {sNumberList[-1]}")
    else:
        students.append({"sNumber": sNumber, "name": name,
                         "surname": surname, "phone": sPhone, "wallet": wallet})


def listStudents():
    print(tabulate(students, headers="keys"))


def addMoneyToWallet(sNumber, amount):
    # yeni birşey
    for i in students:
        print(i)
        if i["sNumber"] == sNumber:
            # print(i)
            # print(i["wallet"])
            i["wallet"] += amount
            # print(i["wallet"])


def shoppingFromCantine(sNumber, info, amount):
    for student in students:
        if student["sNumber"] == sNumber:
            student["wallet"] -= amount
            print(f" {amount} TL for: {info} ")
            print(
                f" Student Number {sNumber}, new wallet balance: {student['wallet']}")


def updateStudent(sNumber):
    for student in students:
        if student["sNumber"] == sNumber:
            print(student)
            print(f"for the student number : {student['sNumber']}")
            name = input("new student name : ")
            surname = input("new student surname : ")
            sPhone = input("new student phone : ")
            wallet = input("new student wallet balance : ")
            # student = {"sNumber": sNumber, "name": name,
            #            "surname": surname, "phone": sPhone, "wallet": wallet}
            student["name"] = name
            student["surname"] = surname
            student["phone"] = sPhone
            student["wallet"] = wallet
            print(f"Student Number {sNumber} is updated ")


print("*".center(50, "-"))
print("Wellcome to our School Database".center(50, "-"))
menu()
