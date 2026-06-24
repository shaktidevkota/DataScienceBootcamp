class Student:
    def __init__(self, name, age, height, university, semester):
        self.name = name
        self.age = age
        self.height = height
        self.university = university
        self.semester = semester

    def display_profile(self):
        print("=" * 40)
        print("STUDENT PROFILE")
        print("=" * 40)
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age} years")
        print(f"Height     : {self.height} feet")
        print(f"University : {self.university}")
        print(f"Semester   : {self.semester}")
        print("=" * 40)

    def academic_status(self):
        if self.semester >= 4:
            print("Status     : Intermediate Undergraduate")
        else:
            print("Status     : Beginner Undergraduate")


student = Student(
    "Shakti Raj Devkota",
    20,
    5.6,
    "Bhaktapur Multiple Campus",
    4
)

student.display_profile()
student.academic_status()