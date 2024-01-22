#!/usr/bin/python3
"""
Returns a tuple with the length of a string and its first character.
If the sentence is empty, the first character should be equal to None.
"""


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Parameters:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the string and its first character.
    """
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

