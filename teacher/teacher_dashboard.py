import time
from .teacher_info import teacher_title
from .teacher_work import view_student, teacher_profile,teacher_subject,set_exam_questions
from replay import replay

def teacher_dashboard(teacher_id, class_id=None):
    name = teacher_title(teacher_id)
    while True:
        print("\nOpening Teachers Dashbord....")
        time.sleep(3)
        print("="*40)
        print("""
            TEACHER DASHBOARD
        """)
        print("="*40)
        print(f"\nWelcome, {name}")
        print("\nThis dashboard provides access to your classes, students records, attendance, and academic reports. \nStay organized and up to date.")

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