# School Management System

A Python-based school management system with three roles: Administrator, Teacher, and Student.

# Overview

This system manages students, teachers, subjects, CBT exams, and results through a console interface.
Users authenticate with credentials in the `user` table and are directed to role-specific dashboards.

- `login.py`: validates credentials and identifies user role.
- `main.py`: application entry point and dashboard router.
- `database.py`: database connection helper.
- `Admin/`: admin dashboard and admin actions.
- `teacher/`: teacher dashboard and teacher actions.
- `Student/`: student dashboard and exam actions.

# How the System Works

# Login Flow

Users sign in with a username and password. The system checks the `user` table, returns the role, and loads any linked teacher or student record.
After login, the user is routed based on role:

- `Admin` -> admin dashboard.
- `teacher` -> teacher dashboard.
- `student` -> student dashboard.

# Role Capabilities

# Administrator

The admin dashboard lets the administrator manage core school records and exam setup:

- Add new student records with personal, guardian, and class data.
- View all students in the database.
- Register teachers and assign them a subject and class.
- Add new subjects to the system.
- View existing subjects.
- Create CBT exams and assign them to a subject.
	- exam name/type
	- subject association
	- duration in minutes
	- term and session

# Teacher

Teachers can manage students in their assigned class and add exam questions:

- View students assigned to their class.
- View their own teacher profile.
- View the teacher's assigned subject.
- Set exam questions for existing exams in their subject.
	- enter a question prompt
	- enter options A, B, C, D
	- select the correct answer

# Student

Students use the student dashboard to take exams and check their results:

- Take CBT exams from the available exam list.
- See each exam title with its related subject name.
- Answer multiple-choice questions and submit the exam.
- View result summaries and scores for completed exams.
- View their own profile and class information.

# Project Structure

- `database.py` - database connection helper.
- `login.py` - authentication and role routing.
- `main.py` - entry point and dashboard router.
- `replay.py` - optional replay or workflow helper.
- `Admin/admin_dashboard.py` - admin menu and dashboard.
- `Admin/admin_work.py` - admin functions for subjects and exams.
- `teacher/teacher_dashboard.py` - teacher menu.
- `teacher/teacher_info.py` - teacher registration and lookup.
- `teacher/teacher_work.py` - teacher actions and exam question entry.
- `Student/student_dashboard.py` - student menu.
- `Student/student_info.py` - student registration and helper functions.
- `Student/student_list.py` - exam listing, exam taking, and results.

# Setup

1. Install Python 3.x.
2. Place the project folder in a convenient location.
3. Configure the database connection in `database.py`.
4. Ensure the following tables exist: `user`, `students`, `teacher`, `subject`, `cbt_exam`, `question`, `student_answer`, `classes`.
5. Run the application from the project root:

```powershell
python main.py
```

# Notes

- Student exam listings now include the subject name beside each exam title.
- Teacher-entered questions are stored in `question`.
- Student answers are stored in `student_answer`.
- Admin exam creation stores metadata in `cbt_exam`.


