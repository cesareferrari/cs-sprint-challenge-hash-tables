def has_negatives(a):
    numbers = {}

    # go through the list of numbers (a)
    for num in a:
        n = abs(num)

        if n in numbers:
            # if abs(number) is in dict: add 1 to value
            numbers[n] += 1
        else:
            # otherwise, add it to the dict as a key with value 1
            numbers[n] = 1

    # return all keys with value 2
    result = [k for k, v in numbers.items() if v == 2]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
