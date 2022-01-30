from student import Student
from student import s1, s2, s3, s4


class SchoolDB:
    students = [s1, s2, s3, s4 ]

    def __init__(self, schoolName):
        self.schoolName = schoolName

    def listStudents(self):
        for student in self.students:
            # print(student.__dict__)
            print(student.sNumber, "-", student.name,
                  student.surname, student.phone, student.wallet)

    def saveStudent(self):
        sNumber = int(input("Student number :"))
        name = input("Student name :")
        surname = input("Student surname :")
        sPhone = input("Student phone :")
        wallet = int(input("Wallet Balance :"))
        s5 = Student(sNumber,name, surname,sPhone, wallet)
        self.students.append(s5)

sdb1 = SchoolDB("Atatürk İlkokulu")
