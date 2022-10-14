import csv
import sys

n = len(sys.argv)

def selection(lis):
    if (int(lis[6]) == 1):
        return 1
    else:
        return 0

list1=[]
list2=[]


if(n!=2):
    print("Enter proper arguments")

else:
    filename = sys.argv[1]
    csv_file = open(filename, 'r')
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        list1.append(line)

r = list(map(selection, list1))

sel = sum(r)

print("Total number of selected candidates {}" .format(sel))
