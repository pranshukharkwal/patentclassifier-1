from flask import Flask,url_for,render_template,request
import requests
from sklearn.feature_extraction.text import CountVectorizer
import joblib
from bs4 import BeautifulSoup
import pandas as pd
from lxml.html import fromstring
from itertools import cycle
import traceback

def prediction(title):
        cv = joblib.load('count_vect')
        clf = joblib.load('finalmodel.sav')
        text = [title]
        vect = cv.transform(text).toarray()
        prediction = clf.predict(vect)[0]
        return prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select',methods=['POST'])
def Select():
    if request.method == 'POST' :
        if request.form['options'] == 'SNumber' :
            print(request.form['options'])
            return render_template('SNumber.html')
        
        elif request.form['options'] == 'SText':
            print(request.form['options'])
            return render_template('SText.html')

        else:
            return render_template('index.html',Error = 'Please Select a Valid Option')

@app.route('/predictN',methods = ['POST'])
def predictN():
    if request.method == 'POST':
        user_input = request.form['input']
        def showtitle(pubno):
            URL = "http://patents.google.com/patent/" + pubno  + "/en?oq=" + pubno
            r = requests.get(URL)
            soup = BeautifulSoup(r.content , 'html5lib')
            title = str((soup.find('h1').text).split(' - ')[1])[:-9]  #For title
            return title
        title = showtitle(user_input)
        predict = prediction(title)
        return render_template('result.html', title = title, prediction = predict)

@app.route('/predictT',methods = ['POST'])
def predictT():
    if request.method == 'POST':
        title = request.form['title']
        predict = prediction(title)
        return render_template('result.html',title = title, prediction = predict)

if __name__ == '__main__':
    app.run(debug = True)

#Flask By default looks in templates folder for templates/
#Else app = Flask(__name__ , template_folder = <FolderName>)
# Flask uses Static folder to store css, js and image files
