import re
import sys
from antlr4 import *
from tinydb import TinyDB, Query
from flask import Flask, render_template, request, url_for, redirect

sys.path.append('../')
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor

app = Flask(__name__)

# Emmagatzematge per a les funcions declaredes
db_fun = TinyDB('db_fun.json')
# Emmagatzematge per l'output
db_out = TinyDB('db_out.json')


# Obté funcions declarades de db_fun.json
def getFuncions():
    output = []
    for entry in db_fun.all():
        output.append(entry['name'] + " " + ' '.join(entry['variables']))
    return output


# Obté outputs de db_out.json
# Format: {"index": '', "input": '', "output": ''}
def getResults():
    return db_out.all()


# Interpreta expressions en Funx i en retorna el resultat 
def interpret(inputString: str):
    # Ignopra comentaris
    inputString = re.sub('#.*?\r', '', inputString)
    # Ignora salts de línia
    input_stream = InputStream(inputString.replace('\r', ''))

    lexer = FunxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)
    tree = parser.root() 
    visitor = TreeVisitor()
    output = visitor.visit(tree)

    # L'input és la declaració d'una funció
    if type(output) is dict: 

        # Comprava si la funció ja existeix, i sobreescriu en
        Function = Query()
        if len(
            db_fun.search(Function.name == output['name'] 
            and Function.variables == output['variables'])
        ) != 0:
            db_fun.remove(Function.name == output['name'] and Function.variables == output['variables'])

        db_fun.insert(output)
        db_out.insert({"index": len(db_out.all()), "input": inputString, "output": "None"})
    else:
        db_out.insert({"index": len(db_out.all()), "input": inputString, "output": output})



@app.route('/', methods=['POST'])
def postExpression():
    text = request.form['text']
    interpret(text)
    return render_template('index.html', funcions=getFuncions(), outputs=getResults())


@app.route('/delete', )
def clearStorage():
    print('eeei')
    db_out.drop_tables()
    db_fun.drop_tables()
    return redirect('/')


@app.route("/")
def index():
    funcions = getFuncions()
    return render_template('index.html', funcions=getFuncions(), outputs=getResults())
