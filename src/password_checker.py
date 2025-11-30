

import re

def check_password_strength(password: str) -> bool:
    pw_length = False
    pw_uppercase = False
    pw_lowercase = False
    pw_digit = False
    pw_special_char = False

    # Check password criteria
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d',password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False    
    return True




 

def get_password_feedback(password: str) -> dict:
    feedback = {
        "length" : len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)), 
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    }
    missing_criteria = []
    if not feedback["length"]:
        missing_criteria.append("at least 8 characters long")
    if not feedback["uppercase"]:
        missing_criteria.append("at least one uppercase letter")
    if not feedback["lowercase"]:
        missing_criteria.append("at least one lowercase letter")
    if not feedback["digit"]:
        missing_criteria.append("at least one digit")
    if not feedback["special_char"]:
        missing_criteria.append("at least one special character")
    
    return {
        'is_strong': all(feedback.values()),
        'missing_criteria': missing_criteria,
        'detailed_feedback': feedback

    }
