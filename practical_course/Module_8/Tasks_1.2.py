import sqlite3

# 1
conn = sqlite3.connect('uni.db')
cursor = conn.cursor()

createStudents = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(15) NOT NULL,
        surname VARCHAR(20) NOT NULL,
        age INT NOT NULL,
        city VARCHAR(20) NOT NULL
    );
'''

createCourses = '''
    CREATE TABLE IF NOT EXISTS Courses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(10) NOT NULL,
        time_start DATE NOT NULL,
        time_end DATE NOT NULL
    );
'''

createStudentCourses = '''
    CREATE TABLE IF NOT EXISTS StudentCourses (
        student_id INT,
        course_id INT,
        FOREIGN KEY(student_id) REFERENCES Students(id),
        FOREIGN KEY(course_id) REFERENCES Courses(id),
        PRIMARY KEY(student_id, course_id)
    );
'''
cursor.execute(createStudents)
cursor.execute(createCourses)
cursor.execute(createStudentCourses)

# 2
c_data = [
    (1, 'python', '2021-07-21', '2021-08-21'),
    (2, 'java', '2021-07-13', '2021-08-16')
]
cursor.executemany('''
    INSERT INTO Courses (id, name, time_start, time_end)
    VALUES (?, ?, ?, ?)
''', c_data)

s_data = [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manchester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')
]
cursor.executemany('''
    INSERT INTO Students (id, name, surname, age, city)
    VALUES (?, ?, ?, ?, ?)
''', s_data)

sc_data = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)
]
cursor.executemany('''
    INSERT INTO StudentCourses (student_id, course_id)
    VALUES (?, ?)
''', sc_data)

conn.commit()

cursor.execute('''
    SELECT * FROM Students 
    WHERE age > 30
''')
print('Query: Students older than 30 years')
for row in cursor.fetchall():
    print(row)

cursor.execute('''
    SELECT *
    FROM Students s
    INNER JOIN StudentCourses sc ON s.id = sc.student_id
    INNER JOIN Courses c ON sc.course_id = c.id
    WHERE c.name = 'python'
''')
print('Query: Students attending Python course')
for row in cursor.fetchall():
    print(row)

cursor.execute('''
    SELECT *
    FROM Students s
    INNER JOIN StudentCourses sc ON s.id = sc.student_id
    INNER JOIN Courses c ON sc.course_id = c.id
    WHERE c.name = 'python' AND s.city = 'Spb'
''')
print('Query: Students attending Python course and from Spb')
for row in cursor.fetchall():
    print(row)

conn.close()
