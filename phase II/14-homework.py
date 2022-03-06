class Base(object):
    def __init__(self, name):
        self.name = name


class University(Base):
    def __init__(self, name, location):
        Base.__init__(self, name)
        self.location = location
        # self.students = []
        # self.professors = []
        self.faculty = []
        self.subjects = []

    def add_subjects(self, *subject):
        for i in subject:
            self.subjects.append(i)

    def delete_subjects(self, subject):
        self.subjects.remove(subject)

    def get_subjects(self):
        for subject in self.subjects:
            subject.get_name()


class Faculty(Base):
    def __init__(self, name):
        Base.__init__(self, name)
        self.students = []
        self.professors = []

    def add_student(self, *students):
        for student in students:
            self.students.append(student)

    def delete_subjects(self, student):
        self.students.remove(student)

    def get_students(self):
        for student in self.students:
            student.get_name()


class Professor(Base):
    def __init__(self, name,faculty):
        Base.__init__(self, name)
        self.faculty = faculty
        self.subject = []


class Student(Base):
    def __init__(self, name, id, faculty):
        Base.__init__(self, name)
        self.id = id
        self.faculty = faculty
        self.subjects = []

    def get_name(self):
        print("{0}| {1}: {2}".format(self.faculty, self.id, self.name)) #SOCIE| u1610163: Muzaffarmirzo Choriev

    def add_subjects(self, *subject):
        for i in subject:
            self.subjects.append(i)

    def delete_subjects(self, subject):
        self.subjects.remove(subject)

    def get_subjects(self):
        for subject in self.subjects:
            subject.get_name()


class Subject(Base):
    def __init__(self, name, professor):
        Base.__init__(self, name)
        self.professor = professor

    def get_name(self):
        print('{0} by {1} '.format(self.name, self.professor))


std1 = Student("Muzaffarmirzo", 1610163, "SOCIE")
std1.get_name()

subj1 = Subject('Web programming', "Aziz Xodjaev")
subj2 = Subject('System programming', "Prof. Naseer")
subj3 = Subject('Analytics and Statistic', "Boxodir Yuldashev")
subj4 = Subject('Academic English', "Ms. Iroda")
subj5 = Subject('History', "Palonchi")

std1.add_subjects(subj1, subj2, subj3, subj4, subj5)
std1.get_subjects()

