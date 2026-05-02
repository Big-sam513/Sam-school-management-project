from .student_info import get_connection
import time


def view_student():

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT student_id, first_name, last_name, gender, admission_no, class_id FROM students")
        students = cursor.fetchall()

        if students:
            print("{:<10} {:<15} {:<15} {:<12} {:<15} {:<10}".format("student_id", "first_name", "last_name", "gender", "Admission_No", "class_id"))
            print("-" * 82)
            
            for s in students:
                print("{:<10} {:<15} {:<15} {:<12} {:<15} {:<10}".format(
                    s[0] if s[0] is not None else "N/A",
                    s[1] if s[1] is not None else "N/A",
                    s[2] if s[2] is not None else "N/A",
                    s[3] if s[3] is not None else "N/A",
                    s[4] if s[4] is not None else "N/A",
                    s[5] if s[5] is not None else "N/A"
                ))     

    except Exception as e:
        print("Failed", {e})

    cursor.close()
    conn.close()

    input("\nPress Enter to return to the Admin Dashboard...")

# view_student()



def student_title(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT first_name, last_name FROM students WHERE student_id = {student_id}
    """
    cursor.execute(query)
    student= cursor.fetchall()
    for s in student:
        first_name = s[0]
        last_name = s[1]
    
    return f"{first_name} {last_name}"
    # print(first_name, last_name)

# student_title()


def take_exam(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    name = student_title(student_id)
    query= f"""
    SELECT exam_id, exam_name, subject_id FROM cbt_exam
"""
    cursor.execute(query)
    exam = cursor.fetchall()

    if not exam:
        print("Exam not Available")
        return

    print("\n=========== Available Exams ==========")
    print("\n{:<10} {:<30} {:<20}".format("Exam_id", "Exam_title", "Subject"))
    print("-" * 60)

    for e in exam:
        exam_id = e[0]
        exam_name = e[1]
        subject_id = e[2]

        query = f"""
        SELECT subject_name FROM subject WHERE subject_id = {subject_id}
        """
        cursor.execute(query)
        subject_result = cursor.fetchone()
        subject_name = subject_result[0] if subject_result else "N/A"

        print("{:<10} {:<30} {:<20}".format(exam_id, exam_name, subject_name))

    exam_id = input("\nEnter Exam_id: ")

    query = f"""
    SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_option FROM question WHERE exam_id = {exam_id}
    """
    cursor.execute(query)
    question = cursor.fetchall()

    if not question:
        print("Questions not available")
        return

    # start_time = time.time()
    # duration
    score = 0
    total = len(question)

    
    print("\n===== EXAM STARTED ====")
    i = 0

    print("="*30)
    print("""
        EXAMINATION IN PROGRESS
    """)
    print("="*30)
    print(f"\n Student: {name}")



    print("""
            EXAM RULES — REMINDER:

     Do not close or exit this session mid-exam.

     Answers are auto-saved after each question.

     Skipped questions can be revisited before submitting.

     Session auto-submits when time runs out.
    """)
    time.sleep(2)
    for g in question:
        # g = question[1]

        print("\nQuestion", i + 1)
        print("------------------------------------------------------")
        print( g[1])
        print("A.", g[2])
        print("B.", g[3])
        print("C.", g[4])
        print("D.", g[5])

        print("Type A/B/C/D or type submit to finish exam: ")

        answer = input("\nEnter the correct answer: ").upper()

        if answer == "SUBMIT":
            print("\nExam Submitted")
            break

        query = f"""
        INSERT INTO student_answer(student_id, exam_id, question_id, selected_option)
        VALUES({student_id}, {exam_id}, {g[0]}, "{answer}")
        """
        cursor.execute(query)
        conn.commit()

        if answer == g[6]:
            score += 1

        
        i += 1
    time.sleep(3)    
    print("===============================================")
    print("\nFinal Score:", score, "/", total)
    print("===============================================")

    cursor.close()
    conn.close()

def view_results(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    print("\n====== MY RESULTS ======\n")

    try:
    
        cursor.execute(f"""
        SELECT DISTINCT exam_id FROM student_answer
        WHERE student_id = {student_id}
        """)
        exams = cursor.fetchall()

        if not exams:
            print("No results yet.")
            return

        for e in exams:
            exam_id = e[0]

            cursor.execute(f"""
            SELECT exam_name FROM cbt_exam WHERE exam_id = {exam_id}
            """)
            exam_name = cursor.fetchone()[0]

            cursor.execute(f"""
            SELECT COUNT(*) FROM question WHERE exam_id = {exam_id}
            """)
            total = cursor.fetchone()[0]

            cursor.execute(f"""
            SELECT COUNT(*) FROM student_answer sa
            JOIN question q ON sa.question_id = q.question_id
                WHERE sa.student_id = {student_id} AND sa.exam_id = {exam_id}
                AND sa.selected_option = q.correct_option
                """)
            score = cursor.fetchone()[0]

            print("Exam:", exam_name)
            print("Score:", score, "/", total)
            print("----------------------")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        conn.close()


    
    input("\nPress Enter to return to the Teacher Dashboard...")



def view_student_profile(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT first_name, last_name, gender, date_of_birth, class_id, parent_number, parent_name, admission_no FROM students WHERE student_id = {student_id}
    """
    cursor.execute(query)
    profile = cursor.fetchall()

    for p in profile:
        print("\n====== MY PROFILE =====")

        print("Personal Information")
        print("-"* 30)
        print("\nFirst Name:", p[0])
        print("Last Name:", p[1])
        print("Gender:", p[2])
        print("Date-of-birth:", p[3])
        print("Class_id:", p[4])
        print("Admission_Number:", p[7])

        print("\nParent/Guardian Informaation")
        print("-"*30)
        print("/nParent/Guardian Name:", p[6])
        print("Parent/Guardian Number:", p[5])

        cursor.close()
        conn.close()


        
    input("\nPress Enter to return to the Teacher Dashboard...")
