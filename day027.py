import getpass

def login_system():
    correct_username = "admin"
    correct_password = "123"

    # Nested function for password validation
    def verify_password():
        for p_attempt in range(3):
            pass_input = getpass.getpass(f"  Password Attempt {p_attempt+1}/3: ")
            if pass_input == correct_password:
                return True
        return False

    # Main Username loop
    for u_attempt in range(3):
        print(f"\n--- [Attempt {u_attempt + 1}/3] ---")
        user = input("Username: ")

        if user == correct_username:
            print("Username correct. Authenticating...")
            
            # Yahan nested function call ho raha hai
            if verify_password():
                print("Access Granted!")
                return
            else:
                print("Access Denied: Password incorrect.")
                return # Password galat hone par system exit
        else:
            print("Invalid Username.")

    print("\nSystem Locked: Too many failed attempts.")

login_system()