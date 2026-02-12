# import turtle
# import colorsys


# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.speed(0) 

# n = 36 
# h = 0  

# for i in range(400):
    
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 1/n
#     t.color(c)
    
#     t.forward(i * 2)
#     t.left(145) 
#     t.width(i/100)

# turtle.done()

def welcome(city="India"):
    print("Welcome to", city)

welcome("Mumbai") # Output: Welcome to Mumbai
welcome()         # Output: Welcome to India