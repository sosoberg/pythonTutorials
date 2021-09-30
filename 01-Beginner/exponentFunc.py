def raiseToPower(base, power):
    result = 1
    # for loop with a range
    for index in range(power):
        result = result * base

    return result

print(raiseToPower(9, 30))
