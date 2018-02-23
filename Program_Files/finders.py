import re
import random
from nltk.corpus import stopwords
def element_finder(item_list,keyword):
    keyword=re.sub("[^\w]"," ",keyword).lower().split()
    item_list2={}
    no_of_stopw_list=[]
    for i in range(len(item_list)):
        item_list2[re.sub("[^\w]|_"," ",item_list[i]).lower()]=0
    for i in range(len(item_list2)):
        no_of_stopw=0
        for j in range(len(keyword)):
            if keyword[j] in list(item_list2.keys())[i].split():
                if keyword[j] in stopwords.words('english'):
                    item_list2[list(item_list2.keys())[i]]+=1
                    no_of_stopw+=1
                    #print(1)
                else:
                    item_list2[list(item_list2.keys())[i]]+=2
                    #print(2)
        no_of_stopw_list.append(no_of_stopw)              
    maxRelevance=max(list(item_list2.values()))
    #print(no_of_stopw_list)
    #print(maxRelevance)
    #print(item_list2)
    if maxRelevance == 0 or maxRelevance-2 in no_of_stopw_list:
        return ' '
    top_results=[]
    for i in range(len(item_list2)):
        if item_list2[list(item_list2.keys())[i]] == maxRelevance:
            top_results.append(item_list[i])
    a=random.randint(0,len(top_results)-1)
    final_result=top_results[a] #maybe find a better option
    return final_result
