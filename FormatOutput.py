__author__ = 'asb'


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

numberOfLines = int(file_len('output.csv'))


r = open('output.csv', 'r')
w = open('formattedOutput.csv', 'w')


for i in range(numberOfLines):
    line = r.readline()
    numberOfCommas = line.count(',')
    while numberOfCommas > 1:
        indexOfComma = line.index(',')
        print line
        tempLine = line[0:indexOfComma] + ' ' + line[indexOfComma+1:]
        print tempLine
        line = tempLine
        numberOfCommas = line.count(',')
    w.write(line)
