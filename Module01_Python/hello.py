class DataScienceStudent:
    def __init__(self, name, college, goal):
        self.name = name
        self.college = college
        self.goal = goal

    def display_profile(self):
        print("=" * 40)
        print("DATA SCIENCE STUDENT PROFILE")
        print("=" * 40)
        print(f"Name    : {self.name}")
        print(f"College : {self.college}")
        print(f"Goal    : {self.goal}")

student = DataScienceStudent(
    "Shakti Raj Devkota",
    "Bhaktapur Multiple Campus",
    "Become a Data Scientist"
)

student.display_profile()