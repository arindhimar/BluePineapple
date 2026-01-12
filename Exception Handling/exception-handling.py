import re

def validate_id(temp_id):
    if temp_id == "":
        raise ValueError("ID cannot be empty!!")
    elif not isinstance(temp_id, int):
        raise ValueError("ID must be an integer")
    elif temp_id < 0:
        raise ValueError("ID cannot be negative")


def validate_name(temp_name):
    if temp_name == "":
        raise ValueError("Name cannot be empty!!")
    elif not re.match("^[a-zA-Z]+$", temp_name):
        raise ValueError("Name must contain only alphabets and spaces")


def validate_email(temp_email):
    if temp_email == "":
        raise ValueError("Email cannot be empty!!")
    elif not re.match("^[a-zA-z0-9]+[@]{1}[a-zA-Z]+[.]{1}[a-zA-Z]+$", temp_email):
        raise ValueError("Invalid Email!!")


def validate_age(temp_age):
    if temp_age == "":
        raise ValueError("Age cannot be empty!!")
    elif not isinstance(temp_age, int):
        raise ValueError("Age must be an integer")
    elif temp_age < 0:
        raise ValueError("Age cannot be negative")
    elif temp_age < 18:
        raise ValueError("Age must be at least 18")


def register_user():
    while True:
        try:
            user_id =int(input("Enter User ID : "))
            validate_id(user_id)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")
    
    while True:
        try:
            user_name = input("Enter Name : ")
            validate_name(user_name)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")
    
    while True:
        try:
            user_email = input("Enter Email: ")
            validate_email(user_email)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")
    
    while True:
        try:
            user_age = input("Enter Age : ")
            user_age = int(user_age)
            validate_age(user_age)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")
    
if __name__ == "__main__":
    try:
        register_user()
    except KeyboardInterrupt:
        print("Registration cancelled by user.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}")
