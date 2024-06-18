import re

def check_password_strength(password):
    if re.match(r"^(?=.*[A-Z])(?=.*[a.z])(?=.*\d)(?=.*[@$!%*&?])[A-Za-z\d@$!%*&?]{8,}$" , password):
        return "Strong"
    elif re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$",password):
        return "Moderate"
    else:
        return "Weak"
    
password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")