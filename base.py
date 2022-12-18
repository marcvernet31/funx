import re
import sys
from antlr4 import *
from tinydb import TinyDB, Query
from flask import Flask, render_template, request, url_for, redirect

from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor

app = Flask(__name__)

# Emmagatzematge per a les funcions declarades
db_fun = TinyDB('db_fun.json')
# Emmagatzematge per a l'output
db_out = TinyDB('db_out.json')


# Obté funcions declarades de db_fun.json
def getFuncions():
    return [o["id"] for o in db_fun.all()]


# Obté outputs de db_out.json
def getResults():
    return db_out.all()


# Interpreta expressions en Funx i en retorna el resultat 
def interpret(inputString: str):
    # Ignora comentaris
    inputString = re.sub('#.*?\r', '', inputString)
    # Ignora salts de línia
    input_stream = InputStream(inputString.replace('\r', ''))

    lexer = FunxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)
    tree = parser.root() 
    visitor = TreeVisitor()
    output = visitor.visit(tree)

    # Comprova si l''input és la declaració d'una funció
    if (type(output) is str) and ("Funció declarada" in output): 
        identificador = output.split(': ')[1]
        Function = Query()
        db_fun.remove(Function.id == identificador)
        db_fun.insert({"id": identificador})

    db_out.insert({"index": len(db_out.all()), "input": inputString, "output": output})


@app.route('/', methods=['POST'])
def postExpression():
    text = request.form['text']
    interpret(text)
    return render_template('base.html', funcions=getFuncions(), outputs=getResults())


@app.route('/delete', )
def clearStorage():
    db_out.drop_tables()
    db_fun.drop_tables()
    return redirect('/')


@app.route("/")
def index():
    funcions = getFuncions()
    return render_template('base.html', funcions=getFuncions(), outputs=getResults())
