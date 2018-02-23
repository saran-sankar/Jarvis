import nltk

porter = nltk.PorterStemmer()

myList = ["cry","crying","cried","look","make","making","into","intimate"]
print(myList)
print([porter.stem(t) for t in myList])
lancaster = nltk.LancasterStemmer()
print([lancaster.stem(t) for t in myList])


