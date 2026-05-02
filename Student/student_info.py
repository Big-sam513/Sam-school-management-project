import pymysql as pm
import getpass
from utils import hash_password


def get_connection():
    return pm.connect(host='localhost', user='root', password='oluwaferanmi', database='school_management')


def first_name():
    while True:
        fname = input("\nEnter your First name: ").strip()
        if fname.isalpha():
            print('Name Verified...')
            return fname
        print('Invalid Credentials. Only letters allowed.')


def last_name():
    while True:
        lname = input("\nEnter your Last name: ").strip()
        if lname.isalpha():
            print('Name Verified...')
            return lname
        print('Invalid Credentials. Only letters allowed.')


def gender():
    while True:
        gen = input("\nEnter your gender (male/female): ").strip().lower()
        if gen in ('male', 'female'):
            print('Gender Verified..')
            return gen
        print('Invalid credentials. Enter male or female.')


def date_of_birth():
    while True:
        dob = input("\nEnter your Date of Birth (YYYY/MM/DD or DD/MM/YYYY): ").strip()
        if '/' in dob and len(dob) >= 8:
            print("Date of birth Verified...")
            return dob
        print("Invalid Credentials. Must include /.")


def address():
    while True:
        addr = input("\nEnter Home Address: ").strip()
        if addr:
            print("Address Verified")
            return addr
        print("Invalid Credentials. Address cannot be empty.")


def parent_name():
    while True:
        p_name = input("\nEnter Parent/Guardian Name: ").strip()
        if p_name.replace(' ', '').isalpha():
            print("Parent Name Verified.")
            return p_name
        print("Invalid Credentials. Use only letters and spaces.")


def parent_number():
    while True:
        p_num = input("\nEnter Parent/Guardian number (11 digits): ").strip()
        if p_num.isdigit() and len(p_num) == 11:
            print("Phone Number Verified.")
            return p_num
        print("Invalid Credentials. Provide exactly 11 digits.")


def select_class():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT class_id, class_name FROM classes")
    classes_list = cursor.fetchall()
    if not classes_list:
        print("No classes found in database.")
        return None

    print('\n===========Available Classes===========')
    for c in classes_list:
        print(f'{c[0]}. {c[1]}')

    while True:
        class_id = input('Enter the student class_id: ').strip()
        if class_id.isdigit() and any(str(c[0]) == class_id for c in classes_list):
            return int(class_id)
        print("Invalid class_id, please choose one from the list.")


def add_student():
    print("\nPlease enter the student details below.")
    print("Ensure that all information provided are accurate.")
    print("\nStudent Personal Information")
    print("-" * 40)

    f_name = first_name()
    l_name = last_name()
    gen = gender()
    dob = date_of_birth()
    addr = address()

    print("\nParent/Guardian information")
    print("-" * 40)
    p_name = parent_name()
    parent_num = parent_number()

    print("\nCreate login")
    print("-"*30)
    password = getpass.getpass("Create Password: ")
    password = hash_password(password)
    student_class_id = select_class()
    if student_class_id is None:
        print("Cannot add student without class selection.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    insert_query = (
        "INSERT INTO students (first_name, last_name, gender, date_of_birth, address, parent_name, parent_number, class_id) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(insert_query, (f_name, l_name, gen, dob, addr, p_name, parent_num, student_class_id))
    conn.commit()
    print("\nStudent record successfully added.")

    student_id = cursor.lastrowid
    # print(student_id)
    admission_no = (f"ADM{student_id:03}")
    # print(admission_no)

    update_query = (f"""
    UPDATE students
    SET admission_no = "{admission_no}" WHERE student_id = {student_id}             
                    
    """)
    cursor.execute(update_query)
    conn.commit()
    print("-"*30)
    print(f"Admission Number: {admission_no}")
    print("-"*30)



    query = "INSERT INTO user(username, password, role, student_id) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (admission_no, password, "Student", student_id))
    conn.commit()

    input("\nPress Enter to return to the Admin Dashboard...")


if __name__ == '__main__':
    try:
        add_student()
    except Exception as e:
        print('Student add failed:', str(e))

