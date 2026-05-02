from Student.student_info import get_connection
from teacher.teacher_dashboard import teacher_dashboard
from Student.student_dashboard import student_dashboard
from Admin.admin_dashboard import admin
from login import login
import os
# import sys
import io
from datetime import datetime
from utils import clear_screen, print_header, print_footer


def default_admin():
    conn = get_connection()

    cursor = conn.cursor()

#     cursor.execute("""
#     INSERT INTO user(username, password, role)
#     VALUES('schooladmin123','admin123','Admin');
                   
#     """)

#     query = """
#     SELECT role FROM user WHERE username = %s AND password = %s
# """
    cursor.execute("SELECT * FROM user WHERE username = 'schooladmin123'")
    admin = cursor.fetchone()
    role = admin[3]

    if not admin:
        cursor.execute("""
#     INSERT INTO user(username, password, role)
#     VALUES('schooladmin123','admin123','Admin');
                   
#     """)
        conn.commit()
    else:
        print(f"Login successful, Welcome {role}")








def main_menu():
    while True:
        clear_screen()
        print_header()
        print()
        print("  Welcome! Please log in to access your")
        print("  personalised dashboard.")
        print()
        print("  Dashboards available for:")
        print("      Administrators   — Manage school data")
        print("      Teachers         — Classes & grading")
        print("      Students         — Results & schedules")
        print()
        print("  ─────────────────────────────────────────")
        print("    [1]  Login to your account")
        print("    [2]  Exit")
        print("  ─────────────────────────────────────────")
        print_footer()
        print()


# def main():
#     while True:
#         os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
#         print("=" * 60)
#         print("          WELCOME TO SAM SCHOOL MANAGEMENT SYSTEM")
#         print("=" * 60)
#         print("\nWelcome to the School Administration Platform.")
#         print("Manage students, teachers, exams, and more with ease.\n")

#         input("Press Enter to continue...")

#         print("\n" + "=" * 40)
        # print("Please select an option below:")
        # print("=" * 40)
        # print("1. Login")
        # print("2. Exit")
        # print("-" * 40)

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            result = login()
            if not result:
                print("\nLogin failed. Please try again.")
                input("Press Enter to continue...")
                continue
            role, teacher_id, class_id, student_id = result

            # Clear screen before entering dashboard
            os.system('cls' if os.name == 'nt' else 'clear')

            if role == "Admin":
                admin()
            elif role == "teacher":
                teacher_dashboard(teacher_id, class_id)
            elif role == "student":
                student_dashboard(student_id, class_id)

            # After dashboard, ask to return to main menu or exit
            print("\n" + "=" * 50)
            replay = input("Return to main menu? (y/n): ").lower().strip()
            if replay != "y":
                print("Thank you for using SAM School Management System. Goodbye!")
                break

        elif choice == "2":
            print("\nThank you for using SAM School Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1 or 2.")
            input("Press Enter to continue...")




main_menu()