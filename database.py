import pymysql as pm

def connection():
    return pm.connect(host='localhost', user='root',password='oluwaferanmi')
print(connection())
print("connection successful")

def create_database():
    """create school management database"""
    try:
        conn = pm.connect(host='localhost', user='root', password='oluwaferanmi')
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTs school_management")
        print("Database created.")
       

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database {e}")
        return False
# print(create_database())   

def create_table():
    """creating all the tables in the database"""
    conn = pm.connect(host='localhost', user='root', password='oluwaferanmi', database='school_management')
    
    cursor = conn.cursor()
    

# print(create_table())

    # Table 1
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) UNIQUE NOT NULL,
    role ENUM('Admin','teacher','student')
    )
                   
""")
    
    query = """
    ALTER TABLE user
    ADD COLUMN teacher_id INT NULL,
    ADD COLUMN student_id INT NULL
"""
    # cursor.execute(query)
    print("Alt")


    # cursor.execute("""
    # INSERT INTO user(username, password, role)
    # VALUES('schooladmin123','admin123','Admin');
                   
    # """)
    # print("Table Users created successfully.")

    # TABLE 2:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender ENUM('Male','Female'),
    date_of_birth DATE,
    class_id INT,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(100),
    FOREIGN KEY(class_id) REFERENCES classes(class_id)
    
    )
""")
    # print("Table Student created successfully.")
    query ="""ALTER TABLE students
    ADD COLUMN parent_name VARCHAR(50) NOT NULL,
    ADD COLUMN admission_no VARCHAR(20) UNIQUE
    """
    # cursor.execute(query)
    print("Altered")

    query = """
    ALTER table students
    RENAME column phone_number TO parent_number

    """
    # cursor.execute(query)
    # conn.commit()
    # print("Renamed")

    # TABLE 3:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher(
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

""")
    
    query = """ALTER TABLE teacher
    ADD COLUMN Gender Enum('Male','Female'),
    ADD COLUMN Subject VARCHAR(50) NOT NULL,
    
    """
    # cursor.execute(query)
    print("ADDED SU")

    query = """
    ALTER TABLE teacher
    ADD COLUMN class_id INT NOT NULL
    """
    # cursor.execute(query)
    print("DDD")


    # print("Table teacher created successfully.")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes(
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(50) NOT NULL,
    class_teacher VARCHAR(50)              
    )    
""")
    query= "ALTER TABLE classes DROP COLUMN class_teacher"
    # cursor.execute(query)
    print("Dropped")
    # print("Table classes created successfully.")

    query= """
    INSERT INTO classes (class_name)
    VALUES
    ('JSS1'),
    ('JSS2'),
    ('JSS3'),
    ('SSS1'),
    ('SSS2'),
    ('SSS3')
    
    """
    # cursor.execute(query)
    print("Added")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subject(
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50)              
    )    
""")
    # print("Table subject created successfully.")

    query = """
    ALTER TABLE cbt_exam 
    ADD COLUMN subject_name VARCHAR(30) NOT NULL
    """
    # cursor.execute(query)
    print("ALT")

    query = """
    ALTER TABLE cbt_exam
    DROP COLUMN subject_name
"""
    # cursor.execute(query)
    print("DDR")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher_subject(
    teacher_subject_id  INT PRIMARY KEY UNIQUE,
    teacher_id INT,     
    subject_id INT,
    class_id INT         
    )
""")
    # print("Table teacher_subject created successfully.")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS result(
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    score INT NOT NULL,
    grade VARCHAR(2) NOT NULL,
    term VARCHAR(20) NOT NULL,
    session VARCHAR(20) NOT NULL,   
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP           
    )
""")
    # print("Table results created successfully.")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,              
    student_id INT NOT NULL,
    attendance_date DATE,
    status ENUM('Present','Absent'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )   
    
""")
    # print("Table Attendance created Successfully.")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cbt_exam(
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_name VARCHAR(100) NOT NULL,
    subject_id INT,
    duration_min INT,
    term VARCHAR(50) NOT NULL,
    session VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP              
    )
    
""")
    # print("Table cbt_exams created successfully.")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS question(
    question_id INT PRIMARY KEY AUTO_INCREMENT,
    question_text TEXT,
    exam_id INT,
    option_a VARCHAR(100),
    option_b VARCHAR(100),
    option_c VARCHAR(100),
    option_d VARCHAR(100),
    correct_option ENUM('A','B','C','D')  
    )
    
    """)
    # print("Table Questions created successfully.")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_answer(
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    exam_id INT,
    question_id INT,
    selected_option ENUM('A','B','C','D')
    )
    """)
    # print("Answers")
create_table()