__author__ = 'asb'

import main, collections, itertools

PMITerm = 'orange'
listOfBGWords = main.GetSortedRelevantTweets(PMITerm)


lister = [] #this code block calcs tuplesIT variable
for words in listOfBGWords:
    lister.append(words)
counted = collections.Counter(lister)
sortedCounter = counted.most_common()
tuplesIT = sorted(sortedCounter) #tuples form ('word', 'instances') of all the words in the tweets - "tuples In Tweets"


lister = [] #this code block calcs
cleanList = []
for sentences in main.allTweets:
    words = sentences.split()
    lister.append(words)

cleanList = list(itertools.chain(*lister))

totalTweets = cleanList #GLOBAL

counted = collections.Counter(cleanList)
tuplesG = sorted(counted.most_common())

dict_tuplesG = dict(tuplesG) #codeblock concatenates the two tuples into one of the form ('word', instances in relevant tweets, instances in corpus)
answer = [(string, count, dict_tuplesG.get(string, 0)) for string, count in tuplesIT]
