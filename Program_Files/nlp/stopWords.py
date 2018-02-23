import nltk
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))
text = "When we use a web search engine, we usually don't mind if the words in the document differ from our search terms in having different endings. A query for laptops finds documents containing laptop and vice versa. Indeed, laptop and laptops are just two forms of the same dictionary word. For some language processing tasks we want to ignore word endings, and just deal with word stems."
my_tokens =text.split()
#print(my_tokens)
#print(stopwords)
myNewList =[]
for word in my_tokens:
    if word not in stops:
        myNewList.append(word)
#print("**************After Removal of Stop Words**************")
#print(myNewList)
#print(stopwords.fileids())
print(stopwords.words('english'))
