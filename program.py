
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
     # create an variable "sqrt", a container to hold the answer, initialize it to 1
    sqrt = 1 
    for i in range (10):
        # repeatly compute "next" using "sqrt"
        next = 0.5 * (sqrt + x/sqrt)
        # assign next to sqrt
        sqrt = next
    # print out the answer to screen
    print(sqrt)


#3.
# Write a function that decides whether a given number is a prime or not. A prime number is a number that is 
# divisible only by 1 and itself. The function is_prime(n) decides whether n is prime or not and returns true 
# if n is prime and returns false otherwise. Write another function display_primes(n)that displays all prime 
# numbers less than or equal to n.

def is_prime(n):
    # 0 and 1 is not prime number, exclude them
    if(n <= 1): 
        return False 
    # 2 and 3 is prime number
    if(n == 3 or n == 2):
        return True
    
    for i in range (2, n):
        # exlude n that can be divisible by any number from 2 to (n-1)
        if( n % i == 0):
            return False
    # all else are prime number 
    return True

def display_primes(n):
    # prompte 
    print("Prime numbers less than or equal to " + str(n) + ":")

    # traverse all the number from 0 to n, check 
    for i in range(n+1):
        if(is_prime(i)):
            print(i)


# 10. Question Menu
def main():
    # prompte the user for input, then save it to variable questionNum
    questionNum = int(input("Enter a question number from 1 ~ 9 (Enter 0 to quit):"))

    if (questionNum == 1):
        num = int(input("Enter a integer term number to compute pi: "))
        # call function 
        compute_pi(num)

    elif (questionNum == 2):
        num = int(input("Enter a number to compute square root: "))
        # call function 
        compute_sqrt(num)
    
    elif( questionNum == 3):
        num = int(input("Enter a number to display all prime: "))
        # call function 
        display_primes(num)



# call main function 
main()





