import webbrowser
import re

def Reply(reply,rep,p,a):
    pun=''
    if reply!='':
        pun='. '
    reply=reply+pun+rep[a]
    p=p+1
    return reply,p
def gender(stringSplit):
    he=she=0
    for i in range(0,len(stringSplit)):
        if stringSplit[i]=='she' or stringSplit[i]=='her':
            she+=1
        elif stringSplit[i]=='he' or stringSplit[i]=='his' or stringSplit[i]=='him':
            he+=1
    if he>she:
        return True
    else:
        return False
def lookup(keyword):
    webbrowser.open('https://www.google.co.in/search?site=&source=hp&q='+keyword)
def speak(word):
    webbrowser.open('https://ssl.gstatic.com/dictionary/static/sounds/oxford/'+word+'--_gb_1.mp3')
def shortform(convo,convocopy,shortform):
 shortform=0
 if re.match('^([a-z]| |[A-Z])*[A-Z][A-Z]+',convo):
     k=(re.search('^([a-z]| |[A-Z])*[A-Z][A-Z]+',convo))
     convoSplit=re.sub("[^\w]", " ", convo ).split()
     length=len( re.sub("[^\w]", " ", k.group(0) ).split()[-1])
     ai=[]
     con=[]
     for i in range(0,length):
        ai.append(re.sub("[^\w]", " ", k.group(0)).split()[-1][i].lower())
     for i in range(1,length+1):
         append='^([a-z]| )*'
         for j in range(0,length):
             if j!=length-1:
                append+=ai[j]+'[a-z]* '
             else:
                append+=ai[j]+'[a-z]*'
         if re.search(append,convocopy):
             con.append(re.sub("[^\w]", " ",  re.search(append,convocopy).group(0)).split()[-i])
             shortform+=1
         append=''
     if shortform>0:
      con.reverse()
      pos=convoSplit.index(re.sub("[^\w]", " ",  k.group(0)).split()[-1])
      convoSplit.remove(convoSplit[pos])
      for i in range(0,length):
          convoSplit.insert(pos+i,con[i])
 if shortform>0:
          return convoSplit,shortform
 else:
          return convo,shortform
