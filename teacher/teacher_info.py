from Student.student_info import get_connection


def register_teacher():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n======================Personal Details=======================")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    gender = input("Enter Gender (Male/Female): ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    subject = input("\nEnter Subject: ")
    class_id = input("Enter Class ID: ")

    username = input("\nCreate Username: ")
    password = input("Create password: ")
    role = input("Enter role: ")

    teacher_query = """
    INSERT INTO teacher(first_name, last_name, Gender, phone_number, email, Subject, class_id)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
"""
    cursor.execute(teacher_query, (first_name, last_name, gender, phone_number, email, subject, class_id))
    teacher_id = cursor.lastrowid
    conn.commit()

    query = (
        "INSERT INTO user(username, password, role, teacher_id) "
        "VALUES (%s, %s, %s, %s)"
    )
    cursor.execute(query, (username, password, role, teacher_id))
    conn.commit()
    print("-"*20)
    print("\nTeacher Added Successful.")
    
    cursor.close()
    conn.close()


def fetch_subject(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT subject FROM teacher WHERE teacher_id = {teacher_id}
"""
    cursor.execute(query)
    subject = cursor.fetchone()

    for s in subject:
        return s
    
    cursor.close()
    conn.close()


def teacher_title(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT first_name, last_name, gender, subject, class_id FROM teacher WHERE teacher_id = %s"
    cursor.execute(query, (teacher_id,))
    teacher = cursor.fetchone()

    if not teacher:
        return "Unknown Teacher"

    first_name, last_name, gender, subject, class_id = teacher

    if gender and gender.lower() == "male":
        title = "Mr"
    elif gender and gender.lower() == "female":
        title = "Miss"
    else:
        title = "Mx"

    return f"{title} {first_name} {last_name}".strip()


