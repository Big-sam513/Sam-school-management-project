
import time
from Student.student_info import add_student
from Student.student_list import view_student
from teacher.teacher_info import register_teacher
from Admin.admin_work import manage_subject, view_subjects, manage_exams
from utils import clear_screen, print_header, print_footer



# add_student()
# def admin():
#     while True:
#         print("\nOpening Admin Dashboard....")
#         time.sleep(5)
#         print("="*40)
#         print(""" 

#                 ADMIN DASHBOARD""")
#         print("="*40)
#         print("Welcome Administrator,")
#         print('You can manage the school system using the options below.')

def admin():
    while True:
        clear_screen()
        print_header()
        print()
        print("\nOpening Admin Dashboard....")
        time.sleep(5)
        print(f"  Welcome back, Administrator!")
        print("  You are logged in as Administrator.")
        print()
        print("  " + "-" * 46)
        print("  Here is a quick overview of your system:")
        print("  " + "-" * 46)
        print()
        print("    [*]  All systems are running normally.")
        print("    [*]  Review any pending tasks below.")
        print("    [*]  Ensure all records are up to date.")
        print()
        print("  " + "-" * 46)
        print("  QUICK REMINDERS")
        print("  " + "-" * 46)
        print("    [!]  Check for unapproved teacher records.")
        print("    [!]  Review student enrollment updates.")
        print("    [!]  Confirm upcoming exam schedules.")
        print("    [!]  Create students exams. ")
        print()
        print_footer()
        print()

        print("""\n
                1. Add Student
                2. View Student
                3. Manage Teachers
                4. Add Subject
                5. View Subjects
                6. Create Exams
                7. Exit

        """)
        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            register_teacher()
        elif choice == "4":
            manage_subject()
        elif choice == "5":
            view_subjects()
        elif choice == "6":
            manage_exams()
        elif choice == "7":
            break

