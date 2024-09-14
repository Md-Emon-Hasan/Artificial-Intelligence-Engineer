### Building Url dynamically
### variable rlues and url building

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my youtube channel'

@app.route('/sucess/<int:score>')
def sucess(score):
    return 'This preson has passed and the marks is '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'This person has failed and the marks is '+str(score)

# result checker
@app.route('/results/<int:score>')
def results(score):
    if score<50:
        results='fail'
    else:
        results='sucess'
    return results

if __name__=='__main__':
    app.run(debug=True)