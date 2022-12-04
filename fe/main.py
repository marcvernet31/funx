from flask import Flask, render_template, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')


def getFuncions():
    # [{'name': 'Suma'}]
    output = []
    for entry in db.all():
        output.append(entry['name'])
    return output

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    db.insert({'name': text})
    return render_template('index.html', funcions=getFuncions())

@app.route("/")
def index():
    funcions = getFuncions()
    return render_template('index.html', funcions=funcions)
