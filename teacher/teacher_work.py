# import pymysql as pm
from .teacher_info import teacher_title,fetch_subject
from Student.student_info import get_connection


def view_student(teacher_id):

    conn = get_connection()
    cursor = conn.cursor()
    name = teacher_title(teacher_id)
    subject = fetch_subject(teacher_id)
    print("="*35)
    print("""
                MODULE: Student Management
                ACTION: View My Students
            """)
    print(f"TEACHER: {name}")
    print(f"SUBJECT: {subject}")
    print("="*35)


    try:
        student_query = f"""
        SELECT class_id FROM teacher WHERE teacher_id = {teacher_id}
    """
        cursor.execute(student_query)
        result = cursor.fetchone()
        if result:
            class_id = result[0]

        query = f"""
        SELECT student_id, first_name, last_name, gender, date_of_birth, parent_number, address, parent_name, admission_no FROM students WHERE class_id = {class_id}
    """
        cursor.execute(query)
        student = cursor.fetchall()
        
        if student:
            print("{:<13} {:<15} {:<12} {:<12} {:<15} {:<15} {:<12} {:<13} {:<13}".format("\nstudent_id","First_name","Last_name","Gender","Date-of-birth","parent_number","Address","parent_name","Admission_No"))
            print("="*128)
            for s in student:
                print("{:<13} {:<15} {:<12} {:<12} {:<15} {:<15} {:<12} {:<13} {:<13}".format(
                    s[0] if s[0] is not None else "N/A",
                    s[1] if s[1] is not None else "N/A",
                    s[2] if s[2] is not None else "N/A",
                    s[3] if s[3] is not None else "N/A",
                    str(s[4]) if s[4] is not None else "N/A",
                    s[5] if s[5] is not None else "N/A",
                    s[6] if s[6] is not None else "N/A",
                    s[7] if s[7] is not None else 'N/A',
                    s[8] if s[8] is not None else "N/A"
                ))
        else:
            print("Student not found")
    except Exception as e:
        print("Student failed", e)
    finally:
        conn.close()
        cursor.close()
        # print(s)

# view_student()

def teacher_profile(teacher_id):
    conn =  get_connection()
    cursor = conn.cursor()

    teacher_query = f"""
    SELECT teacher_id, first_name, last_name, phone_number, email, Gender, Subject, class_id FROM teacher WHERE teacher_id = {teacher_id}
"""
    cursor.execute(teacher_query)
    profile = cursor.fetchone()

    if profile:
        print("="*40)
        print(f"ID: {profile[0]}")
        print(f"First Name: {profile[1]}")
        print(f"Last Name: {profile[2]}")
        print(f"Phone Number: {profile[3]}")
        print(f"Email Address: {profile[4]}")
        print(f"Gender: {profile[5]}")
        print(f"Subject : {profile[6]}")
        print(f"Class ID: {profile[7]}")
        print("="* 40)

    else:
        print("Teacher Profile not found.")

# teacher_profile()


def teacher_subject(teacher_id):
    
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT Subject FROM teacher WHERE teacher_id = {teacher_id}
"""
    cursor.execute(query)
    subject = cursor.fetchone()
    result = subject[0]

    if result:
        print("="*20)
        print(f"My Subject: {result}")
        print("="*20)
    else:
        print("Teacher Subject not found.")




def set_exam_questions(teacher_id):

    conn = get_connection()
    cursor = conn.cursor()

    print("\n====== SET EXAMS QUESTIONS ======")

    query = f"""
    SELECT Subject FROM teacher WHERE teacher_id = {teacher_id}
"""
    cursor.execute(query)
    teacher = cursor.fetchone()
    if not teacher:
        print("Subjects not Found.")
        return

    subject_name = teacher[0]

    query = f"""
    SELECT subject_id from subject WHERE subject_name = "{subject_name}"
"""
    
    cursor.execute(query)
    subject = cursor.fetchone()
    if not subject:
        print("Subject not found in the Database.")

    subject_id = subject[0]

    query = f"""
    SELECT exam_id, exam_name FROM cbt_exam WHERE subject_id = "{subject_id}"
    """
    cursor.execute(query)
    exam = cursor.fetchall()
    if not exam:
        print("Exam not found")
        return
    for e in exam:
        print(f"{e[0]} - {e[1]}")

    exam_id = input("Enter Exam ID: ")

    while True:
        print("====== ADD QUESTIONS ======")

        question = input("\nEnter Question: ")
        a = input("\nOption A: ")
        b = input("Option B: ")
        c = input("Option C: ")
        d = input("Option D: ")
        correct = input("Correct Answer (A/B/C/D): ").upper()

        if correct not in ["A","B","C","D"]:
            print("Invalid Answer.")
            continue


    
        query = f"""
        INSERT INTO question(question_text, exam_id, option_a, option_b, option_c, option_d, correct_option )
        VALUES("{question}","{exam_id}","{a}","{b}","{c}","{d}","{correct}")
    """
        cursor.execute(query)
        conn.commit()

        more = input("\nAdd more question (y/n): ").lower()
        if not more == "y":
            break







    # print(subject)
    
    # print(subject_name)



# set_exam_questions()
# teacher_subject()