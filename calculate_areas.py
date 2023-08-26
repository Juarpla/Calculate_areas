"""
Student: Juan Plasencia
*Showing Creativity:
-With this application you can calculate the area of different geometric figures by entering the values of the variables used to measure the areas
"""
def compute_area_square(side):
    """That accepts a single value as a parameter, and then computes the area for the square and returns it."""
    area = side**2
    return area
def compute_area_rectangle(length, width):
    """It should pass the square side length to it (twice) and then return the value that the function computes"""
    area = length*width
    return area
def compute_area_circle(radio):
    """That accepts a single value as a parameter, and then computes the area for the circle and returns it."""
    area = 3.1415*(radio**2)
    return area

#A loop to ask the user what kind of shape they have, then prompt for the length of a side, or sides, or radius, 
#and then calls the appropriate function, and displays the result
quit = False
while quit == False:
    shape = input("\nWhat kind of shape do you have?\n(square/circle/rectangle): ").lower()
    if shape == "square":
        square_side = float(input("\nEnter the side of a square: "))
        result_square = round(compute_area_square(square_side),2)
        print(f"The area of the square is {result_square}")
        quit = True
    elif shape == "circle":
        circle_radio = float(input("\nEnter the radio of a circle: "))
        result_circle = round(compute_area_circle(circle_radio),2)
        print(f"The area of the cicle is {result_circle}")
        quit = True
    elif shape == "rectangle":
        rectangle_length = float(input("\nEnter the length of a rectangle: "))
        rectangle_width = float(input("Enter the width of a rectangle: "))
        result_rectangle = round(compute_area_rectangle(rectangle_length, rectangle_width),2)
        print(f"The area of the rectangle is {result_rectangle}")
        quit = True
    elif shape == "quit":
        quit = True
    else:
        print("If you want it, you can type 'quit' to exit")   
