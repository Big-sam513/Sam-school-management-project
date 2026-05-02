import os
from datetime import datetime
import hashlib
import sys

if os.name == 'nt':
    import msvcrt
# else:
#     import tty
#     import termios

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    width = 50
    now = datetime.now().strftime("\n%A, %d %B %Y  |  %I:%M %p")
    print("-" * width)
    print("     SAM SCHOOL MANAGEMENT SYSTEM  ")
    print("-" * width)
    print(f"   {now}")
    print("-" * width)

def print_footer():
    width = 50
    print("-" * width)
    print("  ℹ️  For support, contact: admin@samschool.edu")
    print("=" * width)


def hash_password(password):
    """Return a SHA-256 hash for a password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def verify_password(stored_password, provided_password):
    """Verify by comparing stored password or stored hash."""
    if stored_password == provided_password:
        return True
    return stored_password == hash_password(provided_password)


def input_password(prompt="Password: "):
    """Read a password from terminal, masking each character with '*'"""
    if os.name == 'nt':
        print(prompt, end='', flush=True)
        password_chars = []
        while True:
            ch = msvcrt.getwch()
            if ch in ('\r', '\n'):
                print('')
                break
            if ch == '\x03':
                raise KeyboardInterrupt
            if ch in ('\b', '\x7f'):
                if password_chars:
                    password_chars.pop()
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                continue
            if ch in ('\x00', '\xe0'):
                msvcrt.getwch()
                continue
            password_chars.append(ch)
            sys.stdout.write('*')
            sys.stdout.flush()
        return ''.join(password_chars)
    try:
        import getpass
        return getpass.getpass(prompt)
    except Exception:
        return input(prompt)