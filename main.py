from Student.student_info import get_connection
from Admin.admin_dashboard import admin
from teacher.teacher_dashboard import teacher_dashboard
from Student.student_dashboard import student_dashboard
from login import login


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


def main():
    while True:
        print("=" * 45)
        print("WELCOME TO SAM SCHOOL MANAGEMENT SYSTEM")
        print("=" * 45)
        print("\nWelcome to the School Administration Platform.")

        input("Press enter to continue: ")
        print("\nPlease select an option below: ")
        print("""\n
                    1. Login
                    2. Exit
    """)
        choice = input("Enter your choice:")
        if choice == "1":
            result = login()
            if not result:
                continue
            role, teacher_id, class_id,student_id = result
        if role == "Admin":
            admin()
        elif role == "teacher":
            teacher_dashboard(teacher_id, class_id)
        elif role == "student":
            student_dashboard(student_id, class_id)



        # replay = input("Did you want to perform a new operation? (y/n): ").lower()
        # if not replay == "y":
        #     break




main()