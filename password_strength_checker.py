import re

def check_password_strength(password):

    # Check if the password meets all strength criteria
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters."
    
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    
    if not re.search(r'[0-9]', password):
        return "Password should contain at least one digit."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character."

    return "Password is strong!"

print("\n----------Password Strength Checker----------\n")
password = input("Enter your password: ")
print(check_password_strength(password))


