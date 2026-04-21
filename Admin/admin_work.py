import time
from Student.student_info import get_connection


def manage_subject():
    conn = get_connection()
    cursor = conn.cursor()

    subject_name = input("Enter Subject: ")
    query = f"""
    INSERT INTO subject(subject_name) VALUES("{subject_name}")
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    print("-"*30)
    print("\nSubject Added Successfully...")

def view_subjects():
    conn =get_connection()
    cursor = conn.cursor()
    print("="*37)
    print("""
            MODULE: Subject Management
            ACTION: View Created Subjects
            FILTER: Created by you (Administrator)
        """)
    print("="*37)
    query = """
    SELECT subject_id, subject_name FROM subject
    """
    cursor.execute(query)
    subjects = cursor.fetchall()
    cursor.close()
    conn.close()

    if subjects:
        print("\n{:<10} {:<30}".format("Subject_ID", "Subject_Name"))
        print("-"*30)
        for subject in subjects:
            print("{:<10} {:<30}".format(subject[0], subject[1]))
    else:
        print("No subjects found in the database.")


def manage_exams():
    conn = get_connection()
    cursor = conn.cursor()
    print("="*45)
    print("""
            MODULE: Exam Management
            ACTION: Create New Exam
            LOGGED IN AS: Administrator
""")
    print("="*45)

    exam_type = input("\nExam Type(Test/Mid-term exam/Final exam): ")

    query = """
    SELECT subject_id,subject_name FROM subject
"""
    cursor.execute(query)
    sub = cursor.fetchall()
    print("\n======== Available Subjects ========")
    print("{:<15} {:<15}".format("\nSubject_id", "Subject_name"))
    print("-"*40)
    for s in sub:
        print("{:<10} {:<14}".format(
            s[0] if s[0] is not None else "N/A",
            s[1] if s[1] is not None else "N/A"
        ))

    subject_id = input("\nEnter Subject_id: ")
    minutes = input("Enter Duration Minutes: ")
    term = input("Enter Term: ")
    session = input("Enter Session: ")

    query = f"""
    INSERT INTO cbt_exam(exam_name,subject_id,duration_min,term,session)
    VALUES("{exam_type}","{subject_id}","{minutes}","{term}","{session}")

"""
    cursor.execute(query)
    conn.commit()
    time.sleep(2)
    print("\nExam Added Successfully")

# manage_exams()
# manage_subject()
# view_subjects()
    
