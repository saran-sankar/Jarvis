from Program_Files import jarvis
from Program_Files.language import *
from Program_Files.understanding import *
import Jarvis_read_mode
#from Program_Files import iPhone_mode
import random
import re
from datetime import datetime
import urllib.request
#from Program_Files import iot

loop=0
st=0
convocopy=''
Name='You'
keyword=''
reply=''
convoSplit=''
convoiPhoneC=''

while loop>=0:

 a=random.randint(0,2)
 b=random.randint(0,3) 
 c=random.randint(0,4) #currently not in use

 
 if iPhoneMode<2:
  print("\n")
  print("Jarvis")

 if st!=0:                  
     for d in range(0,len(convoSplit)):
        if convoSplit[d] in Time:
            print("The time is")
            print(datetime.now().time())
            p=p+1
        if convoSplit[d] in YouWish:
            hey=hey+1                             #INVOKING JARVIS                  
 if st!=0:
     for d in range(0,len(convoSplit)):
        if convoSplit[d-1] in lights and convoSplit[d] in lights:
            iot.lights(convoSplit[d-1]) # IoT  edit
            p+=1
            break
            
        if convoSplit[d] in read_book:
                p=Jarvis_read_mode.Jarvis_read(convoSplit)   #READING
                break
     
        if convoSplit[d] in love and ((convoSplit[d-1] and convoSplit[d-2])in modest[0] or (convoSplit[d-1] and convoSplit[d-2]) in modest[1]):  #edit
            if modestCount==-5:
                modestCount=-10          #wrong
            else:
                modestCount=-5
        if convoSplit[d] in modest[0] or convoSplit[d] in modest[2]:
            if convoSplit[d] in modest[2] and convoSplit[d-1] in doDid[0]:          
                modestCount=10
            elif convoSplit[d-1] in doDid[0] or d<len(convoSplit)-1 and convoSplit[d+1] in doDid[0]:
                modestCount=modestCount+1
        if convoSplit[d] in Thanks:
             reply,p=jarvis.Reply(reply,Welcome,p,a)
        if convoSplit[d] in Exclamation and bad<=1 and convocopy not in YouWish and hey==0:
             reply,p=jarvis.Reply(reply,Yeah,p,a)
             yeah+=1
        if convoSplit[d] in Yeah:                          #add plus operator(test)
             reply,p=jarvis.Reply(reply,ThoughtSo,p,a)
             yeah=0
        if convoSplit[d] in Laugh:
             reply,p=jarvis.Reply(reply,LaughW,p,a)
        if convoSplit[d] in Okay or convoSplit[d] in no:
             if convoSplit[d] in no:
                 nope+=1
             if convoSplit[d]!=no[-1]:
                 reply,p=jarvis.Reply(reply,Okay,p,a)
        if convoSplit[d] in Oh:
             reply,p=jarvis.Reply(reply,WhatHap,p,a)
             break
        if convoSplit[d] in food[0]:
             reply,p=jarvis.Reply(reply,foodJ,p,a)
        if convoSplit[d] in great and modestCount>0:
            pp=pp+1
            print(Thanks[a])
            p=p+1
        if d!=0 and (convoSplit[d-1] in modest[0] or convoSplit[d-1] in modest[1]):
            if (d<len(convoSplit)-1) and (convoSplit[d+1] in suggest2 or convoSplit[d] in suggest1):
                print(Okay[a]+", "+"that's a good idea")
                p=p+1
        
        if len(convocopySplit)>d+1:
            if (convocopySplit[d] in Help and convocopySplit[d+1] in Help) or convocopySplit[d-1] in Bad2 or (badd>2 and badd<10) :
                badd=0
                for dd in range(0,len(convoSplit)):
                    if (convoSplit[dd] in Bad2) or((convoSplit[dd-1] in Help and convoSplit[dd] in Help) or convoSplit[dd] in Yeah or convoSplit[dd] in Okay):
                        print(Help2J[a])
                        jarvis.lookup('hospitals+near+me')#modify(make dynamic)
                        p=p+1
                        pp=pp+1
                        break            
        if nope==0 or convoSplit[d] in food[1]:
                for dd in range(0,len(convocopySplit)):
                    if convocopySplit[dd] in food[0]:
                        jarvis.lookup(convocopySplit[dd]+'+near+me')
                        p=p+1
                        pp=pp+1
                        break
                    elif convoSplit[d] in food[1]:
                        print(foodJ[a])
                        jarvis.lookup('restaurants+near+me')
                        p=p+1
                        break
                
                
        elif convoSplit[d] in Help and convoSplit[d-1] in Help:
             print(Help1J[a])
             p=p+1
             
     if reply!='':               
        print(reply)
        
     if modestCount>=-5 and modestCount<0 and bad==0:
         print(Thanks[a])
         p=p+1
     elif modestCount<-5:
         print(Oh[b])
         p=p+1                   #not working as expected
     elif modestCount>0:
         if modestCount>=10:
             print("Whose mine?")                              #Not working
         elif pp==0:
             print("Who me?")
         p=p+1
 
 if st!=0:
     for d in range(0,len(convoSplit)):
        if convoSplit[d] in ByeY:
           print(ByeS[a])  
           end=end+1
 
 if st==0:
     print(JarvisIsReady1[a])
 elif convo in YouWish and st!=1:
     print(JarvisIsReady[b])
 elif st==1:
  if convo in Wassup:
             print(JarvisIsDoing[a])
  elif convo not in HowUDoin:
      print(Wassup[a])
  else:
      print(Fine[a])
                 
 elif convo in HowUDoin:
          print(Fine[a])    #can be a mismatch
 elif convo in Wassup and st!=1:
              print(JarvisIsDoing[a])
 elif convo in URDoing: #maybe there is a better soln
                print(JarvisIsDoing2[a])
 
                        
                #teach Jarvis more(priority order is important)
 elif st!=1:
     if st!=0:
       for d in range(0,len(convoSplit)-1):
        if (convoSplit[d-1] in lookUp[0] and convoSplit[d] in lookUp[1]) or (convoSplit[d] in question and p==0):

              if convoSplit[d] not in question:
                  for dd in range(d+1,len(convoSplit)):
                      if convoSplit[dd] not in lookUp[0]:
                          if convoSplit[dd] in Bad2 or badd>2:
                              p+=2
                          for gend in range(0,len(Connect)):
                            if convoSplit[dd] in Connect[gend]:
                                convoSplit[dd]=lastAnswer[gend]
                                break
                          keyword=keyword+'+'+convoSplit[dd]
                  print(webResults[a])                                                            #Look Up
                  jarvis.lookup(keyword)
                  p=p+1
                  break
              else:
                  for dd in range(d,len(convoSplit)):
                      for i in range(0,len(specKey)):
                          if convoSplit[dd] in specKey[i]:
                              specKeyw=i                   #Special Keyword1
                              
                      for ddd in range(0,3):        
                         if convoSplit[dd] in Connect[ddd]:
                              convoSplit[dd]=lastAnswer[ddd]  #connect to the last ans
                      keyword=keyword+'+'+convoSplit[dd]      #error

                  j=0
                  page = urllib.request.urlopen('https://www.bing.com/search?q='+keyword)

                  string = page.read().decode('utf-8')
                  stringSplit = re.sub("[^\w]", " ",  string).split()
                  for i in range(0,len(stringSplit)):#-10000

                       if specKeyw>=0:
                           j=-1
                           if stringSplit[i] in specAns[specKeyw] and stringSplit[i+1] in specAns[specKeyw]:
                               print(re.sub("[,;\s]|[+]",' ',keyword).split()[-1]+" is "+stringSplit[i-1]+" "+stringSplit[i]+" "+stringSplit[i+1])
                               p=p+1
                               specKeyw=-1
                               break                    #Special Keyword2
                           #else:
                               #specKeyw=-1
                            
                       elif stringSplit[i]=='SNAPST':
                           j=j+1
                       if j>1:

                                    
                          if stringSplit[i+6][0].isupper():
                              lastAnswer[0]=stringSplit[i+6]+"+"
                              if stringSplit[i+7][0].isupper():
                                 lastAnswer[0]+=stringSplit[i+7]
                                 print(stringSplit[i+6]+" "+stringSplit[i+7])
                              else:
                                 print(stringSplit[i+6])
                              p=p+1
                              #break
                              page = urllib.request.urlopen('https://www.bing.com/search?q='+lastAnswer[0]+'%3F&go=Submit&qs=bs&form=QBLH')
                              string = page.read().decode('utf-8')
                              string=string.lower()
                              stringSplit = re.sub("[^\w]", " ",  string).split()

                              #Gender
                              #j=0
                                  
                              if jarvis.gender(stringSplit):    #he
                                  lastAnswer[1]=lastAnswer[0]
                              else:
                                  lastAnswer[2]=lastAnswer[0]
                              break
                            
                          else:
                              j=0
                  if j<=1 and j!=-1:
                      p=p+1
                      print(webResults[a])
                      jarvis.lookup(keyword)
                      break
                
        elif convoSplit[d] in pronounce:
            print(listen[a])
            jarvis.speak(convoSplit[d+1])
            
        elif convoSplit[d] in fWord:
            print(mindLanguage[a])
            p=p+1
        elif (convoSplit[d-1] in Connect[0]or convoSplit[d-1] in Connect[1] or convoSplit[d-1] in Connect[2]) and (convoSplit[d] in doDid[1]) and d!=0:
            for teach in range(0,len(convoSplit)-1):
                if convoSplit[teach] in Connect[0] and nope>0 and teach1>0:
                    print(learned[a])
                    break
                if teach==len(convoSplit)-2:
                    if(a%2!=0) and yeah==0:
                        print(Yeah[b-1]+','+ikr[a])
                    else:
                        print(ikr[a])
            p=p+1
        elif convoSplit[d-1] in backtoLap[0] and convoSplit[d] in backtoLap[1] and iPhoneMode>0 and p==0:    #switch off iPhone mode
            print(backtoLapJ[a])
            iPhoneMode=0
            p=p+1
        elif iPhoneMode==0 and convoSplit[d] in iPhone:
            p=p+1
        
            
 if iPhoneMode==0:               #iPhone mode initiation
   for d in range(0,len(convoSplit)-1):
     if convoSplit[d] in iPhone:
         iPhoneMode=1
         convo=''
 if (iPhoneMode>0):
            convo,iPhoneMode,convoiPhoneC=iPhone_mode.iPhone(iPhoneMode,a,convo,convoiPhoneC)
            p=p+1                               #iPhone mode
 teach1=0
 if (convocopy in Wassup or convocopy in YouWish or convocopy in HowUDoin or hey>0)and st!=1:
                 teach1+=1   
                 for d in range(0,len(convoSplit)):
                     if convoSplit[d] in Bad:
                         bad=bad+1
                     if convoSplit[d] in Bad2:
                         bad=3
                     if convoSplit[d] in Bad3:
                         bad=10
                 if bad>9:
                     if a%2==0:
                         print(Oh[b-1]+','+sorry[a])
                     else:
                         print(sorry[a])
                     p=p+1        
                 elif bad==2 or p>1:
                       print(Oh[a])
                       p=p+1
                 elif bad>2 and bad<10:
                       print(Exclamtion2[a])
                       p=p+1
                 elif len(convoSplit)>1:
                       print(Exclamation[a])
                       p=p+1
 for d in range(0,len(convoSplit)):
     if d==len(convoSplit)-2 and p==0:
            print(NotUnderstood[a])             #NotUnd edit

 badd=bad        
 bad=0           
 p=0
 keyword=''
 reply=''
 modestCount=0
 hey=0
 nope=0
 
 if end>0:
     break
 if iPhoneMode<2:
  print("\n")
  print(Name)
 if loop>0:
  convocopy=convo
 if iPhoneMode<2: 
   convo=input()
 convo=re.sub(r'[,;\s]',' ',convo)
 convoSplit,shortform=jarvis.shortform(convo,convocopy,shortform)    
 convo=convo.lower()
 if shortform==0:
     convoSplit = re.sub("[^\w]", " ",  convo).split()
 convocopySplit = re.sub("[^\w]", " ",  convocopy).split()
 shortform=0
 if loop>1000:
     loop=10
     st=10
 st=st+1
 loop=loop+1
