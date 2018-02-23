import urllib.request
import re
from flask import Flask
iPhoneJ=["Okay, I'm on your iPhone","iPhone mode on, let's rock!","Yes!, I love to work from iPhone"]

def iPhone(iPhoneMode,a,convo,convoiPhoneC):
            pun=''
            convoiPhone=''
            iPhoneMode=iPhoneMode+1
            if iPhoneMode>100:
                iPhoneMode=10
            if iPhoneMode==2:
                print(iPhoneJ[a])

            app=Flask(__name__)
            @app.route('/')
            def home():
                return 'Hello World'
            @app.route('/<convoiPhone>')
            def about():
                return 'subpage'
            if __name__=='__main__':
                app.run(host='0.0.0.0',port=8084)
            
            if  convoiPhoneC!=convoiPhone:
                        convo=convoiPhone
                        print("\n")
                        print("You","\n")
                        print(convo,"\n")
                        print("Jarvis")
            else:
                convo=''
            convoiPhoneC=convoiPhone
            return convo,iPhoneMode,convoiPhoneC
