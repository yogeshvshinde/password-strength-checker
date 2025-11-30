from src.password_checker import check_password_strength, get_password_feedback
def print_welcome_message():
    print("Welcome to the Password Strength Checker!")

def print_feedback_message():
    print("This tool will help you evaluate the strength of your password based on several criteria.")
    print("A strong password should be at least 8 characters long and include:")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character (e.g., !, @, #, etc.)")
    print()

def display_feedback(password: str):
    feedback = get_password_feedback(password)
    if feedback['is_strong']:
        print("Your password is strong!")
    else:
        print("Your password is weak. It is missing the following criteria:")
        for criterion in feedback['missing_criteria']:
            print(f"- {criterion}")
    print("\nDetailed Feedback:")
    for key, value in feedback['detailed_feedback'].items():
        status = "Met" if value else "Not Met"
        print(f"{key.capitalize()}: {status}")

def main():
    print_welcome_message()
    print_feedback_message()
    
    while True:
        password = input("Please enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Thank you for using the Password Strength Checker. Goodbye!")
            break
        display_feedback(password)
        print()

if __name__ == "__main__":
    main()
    