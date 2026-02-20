# import getpass

# def login_system():
#     correct_username = "admin"
#     correct_password = "123"

#     # Nested function for password validation
#     def verify_password():
#         for p_attempt in range(3):
#             pass_input = getpass.getpass(f"  Password Attempt {p_attempt+1}/3: ")
#             if pass_input == correct_password:
#                 return True
#         return False

#     # Main Username loop
#     for u_attempt in range(3):
#         print(f"\n--- [Attempt {u_attempt + 1}/3] ---")
#         user = input("Username: ")

#         if user == correct_username:
#             print("Username correct. Authenticating...")
            
#             # Yahan nested function call ho raha hai
#             if verify_password():
#                 print("Access Granted!")
#                 return
#             else:
#                 print("Access Denied: Password incorrect.")
#                 return # Password galat hone par system exit
#         else:
#             print("Invalid Username.")

#     print("\nSystem Locked: Too many failed attempts.")

# login_system()



def check_prime_range():
    print("--- Prime Number Finder (Nested Logic) ---")
    start = int(input("Start number: "))
    end = int(input("End number: "))

    print(f"\nPrime numbers between {start} and {end}:")

    # 1. Outer Loop: Range ke har number ke liye
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            
            # 2. Nested Loop: Divisibility check karne ke liye
            # Kisi number 'num' ko 2 se lekar 'num-1' tak divide karke dekhein
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False # Agar divide ho gaya, toh prime nahi hai
                    break # Loop tod do, agle number par jao
            
            if is_prime:
                print(f"{num} is a Prime Number")

# Program run
check_prime_range()