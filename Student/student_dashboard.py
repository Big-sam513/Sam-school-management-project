import time
from Student.student_list import student_title,take_exam,view_results, view_student_profile
from Student.student_info import get_connection
from utils import clear_screen, print_header, print_footer

def student_dashboard(student_id, class_id):
    conn = get_connection()
    cursor = conn.cursor()
    name = student_title(student_id)
    while True:
        print("\n  >> Opening Student Dashboard, please wait...")
        time.sleep(2)
        clear_screen()
        print_header()
        print()
        print(f"  Welcome back, {name}!")
        print("  You are logged in as Student.")
        print()
        print("  " + "-" * 46)
        print("  STUDENT DASHBOARD")
        print("  " + "-" * 46)
        print()
        print("  Access your academic information, track your")
        print("  progress, and stay on top of your studies.")
        print()
        print("  " + "-" * 46)
        print("  QUICK REMINDERS")
        print("  " + "-" * 46)
        print()
        print("    [*]  Check your class schedule for today.")
        print("    [*]  Review your latest results and scores.")
        print("    [*]  Take your CBT exams.")
        print("    [!]  Ensure your assignments are submitted.")
        print()
        print_footer()
        print()
        input("  >> Press Enter to continue to your menu: ")

        query = """
        SELECT class_name FROM classes WHERE class_id = %s
        """
        cursor.execute(query, (class_id,))
        class_name = cursor.fetchone()
        for c in class_name:
          print("="*15)
          print(f"Class: {c}")
          print("="*15)

        
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