import re
import random
import string

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Too short (min 8 chars).")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Add number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add special character.")

    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def generate_strong_password(length=12):
    if length < 8:
        length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
