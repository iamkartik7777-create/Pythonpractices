# correct_username = "kartik"
# correct_password = "123"

# for i in range(3):
#     print(f"\n--- Login Attempt {i + 1} of 3 ---")
    
#     user_input = input("Enter Username: ")
#     pass_input = input("Enter Password: ")

#     if user_input == correct_username and pass_input == correct_password:
#         print("Login Successful! Welcome, Admin.")
#         break  
#     else:
#         print("Invalid details. Try again.")
        
# else:
    
#     print("\nAccount Locked! Aapne 3 galat attempts kiye hain.")



correct_username = "kartik"
correct_password = "123"

# Bahar wala loop (Outer Loop): Username check karne ke liye 3 chances
for u_attempt in range(3):
    print(f"\n--- [Username Attempt {u_attempt + 1}/3] ---")
    user_input = input("Enter Username: ")

    if user_input == correct_username:
        print("Username Correct!")
        
        # Andar wala loop (Nested Loop): Password ke liye 3 alag chances
        for p_attempt in range(3):
            print(f"--- [Password Attempt {p_attempt + 1}/3] ---")
            pass_input = input("Enter Password: ")

            if pass_input == correct_password:
                print("Login Successful. Welcome!")
                exit() # Poora program band karne ke liye (ya break use karein)
            else:
                print("Incorrect Password.")
        
        print("Password ke saare attempts khatam!")
        break # Password fail hone par wapis username par bhej dega

    else:
        print("Username not found.")

else:
    print("\nSorry, aapke saare chances khatam ho gaye hain.")