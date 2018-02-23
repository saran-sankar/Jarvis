from nltk.tokenize import word_tokenize, sent_tokenize
line = "Hello! 'Welcome to text pre-processing session.' Do you know python? Mr. XXX is the tutor for this session."
tokens = word_tokenize(line)
print(tokens)

sentences = sent_tokenize(line)
print(sentences)




##import nltk
##tokenizer = nltk.data.load('tokennizers/punkt/english.pickle')
##line = "Hello! Welcome to text pre-processing session. Do you know python? Mr. XXX is the tutor for tis session"
##print(tokenizer.tokenize(line))
