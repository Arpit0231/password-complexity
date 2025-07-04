import re

def assess_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r'[A-Z]', password)
    lowercase_error = not re.search(r'[a-z]', password)
    digit_error = not re.search(r'\d', password)
    special_char_error = not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Moderate ⚠️"
    elif score == 2:
        strength = "Weak ❌"
    else:
        strength = "Very Weak 🔓"

    # Detailed feedback
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters long.")
    if uppercase_error:
        feedback.append("Include at least one uppercase letter.")
    if lowercase_error:
        feedback.append("Include at least one lowercase letter.")
    if digit_error:
        feedback.append("Include at least one number.")
    if special_char_error:
        feedback.append("Include at least one special character (!@#$%^&* etc.)")

    return strength, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f" - {item}")
    else:
        print("✅ Your password meets all recommended criteria!")

if __name__ == "__main__":
    main()
