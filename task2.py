passwords = [
    "Hello123!",
    "hello",
    "HELLO123!",
    "Hello111!",
    "Admin@123",
    "GoodPass@45"
]

prohibited = ["admin", "password", "123456"]
special_chars = "!@#$%^&*"

for password in passwords:
    errors = []

    if len(password) < 8:
        errors.append("Minimum length must be 8 characters")

    if not any(c.isupper() for c in password):
        errors.append("Missing uppercase letter")

    if not any(c.islower() for c in password):
        errors.append("Missing lowercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Missing digit")

    if not any(c in special_chars for c in password):
        errors.append("Missing special character")

    if any(password[i] == password[i + 1]
           for i in range(len(password) - 1)):
        errors.append("Contains consecutive repeated characters")

    if any(word in password.lower() for word in prohibited):
        errors.append("Contains a prohibited substring")

    print("\nPassword:", password)

    if errors:
        print("Invalid password")
        for error in errors:
            print("-", error)
    else:
        print("Valid password")