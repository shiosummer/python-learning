class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def get_name(self):
        return f'{self.name}'
    def get_age(self):
        return int(self.age)
    def get_course(self):
        self.course.sort()
        return int(self.course[-1])

student=Student('Whzy','22',[80,3185,2159])
print(f'姓名:{student.get_name()}')
print(f'年龄:{student.get_age()}')
print(f'最高分:{student.get_course()}')