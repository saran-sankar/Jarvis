import webbrowser
from flask import Flask

def light(onOff):
    webbrowser.open('http://172.20.10.6:8084/'+onOff)
    app=Flask(__name__)
    @app.route('/')
    def home():
        return 'Hello World'
    @app.route('/on')
    def about():
        return 'on'
    if __name__=='__main__':
        app.run(host='0.0.0.0',port=8084)
def lights(onOff):
    light(onOff)
    
