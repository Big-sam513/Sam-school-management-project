import time
import getpass
from Student.student_info import get_connection
from utils import verify_password, input_password

def login():
    attempt = 0
    while attempt < 3:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            print("=================== USER LOGIN ======================")
            print("\nPlease enter your login credentials.")
            username = input("\nEnter your Username: ")
            password = input_password("Enter your password: ")
            print("\n---------------------------------------------")
            query = "SELECT password, role, teacher_id, student_id FROM user WHERE username=%s"
            cursor.execute(query,(username,))
            result = cursor.fetchone()
            if not result:
                print("Invalid Credentials")
                attempt += 1
                continue

            stored_password, role, teacher_id, student_id = result

            if not verify_password(stored_password, password):
                print("Invalid Credentials")
                attempt += 1
                continue

            class_id = None
            if role == "teacher" and teacher_id:
                cursor.execute("SELECT class_id FROM teacher WHERE teacher_id=%s", (teacher_id,))
                teacher_row = cursor.fetchone()
                if teacher_row:
                    class_id = teacher_row[0]
            elif role == "student" and student_id:
                cursor.execute("SELECT class_id FROM students WHERE student_id=%s", (student_id,))
                student_row = cursor.fetchone()
                if student_row:
                    class_id = student_row[0]

            if role:
                print("Authenticating user.....")
                time.sleep(3)
                print(f"Login Successful, Welcome {role}.")
                return role, teacher_id, class_id, student_id
            
            else:
                print("Invalid Credentials")
        except Exception:
            attempt += 1
            print(f"Invalid Credentials, You have {3-attempt} attempts remaining")
            continue
    
    else:
        print("Login Failed.")

# def replay():
#     while True:
#         replay = input("Did you want to perform a new operation(y/n): ").lower()
#         if not replay == "y":
#             break
#         else:
#             main()