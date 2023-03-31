"""
   Create a function to return the first element of the list
"""


def first_element_of_list(num_list):
    if not num_list:
        return None
    return num_list[0]


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
first_element = first_element_of_list(my_list)
print(first_element)
