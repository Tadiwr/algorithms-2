# Link: https://leetcode.com/problems/find-words-containing-character/description/

def findWordsContaining(words: list[str], x:str) -> list[int]:
    out_list = []

    for i in range(len(words)):
        if x in words[i]:
            out_list.append(i)
        
    return out_list


print(findWordsContaining(["leet","code"], 'e')) # expecting [0, 1]