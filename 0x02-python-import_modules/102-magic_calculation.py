def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c
    else:
        return __import__('magic_calculation_102').sub(a, b)

if __name__ == "__main__":
    print(magic_calculation(10, 15))  # Correct output: FAKE magiccalculation_102
    print(magic_calculation(23, 17))  # Correct output: FAKE magiccalculation_102

