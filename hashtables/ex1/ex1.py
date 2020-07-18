def get_indices_of_item_weights(weights, length, limit):
    packages = {}

    # put all weights in packages dict as tuples (weight, index)
    for i in range(length):
        packages[i] = (weights[i], i)

    # go through the packages key, calculate limit - current weight
    for key in packages:
        # extract the current weight
        weight = packages[key][0]
        # find a target that is limit - weight
        target = limit - weight

        # if the target weight is in the weight list
        # get the keys where the value weight is the same
        # as either the target or the original weight
        if target in weights:
            result = [k for k, v in packages.items()
                        if v[0] == weight
                        or v[0] == target]

            return sorted(result, reverse = True)

    return None


if __name__ == "__main__":

    weights = [ 4, 6, 10, 15, 16 ]
    length = 5
    limit = 21

    result1 = get_indices_of_item_weights(weights, length, limit)
    print(result1)

    answer_2 = get_indices_of_item_weights([4, 4], 2, 8)
    print(answer_2) # [1, 1] should be [1, 0]
