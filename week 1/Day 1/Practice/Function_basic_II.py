# 1. Countdown

def countdown(num):
    """ Return a new list that counts down from num to 0 """
    arr = []
    for i in range(num, -1, -1):
        arr.append(i)
    return arr


print(countdown(5))


# 2. Print and Return
def print_and_return(my_list):
    """ Takes in a list and prints the first value and return the second """

    print(my_list[0])
    return my_list[1]


print(print_and_return([1, 2]))

# 3. First Plus Length


def first_plus_length(my_list):
    """ Takes a list and returns the sum of the first value and the list's length """

    return my_list[0] + len(my_list)


print(first_plus_length([1, 2, 3, 4, 5]))


# 4. Values Greater than Second
def values_greater_than_second(my_list):
    """ Takes a list and creates a new list with values that
        are only greater than the second value """

    if len(my_list) < 2:
        return False
    new_list = []
    for i in my_list:
        if i > my_list[1]:
            new_list.append(i)
    print(len(new_list))
    return new_list


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))


# 5. This Length, That Value

def length_and_value(size, value):
    """ Takes two values and creates a list of a given size with
        every value equal to the given value """

    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list


print(length_and_value(4, 7))
print(length_and_value(6, 2))