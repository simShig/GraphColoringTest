import math

def getValues(n):
    #Generate random values:
    # valuesList = [random.random() * 100 for _ in range(n)]

    #Generate ardesh sequences (of \sqrt(n) descending blocks):
    block_size = int(math.sqrt(n))

    # Initialize an empty list to store the result
    valuesList = []

    # Generate values for each block
    for i in range(0, n, block_size):
        # Calculate the start and end of the current block
        start = i + 1
        end = i + block_size
        # Generate the numbers for the block in descending order and append to the list
        block = list(range(end, start - 1, -1))
        valuesList.extend(block)

    print(valuesList)

    return valuesList

