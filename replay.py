# from main import main

def replay():
    while True:
        replay = input("Did you want to perform a new operation(y/n): ").lower()
        if not replay == "y":
            continue
        else:
            break
            # main()