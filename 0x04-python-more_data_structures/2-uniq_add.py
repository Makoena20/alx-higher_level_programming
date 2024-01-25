#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    result = sum(unique_set)
    return result

# Uncomment the following lines to test the function
# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))

