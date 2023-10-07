import math

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


# 4.
# Write a function process_scores( )that reads student names and their scores from a user and displays the following: 
# the average score, the minimum score, the maximum score, and the students who received the minimum and maximum scores. 
# The function repeatedly prompts the user to enter the name and the score of a student. The user enters the name and the 
# score separated by blank in one line. The name is a single word and the score is an integer. The user enters q in lower 
# or upper case to quit. The user does not enter score after q. The outputs are displayed with appropriate messages.

def process_scores():
    
    # define and initiate two empty list as containers for name and score
    name = []
    score = []

    # keep prompting user for input until quit
    while True:
        
        # collect user's input in a string varibale called "enter"
        enter = input("Enter student's name and score. Enter q or Q to quit: ")
        # if user enter q or Q, quit
        if enter.lower() == "q":break

        # split string "enter" with a pace, result "studentScore" is a list
        studentScore = enter.split()

        # append name to name list
        name.append(studentScore[0])
        # append score to score list; change score type from string in integer
        score.append(int(studentScore[1]))

    #outside the while loop, initialize and define a new variable called sum
    sum = 0
    # calculate sum and average 
    for element in score:
        sum = sum + element
        average = sum / len(score)

    # use list function for min and max
    minScore = min(score)
    maxScore = max(score)

    # traverse the list to find the name with min score
    for i in range (len(name)):
        if(score[i] == minScore):
            print("Minimum score: " + name[i] + " " + str(score[i]) )

    # traverse the list to find the name with max score    
    for i in range (len(name)):
        if(score[i] == maxScore):
            print("Maximum score: " + name[i] + " " + str(score[i]))

    print("Average score: " + str(average))

# 5. 
# Write a function that determines the tax amount according to the following tax rules. 
# The tax rate depends on the income, the marital status, and the state residency. For in state 
# residents, the following rates apply. If single and income is less than 30000 then tax rate is 
# 20%. If single and income is greater or equal to 30000 then tax rate is 25%. If married and income
# is less than 50000 then tax rate is 10%. If married and income is greater or equal to 50000 then
# tax rate is 15%. For out of state residents, the similar rules apply except the tax rate is 3% 
# less than the tax rate of the corresponding in state residents. The function is 
# compute_tax(income, status, state). The income is an integer. The status is string single or 
# married in lower or upper case letters. The state is character i or o in lower or upper case 
# letters. The function computes and returns the tax amount.
def compute_tax(income, status, state):
   
    # if single 
    if(status.lower() == "single"):
        # if single and poor
        if(income < 30000):
            tax = income * 0.2
        # if single not poor    
        else:
            tax = income * 0.25
    # if married
    else:
        # if married and poor
        if(income < 50000):
            tax = income * 0.1
        # if married rich
        else:
            tax = income * 0.15
    
    # in state or not
    if(state.lower() == "o"):
        tax = 0.97 * tax
    
    print(tax)
    return tax

# 6.
# Write a function that solves a given quadratic equation. The function is solve_quadratic(a, b, c).
# The input parameters a, b, and c represent the coefficients of the quadratic equation 
# ax2 + bx + c = 0. First the function checks whether the given equation actually has solutions. The
# equation has solutions only if b2 – 4ac ≥ 0. If there are solutions then the function computes the 
# solutions using the formula (–b ± √(b2 – 4ac))/2a. The function returns the two solutions as return 
# values. If there are no solutions then the function returns two zeros.

def solve_quadratic(a, b, c):
   
    dis = b * b - 4 * a * c

    # if dis >= 0, has solutions
    if(dis >= 0):
        solution1 = (-b + math.sqrt(dis)) / (2*a)
        solution2 = (-b - math.sqrt(dis)) / (2*a)
        
        #return solution1, solution2
        print(f"solution1: {solution1}")
        print(f"solution2: {solution2}")
        return solution1, solution2

    # if dis < 0, no solution
    else:
        print("No solution")
        return 0, 0
    
