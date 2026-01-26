                 #Even or Odd number
num =int(input("Even or Odd number:"))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


                   #Check positive, negative, or zero (if–elif–else)
num = float(input("Check positive, negative, or zero :"))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


                #Student pass or fail
marks =float(input("Enter Your marks :"))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

                 #Grade system example
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


                  #Biggest of two numbers
a = 10
b = 20

if a > b:
    print("A is greater")
else:
    print("B is greater")
                    

               #Login validation (real-life example)
username = "admin"
password =str(input("Enter a Password:"))

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


          