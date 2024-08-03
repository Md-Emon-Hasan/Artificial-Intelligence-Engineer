from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return '<h1>Welcome to my youtube channel</h1>'

@app.route('/index',methods=['GET'])
def index():
    return 'welcome to index page'

# variable rule
@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the score is: '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the socre is: '+str(score)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        # return render_template('form.html',score=average_marks)
        if average_marks>=50:
            res='success'
        else:
            res='fail'
        return redirect(url_for(res,score=average_marks))

if __name__=='__main__':
    app.run(debug=True)
