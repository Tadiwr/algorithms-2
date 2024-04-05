# Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def finalValueAfterOperations(operations : list[str]) -> int:
    x = 0
    valueToBeAdded = {'X++' : 1, '++X' : 1, 'X--': -1, '--X' : -1}

    for operation in operations:
        x += valueToBeAdded[operation]

    return x


print(finalValueAfterOperations(["--X","X++","X--"]))