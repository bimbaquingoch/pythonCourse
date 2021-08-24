def find_max(listNumbers):
    maxN = listNumbers[0]
    for number in listNumbers:
        if number > maxN:
            maxN = number

    return maxN
