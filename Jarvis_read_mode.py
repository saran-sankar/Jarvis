from Program_Files.language import*
from Program_Files import finders
import re
def Jarvis_read(convoSplit):
        bookName=''
        book_Library=['A Game of Thrones.txt','A Clash of Kings.txt']
        for i in range(len(convoSplit)):
            if convoSplit[i] in read_book:
               for j in range (i+1,len(convoSplit)):
                if j==len(convoSplit)-1:
                    bookName+=convoSplit[j]+'.txt'
                else:
                    bookName+=convoSplit[j]+' '
        bookName=finders.element_finder(book_Library,bookName)
        if bookName==' ' or bookName=='':
            print('Not found!')
            return 1
        print("Reading mode on")
        print("Reading"+" "+bookName)
        print("Completed!\n")
        while "back" not in convoSplit:
                print("\nYou")
                convo=input().lower()
                print("\nJarvis")
                convoSplit = re.sub("[^\w]|\.", " ",  convo).lower().split()
                file=open("/Users/me/Desktop/My_Stuff/Jarvis/Program_Files/pos/"+bookName)
                sentances=re.sub(" ","_",re.sub("[0-9]|\'","",file.read())).rstrip().split()
                for i in range(len(convoSplit)):
                  if convoSplit[i] in question:
                      isare=convoSplit[i+1]
                      name=convoSplit[i+2]
                for ii in range(len(sentances)):
                   f=re.sub("_"," ",sentances[ii]).lower().split()
                   for i in range(len(f)-1):
                        if f[i] == name and f[i+1]== isare:
                               sentance=(re.sub("_"," ",sentances[ii])).lower().split()
                               for j in range(len(sentance)):
                                    if sentance[j] == name and sentance[j+1]== isare:
                                         answer=''
                                         while j != len(sentance)-1 :
                                              answer+=f[j]+" "
                                              j+=1
                                         print(answer)
                               break
        return 1                     



        

