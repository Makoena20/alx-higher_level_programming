#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Parameters:
    - my_list (list): The input list.
    - idx (int): The index at which the element should be replaced.
    - element: The new element to be placed at the specified index.

    Returns:
    - The modified list or the original list if index is out of range or negative.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

