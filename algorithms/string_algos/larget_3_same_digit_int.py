
def largestGoodInteger(num: str) -> str:

    biggest = ''
    l = 0
    

    for r in range(len(num)):

        if r-l == 2 and num[l] == num[r]:
            good_int = num[l:r+1]
            biggest = biggest if good_int < biggest else good_int
        
        l = r if r-l==2 or num[r] != num[l] else l
        

    return biggest

print(largestGoodInteger("42352338")) # expect 777

