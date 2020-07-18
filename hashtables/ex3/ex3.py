def intersection(arrays):
    # initialize numbers dict
    numbers = {}

    # for each array in arrays
    for array in arrays:
        # for each number in array
        for num in array:
            if num in numbers:
                # if number is in numbers: increment + 1
                numbers[num] += 1
            else:
                # else add number to numbers, with value 1
                numbers[num] = 1

    # in numbers: find items where value == len(arrays)
    result = [k for k, v in numbers.items() if v == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
