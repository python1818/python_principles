class Student:
    def __init__(self, sNumber, name, surname, phone, wallet):
        self.sNumber = sNumber
        self.name = name
        self.surname = surname
        self.phone = phone
        self.wallet = wallet


s1 = Student(sNumber=101, name="Ali", surname="Ak", phone="12345", wallet=1000)
print(s1)
print(s1.__dict__)
s2 = Student(102, "Ayşe", "Al", "99999", 0)
s3 = Student(103, "Zeynep", "Ak", "12345", 2000)
s4 = Student(104, "Ahmet", "Al", "99999", 1500)
print(s2.__dict__)
print(s3.__dict__)
print(s4.__dict__)