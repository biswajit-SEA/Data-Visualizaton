import csv
import sys

n = len(sys.argv)

list=[]

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
        list.append(line)

x = len(list)

for row in list:
    print(row)

print("the no of candidates is {}" .format(x))
