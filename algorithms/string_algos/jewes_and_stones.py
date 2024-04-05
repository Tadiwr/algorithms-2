def numberOfJewelsInStones(jewels: str, stones: str):
    count = 0

    for stone in stones:
        count += 1 if stone in jewels else 0
        
    return count



print(numberOfJewelsInStones("aA", "aAAbbbb"))