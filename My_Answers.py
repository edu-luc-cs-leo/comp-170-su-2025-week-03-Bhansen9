

"""Diamond shape

Write a function `draw_diamond` that draws a diamond shape of a specified height"""

def Diamond_shape():
    N = int(input("How tall should the Diamond shape be: "))
    second_line_amounts = N * 0.6
    first_line_amounts = int(N * 0.33)
    middle_line_spaces_amount = (N - second_line_amounts) / 2
    end_line_spaces_amount = (N - first_line_amounts) / 2
    for i in range(int(N/5)):
        print(" " * int(end_line_spaces_amount) + "#" * int(first_line_amounts) + " " * int(end_line_spaces_amount))
    for i in range(int(N/5)):
        print(" " * int(middle_line_spaces_amount) + "#" * int(second_line_amounts) + " " * int(middle_line_spaces_amount))
    for i in range(int(N/5)):
        print("#"* N)
    for i in range(int(N/5)):
        print(" " * int(middle_line_spaces_amount) + "#" * int(second_line_amounts) + " " * int(middle_line_spaces_amount))
    for i in range(int(N/5)):
        print(" " * int(end_line_spaces_amount) + "#" * int(first_line_amounts) + " " * int(end_line_spaces_amount))
#Diamond_shape()


"""## Right triangle

Write a function `draw_right_triangle` that draws a right angle triangle whose height is specified as a parameter to the function."""

def right_triangle(height):
    count = height
    limit = 1
    while count > 0:
        print(" #"* limit)
        limit  += 1
        count -= 1
#right_triangle(9)

""" Compound interest

Write a function `compound_interst` that computes the compound interest for a given amount, a given annual interest rate, and a given period of time. 
For example, over a 5 year period, an initial investment of $1,000, earning 5% interest will accumulate as follows:
"""
def compound_int():
    start_amount = 1000
    interest_per_year = 0.05
    time_for_compounding = 5
    time_gone_by = 0
    while time_for_compounding > 0:
        start_amount = start_amount + start_amount * interest_per_year

        time_for_compounding -= 1
        time_gone_by += 1
        print(f"{time_gone_by}st year with {interest_per_year} interest per year: ${start_amount}")
# compound_int()

"""## Hollow square 

Write a function `draw_hollow_square` that draws a square that is empty in the middle. The size of the square's and the thickness of its edge should be given as parameters. 
For example `draw_hollow_square(8,2)` should produce the following drawing:"""

def Hollow_Square(size,edge_remainder):
    hole_size = size - edge_remainder * 2
    print(hole_size)
    for i in range(int(size / 4)):
        print( "#" * size)
    for i in range(int(size / 2)):
        print("#"* edge_remainder + " "* hole_size + "#"* edge_remainder )
    for i in range(int(size / 4)):
        print( "#" * size)
#Hollow_Square(8,2)

# relfection

"""When looking between the code that I sent in for week 2 and the answers I see a lot of similarities. 
I think all my answers are correct and display the right outcomes but obviously it's not gonna be the same code. 
There are definitely a lot of simplair steps I could have taken like in the solutions for the greeting. They use the list while I use a dictionary. 
This is a key change that may lead to more steps in my code. Although they both could lead to the same outcomes just one has a few more steps. 
I think overall I did good making the code lead to the right outcomes but there are some things I can change when it comes to putting together functions like this in the future. 
I think a list in the future would be a big help in being able to store data easier than a dictions especially in bigger datasets."""


















