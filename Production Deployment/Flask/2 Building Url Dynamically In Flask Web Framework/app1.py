from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my youtube channel'

@app.route('/sucess/<int:score>')
def sucess(score):
    return 'This person has passed and the marks is '+str(score)+'<html><body><h1>HTML TAG</h1></body></html>'

@app.route('/fail/<int:socre>')
def fail(score):
    return 'This person has failed and the marks is '+str(score)

# result checker
@app.route('/results/<int:marks>')
def results(marks):
    results = ''
    if marks<50:
        results='fail'
    else:
        results='sucess'
    return redirect(url_for(results,score=marks))  
        
if __name__=='__main__':
    app.run(debug=True)