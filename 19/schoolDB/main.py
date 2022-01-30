from student import Student
from schoolDB import sdb1

print("welcoe to our schoolDB")


while True:
    choice = int(input("""
        1- list all student
        2- save new student
        type your choice   :
        """

    
    
    ))
    if choice==1:
        sdb1.listStudents()
    elif choice==2:
        sdb1.saveStudent()
