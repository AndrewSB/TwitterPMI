__author__ = 'asb'
#Thursday & Friday 2014-01-16,17
#Andrew Shekhar Breckenridge
#asbreckenridge@me.com  @Andrew_Breck



import nltk, re, itertools
from nltk.corpus import PlaintextCorpusReader
import collections


def GetTweets():
    corpusdir = 'DB/'

    newCorpus = PlaintextCorpusReader(corpusdir, '.*\.txt$') #Regex allows you to ignore .DS_Store

    pattern = '\r\n' #Regex accepts \r\n as the next line encoding in each 'tweet' in the database
    tweets = nltk.regexp_tokenize(newCorpus.raw(), pattern, gaps=True) #iterate through list, creating 'tweets'
    tweets = [x.lower() for x in tweets] #make all strings lowercase to make matching easier
    return tweets

allTweets = GetTweets() #GLOBAL

def GetRelevantTweets(PMITerm):
    matching = []
    for s in allTweets:
        if PMITerm in s:
            matching.append(s)

    backgroundcorp = []
    for element in matching:
        current = re.split(r'\s', element)
        backgroundcorp.append(current)

    return backgroundcorp


def GetSortedRelevantTweets(PMITerm):
    corpus = []
    backgroundcorp = GetRelevantTweets(PMITerm)

    for list in backgroundcorp:
        for word in list:
            if word != 'orange' and word != 'oranges':
                if (word.find('"') != -1):
                    word = word[0:word.index('"')] + word[word.index('"')+1:]
                if (word.find("'") != -1):
                    word = word[0:word.index("'")] + word[word.index("'")+1:]
                corpus.append(word)

    return sorted(corpus)


def CountInstancesGlobal():
    line =[]
    for sentances in GetTweets():
        words = sentances.split()
        line.append(words)
    line = [item for item in list(itertools.chain(*line)) if (item)]

    counted = collections.Counter(line)
    iterater = (sorted(counted.most_common()))

    return iterater




def CountInstances(PMITerm):
    list = []
    for words in GetSortedRelevantTweets(PMITerm):
        list.append(words)

    counted = collections.Counter(list)

    iterater = (sorted(counted.most_common()))
    return iterater





def WriteToExcel():
    f = open('wordbank.csv','w')
    list = CountInstancesGlobal()
    for twoplet in list:
        f.write(str(twoplet[0]))
        f.write(',')
        f.write(str(twoplet[1]))
        f.write('\n')
    f.close()


def WriteEAndToExcel(PMITerms):
    f = open('output.csv', 'w')
    for word in CountInstances(PMITerms):
        f.write(word[0])
        f.write(',')

        count = -1
        query = word[0]
        list = CountInstancesGlobal()
        for i in list:
            count = count + 1
            if i[0] == query:
                break
        f.write(list[count][0])
        f.write(',')
        f.write(str(list[count][1]))
        f.write(',')

        f.write(str(word[1]))
        f.write('\n')
    f.close()
