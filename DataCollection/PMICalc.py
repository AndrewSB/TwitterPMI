from __future__ import division
__author__ = 'asb'
import driver, main, csv, math

PMITerm = driver.PMITerm

#panswer[0]  = string
#panswer[1]  = p(x,y)
#panswer[2]  = p(y)
#pofx       = p(x)
#PMI(x;y)   = p(x,y)/(p(x)*p(y))

#Output: string, PMI(x,y)
answer = driver.answer

numberOfTweets = len(main.allTweets)
numberOfWords = len(driver.totalTweets)


panswer = [] #panswer becomes (x,x,x) with string, p(x,y), p(y)
for element in answer:
    panswer.append((element[0], (element[1]/numberOfTweets), (element[2]/numberOfWords)))

pofx = driver.totalTweets.count(PMITerm)/numberOfWords


PMIs = []
for element in panswer:
    if (pofx != 0 and element[2] != 0):
        top = -element[1]*math.log((element[1])/(pofx*element[2]))
        bottom = element[1]*math.log(element[1])
        PMI = top/bottom
        #PMI = (element[1]/((pofx*element[2])))
        #PMI = math.log(PMI)
    else:
        PMI = 'invalid'
    PMIs.append((element[0], PMI))


f = open('output.csv', 'wb')
for element in PMIs:
    f.write(str(element[0]))
    f.write(',')
    f.write(str(element[1]))
    f.write("\n")
f.close()