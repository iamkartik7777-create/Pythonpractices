correct_username = "kartik"
correct_password = "123"

for i in range(3):
    print(f"\n--- Login Attempt {i + 1} of 3 ---")
    
    user_input = input("Enter Username: ")
    pass_input = input("Enter Password: ")

    if user_input == correct_username and pass_input == correct_password:
        print("Login Successful! Welcome, Admin.")
        break  
    else:
        print("Invalid details. Try again.")
        
else:
    
    print("\nAccount Locked! Aapne 3 galat attempts kiye hain.")