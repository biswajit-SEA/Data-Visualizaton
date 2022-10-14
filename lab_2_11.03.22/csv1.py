import csv
import sys

n = len(sys.argv)

if(n!=2):
    print("Enter proper arguments")

else:
    filename = sys.argv[1]
    csv_file = open(filename, 'r')
    csv_reader = csv.reader(csv_file)

    count = 0

    for line in csv_reader:
        if(line[0].isnumeric()):
            count += 1

print("Total no of candidates passed: {}" .format(count))
