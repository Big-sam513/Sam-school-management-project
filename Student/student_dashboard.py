import time
from Student.student_list import student_title,take_exam,view_results, view_student_profile
from Student.student_info import get_connection

def student_dashboard(student_id, class_id):
    conn = get_connection()
    cursor = conn.cursor()
    name = student_title(student_id)
    while True:
        print("\nOpening student dashboard...")
        time.sleep(3)

        print("="*40)
        print("""
            STUDENT DASHBOARD
        """)
        print("="*40)
        print(f"\nWelcome, {name}")

        query = """
        SELECT class_name FROM classes WHERE class_id = %s
        """
        cursor.execute(query, (class_id,))
        class_name = cursor.fetchone()
        for c in class_name:
          print(f"Class: {c}")

        
        print("""
                1. Take CBT Exam
                2. View My Results
                3. View My Profile
                4. Logout
        """)
        choice = input("Enter your Choice: ")

        if choice == "1":
           take_exam(student_id)
        elif choice == "2":
          view_results(student_id)
        elif choice == "3":
           view_student_profile(student_id)
        else:
          break


# student_dashboard()