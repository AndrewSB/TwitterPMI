__author__ = 'asb'


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

numberOfLines = int(file_len('output.csv'))


f = open('output.csv', 'r+b')

for i in range(numberOfLines):
    line = f.readline()
    numberOfCommas = line.count(',')
    while numberOfCommas > 1:
        indexOfComma = line.index(',')
        tempLine = line[0:indexOfComma] + ' ' + line[indexOfComma+1:]
        line = tempLine
        numberOfCommas = line.count(',')
        f.seek(i)
        f.write(line)

for i in range(numberOfLines):
    if numberOfCommas > 1:
        f.seek(i)
        print f.readline()