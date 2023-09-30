from flask import Flask
from flask import render_template
app = Flask(__name__) #플래스크 클래스를 가져옵닌다. 


@app.route('/') 
def index():
    return render_template('index.html', greeting="우리 웹사이트에 온 것을 환영합니다")
