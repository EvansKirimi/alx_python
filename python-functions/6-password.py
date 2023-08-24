#!/usr/bin/python3
def validate_password(password):
    if len(password) >= 8:
        if ' ' in password:
            return False
        else:
            for char in password:
                if char.isupper() or char.islower() and :
                    return True
                
    else:
        return False