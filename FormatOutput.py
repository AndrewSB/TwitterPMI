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
    if (line.count(',') == 5):
        indexOfComma = line.index(',')
        line[line.index(',')] = ' '
        print line