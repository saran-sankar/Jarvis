from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
my_tokens = ["leaves","calves","books","surprising","data mining","girls","goes","puppies"]
for word in my_tokens:
    print(lemmatizer.lemmatize(word))
