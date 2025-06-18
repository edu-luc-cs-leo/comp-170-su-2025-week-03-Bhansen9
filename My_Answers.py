




"""Diamond shape

Write a function `draw_diamond` that draws a diamond shape of a specified height"""

def Diamond_shape():
    N = input("How tall should the Diamond shape be: ")


    Aspect_ratio = 1
    first_line_proportion = 0.2
    second_line_proportion = 0.2
    middle_line_porportion = 0.2
    fourth_line_porportion = 0.2
    fifth_line_proportion = 0.2

    # fifth line
    fifth_Tier = int(N / Aspect_ratio)
    fifth_Tier = int(N * fifth_line_proportion)

    # fourth line
    fourth_line_porportion = int(N / Aspect_ratio)












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











