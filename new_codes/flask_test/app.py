from flask import Flask
from flask import render_template
app = Flask(__name__) #플래스크 클래스를 가져옵닌다. 


@app.route('/') 
def index():
    return render_template('index.html', greeting="Do it! 파이썬 생활프로그래밍//김창현")
