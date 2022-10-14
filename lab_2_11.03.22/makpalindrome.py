palindrome_arr=[]
class makepalindrome:
    def __init__(self,arr):
        self.arr=arr
    def makePalindrome(self):
        for i in arr:
            num=str(i)
            rev=num[::-1]
            l=len(num)
            if num==rev:
                palindrome_arr.append(i)
            else:
                if l<=4:
                    pal=num+rev[1:l]
                    palindrome_arr.append(int(pal))
                else:
                    palindrome_arr.append(0)

arr=[12,457,9,1281,313,55]
a=makepalindrome(arr)
a.makePalindrome()
print(palindrome_arr)

