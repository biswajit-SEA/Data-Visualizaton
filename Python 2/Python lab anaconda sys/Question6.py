import csv
import sys

n = len(sys.argv)

list1=[]

if(n!=3):
    print("Wrong arguments")

else:
    filename = sys.argv[1]
    csv_file = open(filename, 'r')
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        list1.append(line)


list1[0].append("total_marks")
sum = 0

for i in list1[1:]:
    for j in range (1,6):
        if(i[j].isnumeric()):
            sum += int(i[j])
    i.append(sum)
    sum=0

res = [list1[0]] + sorted(list1[1:], key = lambda x:x[7], reverse = True)

filename = sys.argv[2]
csv_file = open(filename, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerows(list1)

print(res)