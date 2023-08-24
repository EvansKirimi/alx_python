#!/usr/bin/python3
def validate_password(password):
    if len(password) >= 8:
        if ' ' in password:
            return False
        else:
            upper = False
            lower = False
            digit = False
            for char in password:
                if char.isupper():
                    upper = True
                elif char.islower():
                    lower = True
                elif char.isdigit():
                    digit = True
            if (upper and lower and digit):
                return True
            else:
                return False
                
    else:
        return False