# 7.
# Write a function sort(list) that sorts a given list of numbers. The function returns the sorted 
# list as return value. The given input list remains unchanged. Selection sort must be used. Built in 
# sort function cannot be used.

def sort(list):
    # Since orignial list cannot be changed, copy list to a new list called "cpList"
    cpList = list.copy()
    # traverse every element in the list, index 0 to the end
    for i in range(len(list)):
        # set the index of minimum number to i, minimum index will start from index 0
        min_index = i
        # for each element, traverse and compare all the numbers after this element
        for j in range(i+1,len(list)):
            # if the later number smaller than the element, swap
            if int(cpList[j]) < int(cpList[i]):
                # swap with an temporary container called "temp"
                temp = cpList[i]
                cpList[i] = cpList[j]
                cpList[j] = temp
    
    # print the list: traverse every element and print each
    for i in range(len(list)):
        print(cpList[i])
    
    return cpList

# 8.
# Write a function that automatically generates the user id and the password for the user. The user id 
# and the pass words are based on the user’s last name and first name. The user id is the first letter 
# of the first name followed by the last name. The password is the first letter of the first name 
# followed the last letter of the first name followed by the first three letters of the last name 
# followed by the length of the first name followed by the length of the last name. The user may enter 
# the first and last names in lower or upper case letters. Both the user id and passwords must be in 
# upper case. For example, if the first name is John and the last name is Maxwell then the user id is 
# JMAXWELL and the password is JNMAX47. The function id_password(first, last) takes first name and last 
# name as inputs and returns user id and password as outputs.

def id_password(first, last):
    # first letter of the first name
    firstName1stLetter = first[0]
    # length of the first name
    lenFirst = len(first)
    # last letter of the first name 
    firstNameFinalLetter = first[(lenFirst)-1]

    # id 
    id = (firstName1stLetter + last).upper()
    # password
    password = (firstName1stLetter + firstNameFinalLetter + last[0:3] + str(lenFirst) + str(len(last))).upper()

    print("Id: " + id)
    print("Password: " + password)

    return id, password

  

# 10. Question Menu
def main():
    print("Question 1: compute pi")
    print("Question 2: compute square root")
    print("Question 3: display prime number")
    print("Question 4: student score")
    print("Question 5: tax calculation")
    print("Question 6: quadratic equation")
    print("Question 7: selection sort")
    print("Question 8: Id & Password Generator")
    

    # continue prompte, until user quit
    while True:
        # prompte the user for input, then save it to variable questionNum
        questionNum = int(input("Enter a question number from 1 ~ 9 (Enter 0 to quit):"))

        if(questionNum == 0): break

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
    
        elif(questionNum == 4):
            process_scores()
        
        elif(questionNum == 5):
            
            status = input("Enter marital status: married or single: ")
            income = int(input("Enther income: "))
            state = input("Enter state residency: 'i' for instate, 'o' for out state: ")
            
            compute_tax(income, status, state)

        elif(questionNum == 6):
            
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            c = int(input("Enter c: "))

            solve_quadratic(a, b, c)

        elif(questionNum == 7):

            list = (input("Enter numbers, seperate numbers with space: ")).split()

            sort(list)
        
        elif(questionNum == 8):
            first = input("Enter first name: ")
            last = input("Enter last name: ")

            id_password(first, last)


# call main function 
main()


# 11.
# Write a Rectangle class. The class has two data members namely length and width. It has a constructor that 
# sets the length and width to its two parameter values. It has set and get methods for each of length and width. 
# The class a method that returns the area of the rectangle. It also has the standard string method that returns 
# a string representation of the rectangle. Write code to test all the methods of the rectangle class.

class Rectangle:
    # constructor 
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # set method
    def setLength(self, length):
        self.length = length
    
    def setWidth(self, width):
        self.width = width

    # get method 
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width

    # method for return area
    def area(self):
        return self.length * self.width
       

    # to string 
    def __str__(self):
        return "length: " + str(self.length) +"\nwidth: " + str(self.width)
    
# test:
x = Rectangle(20, 30)
print(x)
print("Area:", x.area())






