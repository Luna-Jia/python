
# 1.
# Write a function that computes the value of mathematical constant π. The value of π 
# can be computed using the infinite series p = 4(1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + . . .). 
#The function compute_pi(n) computes the value of π using the first n terms of the infinite 
# series and returns the value.

def compute_pi(n):
    # create an variable, a container to hold the answer 
    pi = 0 
    # a for loop, n is range, must be an integer. Means 0<= i < n, incease is 1 (optional)
    for i in range (0, n, 1): 
        if i % 2 == 0:
            pi =pi + 1/(2 * i + 1)
        else:
            pi =pi - 1/(2 * i + 1)

    pi = 4 * pi
    print("The approximate value of pi with", n, "terms is:", pi)

# 2. 
# Write a function that computes the square root of a given number. The square root of a number
#  x can be computed as follows. First guess that the square root of x is 1. Then repeatedly get 
# the next guess from the last guess using the relation next = 0.5(last + x / last) where last is 
# the last guess and next is the next guess. Repeat ten times using a loop and the tenth guess will 
# be the square root. The function compute_sqrt(x) computes the square root of x and returns the square root.

def compute_sqrt(x):
    sqrt = 1
    next = 0.5 * (sqrt + x/sqrt)
    sqrt = next






# 10. Question Menu
def main():
    # prompte the user for input, then save it to variable questionNum
    questionNum = int(input("Enter a question number from 1 ~ 9 (Enter 0 to quit):"))

    if (questionNum == 1):
        num = int(input("Enter a integer term number to compute pi: "))
        # call function 
        compute_pi(num)

# call main function 
main()





