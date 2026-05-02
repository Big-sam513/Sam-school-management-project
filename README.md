
# SAM School Management System

A terminal-based School Management System built with Python that provides
role-based access for Administrators, Teachers, and Students. Each role 
has a dedicated dashboard tailored to their specific needs and 
responsibilities within the school.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Roles & Dashboards](#roles--dashboards)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [Author](#author)

---

## Overview

SAM School Management System is a command-line application designed to 
simplify the day-to-day management of a school. It provides a clean and 
interactive terminal interface where users can log in based on their role 
and access only the features relevant to them.

The system is built entirely in Python and runs in any terminal environment,
making it lightweight, fast, and easy to use without the need for a 
graphical interface or internet connection.

---

## Features

### General
- Clean and interactive terminal interface
- Role-based login system with secure password masking
- Personalised dashboards for each role
- Real-time date and time display on every screen
- Consistent navigation across all menus

### Administrator
- Add, view, update, and remove student records
- Add, view, update, and remove teacher records
- Manage classes and assign teachers and students
- Create and assign subjects
- View school-wide attendance logs
- View exam results and assessment records
- Generate and export academic reports
- Manage account settings and password

### Teacher
- View assigned classes and subject schedule
- Mark and manage student attendance
- Record and update student scores and assessments
- View academic reports for their classes
- Manage account settings and password

### Student
- View personal class schedule
- Check attendance records
- View exam results and assessment scores
- Track academic progress
- Manage account settings and password

---

## Project Structure
Sam_Management/
│
├── Admin/
│   ├── init.py
│   └── admin_dashboard.py       # Admin dashboard logic and display
│
├── Teacher/
│   ├── init.py
│   └── teacher_dashboard.py     # Teacher dashboard logic and display
│
├── Student/
│   ├── init.py
│   └── student_dashboard.py     # Student dashboard logic and display
│
├── main.py                      # Entry point -- main menu and login
└── README.md                    # Project documentation


---

## How It Works

1. The system starts at the **Main Menu** where the user is welcomed and 
   prompted to log in.

2. The user enters their **username and password**. The password is masked 
   with `*` characters for security as each character is typed.

3. The system **verifies the credentials** and identifies the user's role 
   (Administrator, Teacher, or Student).

4. Based on the role, the user is redirected to their **dedicated dashboard** 
   which displays a personalised welcome message and quick reminders.

5. From the dashboard, the user can navigate to the features available to 
   their role using numbered menu options.

6. The user can **log out** at any time and return to the main menu, or 
   exit the system entirely.

---

## Roles & Dashboards

### [A] Administrator
The Administrator has the highest level of access in the system. They are 
responsible for managing all school data including students, teachers, 
classes, subjects, attendance, and academic reports. The admin dashboard 
provides a full overview of the school system and flags pending tasks that 
require attention.

### [T] Teacher
Teachers have access to features related to their assigned classes. They 
can mark attendance, record student scores, and view academic reports for 
their students. The teacher dashboard displays a summary of their 
responsibilities and reminds them of pending tasks such as unmarked 
attendance or unsubmitted reports.

### [S] Student
Students have a read-focused dashboard where they can view their personal 
academic information including their schedule, attendance record, and exam 
results. The student dashboard encourages them to stay on top of their 
studies.

---

## How to Run

### Step 1 -- Clone the repository
```bash
git clone https://github.com/Big-sam513/Sam-school-management-project.git
```

### Step 2 -- Navigate to the project folder
```bash
cd Sam-school-management-project
```

### Step 3 -- Run the application
```bash
python main.py
```

> Recommended: Run using **Anaconda Prompt** for the best terminal 
> display experience.

---

## Requirements

- Python 3.x
- Anaconda (recommended)
- No external libraries required -- uses Python standard library only

### Standard Libraries Used
- `os` -- screen clearing and OS detection
- `sys` -- system exit and stdout control
- `time` -- loading delays and transitions
- `datetime` -- real-time date and time display
- `msvcrt` -- secure password masking on Windows
- `getpass` -- secure password masking on Unix/macOS

---

## Author

**Big-sam513**
GitHub: [https://github.com/Big-sam513](https://github.com/Big-sam513)

---

## License

This project is open source and available for educational purposes.


