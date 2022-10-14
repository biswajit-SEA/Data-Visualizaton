def concate(x):
    rev = x // 10
    

    y = "".join(reversed(str(rev)))

    x = str(x)

    x += y

    return int(x)

list = [15342342, 1454541, 31231, 6345, 12, 457, 9, 1281, 313, 55]
list2 = []

for i in list:
    z = "".join(reversed(str(i)))
  
    if(i == int(z)):
        list2.append(i)

    elif(len(str(i)) == 1):
        list2.append(i)
    
    elif(len(str(i)) > 1 and len(str(i)) <= 4):
        x = concate(i)
        list2.append(x)         

    elif(len(str(i)) > 4):
        a = 0
        list2.append(a)

print(list2)