# num=float(input("Enter your marks :"))
# if num >= 40:
#     print("YOU ARE PASSED ",(num))
# else:
#     print("YOU ARE FAIL",(num))

num = int(input("ENTER YOUR NO. :"))
if num == 1 :
    print(1)
elif num == 1 :
    print( 1 )

#Q1
num=300
num2=50
num3=90

if num>num2 and num>num3:
    print("num is largest")
elif num2>num and num2>num3:
    print("num2 is largest")
else:
    print("num3 is largest")

#Q2
marks=int(input("Enter your marks"))
if marks>=80 and marks<=100:
    print("A Grade")
elif marks>=60 and marks<80:
    print("B Grade")
elif marks>=30 and marks<60:
    print("C Grade")
elif marks>=0 and marks<30:
    print("D Grade")
else:
    print("Invlid Input")


#Q3 Input income and calculate tax:
# • ≤2,50,000 → No tax.
# • 2,50,001 – 5,00,000 → 5% tax.
# • 5,00,001 – 10,00,000 → 20% tax.
# • Above 10,00,000 → 30% tax.
income=int(input("Enter your income: "))
if income<250000:
    print("no tax ")
elif income>=250000 and income<500000:
    print(int(income(0.05)))
elif income>=500000 and income<1000000:
    print(int(income(0.2)))
elif income>=1000000:
    print(income(0.3))
income = float(input("Enter your annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Income:", income)
print("Tax to be paid:", tax)

# 4 Input time in 24-hour format and display:
# • If time < 12 → "Good Morning".
# • If 12–17 → "Good Afternoon".
# • If 18–20 → "Good Evening".
# • Else → "Good Night".    
# Function to get input and handle the greeting logic

def time_greeting_strict():
    # Input time from the user
    time_str = input("Enter the current hour (0-23): ")
    current_hour = int(time_str) # Conversion to Integer is required for comparison

    # Check for Good Morning (0 to 11)
    if current_hour >= 0 and current_hour < 12:
        print("Good Morning")
    
    # Check for Good Afternoon (12 to 17)
    else: # If it's not Morning (i.e., time is 12 or greater)
        if current_hour >= 12 and current_hour <= 17:
            print("Good Afternoon")
        
        
        else: 
            if current_hour >= 18 and current_hour <= 20:
                print("Good Evening")
            
            else: 
                print("Good Night")


#Q5  Weeks days
day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")




