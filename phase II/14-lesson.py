# class Class1:
#     def m(self):
#         print("In Class1")
#
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#         super().m()
#
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         super().m()
#
# class Class3_1(Class1):
#     def m(self):
#         print("In Class3_1")
#         super().m()
#
# class Class4(Class2, Class3, Class3_1):
#     def m(self):
#         print("In Class4")
#         super().m()
#
#
# m = Class4()
# m.m()
# print(Class4.mro())

class Subject(object):
    def __init__(self, name, teacher):
        self.subject_name = name
        self.subject_teacher = teacher

    def get_subject(self):
        print("{0}: by {1}".format(self.subject_name, self.subject_teacher))


class Student(object):
    def __init__(self, name):
        self.student_name = name
        self.subjects = []

    def add_subjects(self, subj_obj):
        self.subjects.append(subj_obj)

    def get_subjects(self):
        print([subj.get_subject() for subj in self.subjects])


subj1 = Subject('Python programming', "Choriev Muzaffarmirzo")
subj2 = Subject('Front-end programming', "Otabek Temirov")

std1 = Student("Nurmuhammad")
std1.add_subjects(subj1)
std1.add_subjects(subj2)

std1.get_subjects()































