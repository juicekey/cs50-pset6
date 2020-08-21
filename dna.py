from sys import argv, exit
import csv

def main():

    if len(argv) != 3:
        print('database, sequence')
        exit(1)
    #check number arguments

    database = open(argv[1])
    i = next(database)
    database.close()
    strList = i.strip('\n').split(',')
    strList.pop(0)
    #get list of STRs

    with open(argv[2], 'r') as sequence:
        sequence = sequence.read()

    count = []
    countList = []

    for item in strList:
        counter = 0
        for i in range(len(sequence) - len(item)):
            current = sequence[i: i + len(item)]
            while current == item:
                counter += 1
                current = sequence[i + counter * len(item): i + len(item) + counter * len(item)]
            count.append(counter)
            counter = 0
        countList.append(max(count))
        count = []
        #iterate through sequence when correct STR is found

    database = csv.DictReader(open(argv[1]))
    match = False
    for row in database:
        values = list(row.values())
        strCounts = []
        for value in values:
            strCounts.append(value)
        strCounts.pop(0)
        for i in range(len(strCounts)):
            strCounts[i] = int(strCounts[i])
        if strCounts == countList:
            match = True
            print(values[0])
    if match == False:
        print('No match')
#print name when a match is found




main()