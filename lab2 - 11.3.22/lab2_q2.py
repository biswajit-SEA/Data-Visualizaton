def makepalindrome(lst):
    c=0
    for i in lst:
        a=i
        l=len(i)
        if a == a[::-1]:
            lst[c] = int(a)
        else:
            if l <= 4:
                b = a[-2::-1]
                a += b
                lst[c] = int(a)
            else:
                lst[c] = 0
        c += 1
    return(lst)

lst=(input("Enter elements separated by commas : ")).split(",")
lst2=makepalindrome(lst)
print(lst2)