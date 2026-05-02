import time
from .teacher_info import teacher_title
from .teacher_work import view_student, teacher_profile,teacher_subject,set_exam_questions
from replay import replay
from utils import clear_screen,print_header,print_footer

def teacher_dashboard(teacher_id, class_id=None):
    name = teacher_title(teacher_id)
    while True:
        print("\n  >> Opening Teacher Dashboard, please wait...")
        time.sleep(2)
        clear_screen()
        print_header()
        print()
        print(f"  Welcome back, {name}!")
        print("  You are logged in as Teacher.")
        print()
        print("  " + "-" * 46)
        print("  TEACHER DASHBOARD")
        print("  " + "-" * 46)
        print()
        print("  This dashboard gives you access to everything")
        print("  you need to manage your classes effectively.")
        print()
        print("  " + "-" * 46)
        print("  QUICK REMINDERS")
        print("  " + "-" * 46)
        print()
        print("    [*]  Review your class schedule for today.")
        print("    [*]  Set exam questions for all active subjects.")
        print("    [*]  Update student scores and assessments.")
        print("    [!]  Ensure academic reports are up to date.")
        print()
        print_footer()
        print()
        input("  >> Press Enter to continue to your menu: ")

        print("""
            1. View My Students
            2. View My Profile
            3. View My Subjects
            4. Enter Students Scores
            5. Set Exam Questions
            6. Back.
    """)
        choice = input("Enter your choice: ")

        if choice == "1":
            view_student(teacher_id)
        elif choice == "2":
            teacher_profile(teacher_id)
        elif choice == "3":
            teacher_subject(teacher_id)
        elif choice == "5":
            set_exam_questions(teacher_id)
        elif choice == "6":
            break

# teacher_dashboard()