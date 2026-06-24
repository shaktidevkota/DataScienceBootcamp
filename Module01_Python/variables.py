class Student:
    def __init__(self, name, age, height, semester, is_csit_student):
        self.name = name
        self.age = age
        self.height = height
        self.semester = semester
        self.is_csit_student = is_csit_student

    def display_information(self):
        print("=" * 50)
        print("STUDENT INFORMATION")
        print("=" * 50)

        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Height         : {self.height} ft")
        print(f"Semester       : {self.semester}")

        status = "Yes" if self.is_csit_student else "No"
        print(f"CSIT Student   : {status}")

    def show_data_types(self):
        print("\nDATA TYPES")
        print("-" * 50)

        print(f"Name       -> {type(self.name).__name__}")
        print(f"Age        -> {type(self.age).__name__}")
        print(f"Height     -> {type(self.height).__name__}")
        print(f"Semester   -> {type(self.semester).__name__}")
        print(f"CSIT       -> {type(self.is_csit_student).__name__}")

    @staticmethod
    def convert_age(age_text):
        return int(age_text)


student = Student(
    name="Shakti Raj Devkota",
    age=20,
    height=5.6,
    semester=4,
    is_csit_student=True
)

student.display_information()
student.show_data_types()

print("\nTYPE CONVERSION")
print("-" * 50)

age_text = "20"
converted_age = Student.convert_age(age_text)

print(f"Before Conversion: {type(age_text).__name__}")
print(f"After Conversion : {type(converted_age).__name__}")