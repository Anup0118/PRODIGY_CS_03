import re
def assess_password_complexity(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[^\w\s]', password))

    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_criteria
    ])

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include atleast one uppercase letters.")
    if not lowercase_criteria:
        feedback.append("Password should include atleast one lowercase letters.")
    if not digit_criteria:
        feedback.append("Password should include atleast one digit.")
    if not special_criteria:
        feedback.append("Password should include atleast one special characters.")

    if strength_score == 5:
        feedback.append("Your password is very strong.")
    elif 3 <= strength_score <5:
        feedback.append("Your password is strong, but could be improved.")
    else:
        feedback.append("Your password is weak. Consider improving it by following the recomendations.")

    return feedback

def main():
    password = input("Enter a password to assess its complexity: ")
    feedback = assess_password_complexity(password)
    print("\nPassword Strength Assessment: ")
    for comment in feedback:
        print(f"- {comment}")

if __name__ == "__main__":
    main()