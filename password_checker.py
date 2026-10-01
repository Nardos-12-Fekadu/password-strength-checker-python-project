from getpass import getpass

# List of allowed special characters
special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

while True:
    print("\n========== Password Strength Checker ==========")

    # Password is hidden while typing
    password = getpass("Enter your password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check all characters in one loop
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    print("\nChecking password...")

    valid = True

    # Check every requirement
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
        valid = False

    if not has_upper:
        print("❌ Password must contain at least one uppercase letter.")
        valid = False

    if not has_lower:
        print("❌ Password must contain at least one lowercase letter.")
        valid = False

    if not has_digit:
        print("❌ Password must contain at least one digit.")
        valid = False

    if not has_special:
        print("❌ Password must contain at least one special character.")
        valid = False

    # If every requirement is satisfied
    if valid:
        print("\n====================================")
        print("🎉 PASSWORD CREATED SUCCESSFULLY!")
        print("====================================")
        print("✅ Your password is STRONG.")
        print("🔒 It meets all security requirements.")
        print("\nRemember:")
        print("• Never share your password.")
        print("• Use a different password for every account.")
        print("• Store it safely or use a password manager.")
        print("\nThank you for using Password Strength Checker!")
        break

    # Ask again
    print("\n⚠️ Please try again.\n")