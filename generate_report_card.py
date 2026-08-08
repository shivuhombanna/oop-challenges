class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.__marks={}

    def reed_marks(self):
        return self.__marks

    def add_marks(self,subject,marks):
        self.__marks[subject]=marks

    def calculate_avg(self):
        total=0
        for marks in self.__marks.values():
            total+=marks
        avarage =total/len(self.__marks)
        return avarage

    def is_pass(self):
        he_pass=all(mark<35 for mark in self.__marks.values())
        if he_pass:
            print(f"{self.name} is pass ")
        else:
            print(f"{self.name} is fail ")

    def calculate_grade(self):
        print("Gread ", end="")
        persntage=self.calculate_avg()/100
        if persntage>=85:
            print("A")
        elif persntage>=65:
            print("B")
        else:
            print("c")

class Report:
    @staticmethod
    def generate(student:Student):
        student_mark= student.reed_marks()
        print(f"Name : {student.name}   roll_no {student.rollno}")
        print("----------------------MARKS---------------------------")
        for subject, marks in student_mark.items():
            print(f"{subject}    {marks} ")
        print(f"Avarage : {student.calculate_avg()}")
        student.is_pass()
        student.calculate_grade()

s=Student( "Shivaraj",1)
s.add_marks("maths",98)
s.add_marks("science",33)

Report.generate(s)


