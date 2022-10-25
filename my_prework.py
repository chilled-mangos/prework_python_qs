# question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    """Greet the username."""
    print("Hello " + user_name + "!")

hello_name("timothy greenie")

# question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """print odd numbers from 1-100 and returns nothing."""
    list = (range(0,100))
    for range in list:
        if range % 2 != 0:
            print(range, end = " ")
#there is no arguments so nothing returns


# question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    """return the max number of a given list."""
    print(max(a_list))
max_num_in_list([1, 3, 10, 14, 22, 66, 75, 89, 3])


# question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """return if the given number is a leap year"""
    if a_year % 4 == 0:
        print("True")
    elif a_year % 4 != 0:
        print("False")

is_leap_year(2024)


#question 5
# Write a function to check to see if all numbers in list are consecutive numbers. '
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    """checking to see if all these numbers are consecutive numbers. """
    for i in range(len(a_list)-1):
        if a_list[i]+1 != a_list[i+1]:
            return False
    return True

print(is_consecutive([2,3,4,5,6,7]))
print(is_consecutive([1,2,4,5]))



