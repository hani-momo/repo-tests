from peewee import *

conn = SqliteDatabase('uni.sqlite')
conn.connect()

class BaseModel(Model): # parent class, connection. for no duplication
    class Meta:
        database = conn

class Students(BaseModel): # peewee's Models

    id = AutoField() # Primary key
    name = CharField(max_length=15, null=False)
    surname = CharField(max_length=20, null=False)
    age = IntegerField(null=False)
    city = CharField(max_length=20, null=False)

class Courses(BaseModel):

    id = AutoField() # Primary key
    name = CharField(max_length=10, null=False)
    time_start = DateField(null=False)
    time_end = DateField(null=False)

class StudentCourses(BaseModel):

    student_id = ForeignKeyField(Students, field=Students.id, backref='courses')
    course_id = ForeignKeyField(Courses, field=Courses.id, backref='students')
    primary_key = CompositeKey('student_id', 'course_id') # Primary keys

conn.create_tables([Students, Courses, StudentCourses])

# insert data
c_data = [
    (1, 'python', '2021-07-21', '2021-08-21'),
    (2, 'java', '2021-07-13', '2021-08-16')
]
Courses.insert_many(c_data).execute()

s_data = [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manchester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')
]
Students.insert_many(s_data).execute()

sc_data = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)
]
StudentCourses.insert_many(sc_data).execute()
conn.commit()

# select data
query = Students.select().where(Students.age > 30)
print('Query: Students older than 30 years')
for student in query:
    print(student.name, student.surname, student.age)

query = (Student.select().join(StudentCourse).join(Course).where(Course.name == 'python'))
print('Query: Students attending Python course')
for student in query:
    print(student.name, student.surname, student.age, student.city)

query = (Student.select().join(StudentCourse).join(Course).where((Course.name == 'python'), (Student.city == 'Spb')))
print('Query: Students attending Python course and from Spb')
for student in query:
    print(student.name, student.surname, student.age, student.city)

conn.close()
