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



