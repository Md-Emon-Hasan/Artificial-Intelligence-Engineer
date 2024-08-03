from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome To My Youtube Channel. Please subscribe my channel'

@app.route('/member')
def member():
    return 'welcome to my Youtube channel memeber'

if __name__=='__main__':
    app.run(debug=True)