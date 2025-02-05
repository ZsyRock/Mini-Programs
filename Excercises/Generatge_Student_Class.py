# class Student:
#     def __init__(self, student_name, student_ID, student_Chinese, student_Math, student_English):
#         self.name = student_name
#         self.ID = student_ID
#         self.Chinese = float(student_Chinese)
#         self.Math = float(student_Math)
#         self.English = float(student_English)
#
#     def grade(self):
#         Mean_Grade = (self.Chinese + self.Math + self.English) / 3
#         print(f"this student {self.name} whose ID is {self.ID} has the grade: \nChinese grade is: {self.Chinese},\nMath grade is: {self.Math},\nEnglish grade is: {self.English},\n{self.name}'s mean grade is: {Mean_Grade}, Hope he can do better in the future!")
#
# student_xiaoming = Student("Xiaoming", 123, 90, 80, 70)
# student_xiaoming.grade()

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"Chinese": 0, "Math": 0, "English": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"This student {self.name} (ID: {self.student_id}) grade is ")
        for course in self.grades:
            print(f"{course}: {self.grades[course]} scores")

chen = Student("Chen Chen", "123456")
zeng = Student("Zeng Xiaoxian", "654321")
chen.set_grade("Chinese", 98)
chen.set_grade("English", 99)
chen.print_grades()
print(chen.name)
zeng.set_grade("Math", 95)
print(zeng.grades)



