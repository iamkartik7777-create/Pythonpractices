# username = "admin"
# password = str(input("Enter yours Password :"))

# if username == "admin":
#     print("Username correct!")
    
#     # Nested If
#     if password == "123":
#         print("Login Successful. Welcome!")
#     else:
#         print("Wrong password. Try again.")

# else:
#     print("Username not found.")




correct_username = "kartik"
correct_password = "123"

while True:
    print("\n--- Login Page ---")
    user_input = input("Enter your Username enter : ")

    if user_input == correct_username:
        print("Username correct!")
        
        pass_input = input("Enter your Password enter : ")

        if pass_input == correct_password:
            print("Login Successful. Welcome, Admin!")
            break  
        else:
            print("Wrong password. Please try again.")

    else:
        print("Username not found. Please register or try again.")