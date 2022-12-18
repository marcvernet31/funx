if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

# Emmagatzema un log d'errors per a cada execució
global errors
errors = []

# Emmagatzema les variables declarades i el seu valor
global variables
variables = {}

# Emmagatzema les funcions declarades
global funcions
funcions = {}

# Possibles errors
possibleErrors = [
    "Error: Divisió per zero", 
    "Error: Nom repetit de variable", 
    "Error: La funció cridada no existeix",
    "Error: Nombre de variables incorrecte"
]


class Funcio():
    def __init__(self, nom, expr, variables):
        self.nom = nom 
        self.expr = expr
        self.variables = variables
        self.variables_locals = {}
    def initDict(self):
        for var in self.variables:
            self.variables_locals[var] = 0


class TreeVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        output = self.visit(l[0])

        global errors
        if len(errors) != 0: 
            output = errors[0]
            errors = []
        return output
  
    def visitParentExpr(self, ctx):
        l = list(ctx.getChildren())        
        return self.visit(l[1])

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitAssignacio(self, ctx):
        l = list(ctx.getChildren())
        valor = self.visit(l[2])
        # Evitar assignar None en cas de divisió per zero
        if valor == None: valor = 0
        variables[l[0].getText()] = valor
    
    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        if l[0].getText() in variables: return variables[l[0].getText()]
        else: return 0

    def visitIgualtat(self, ctx):
        l = list(ctx.getChildren())

        valor_1 = self.visit(l[0])
        sym = l[1].getText()
        valor_2 = self.visit(l[2])

        if sym == '=':  return int(valor_1 == valor_2)
        if sym == '!=': return int(valor_1 != valor_2)
        if sym == '<':  return int(valor_1 < valor_2)
        if sym == '>':  return int(valor_1 > valor_2)
        if sym == '<=': return int(valor_1 <= valor_2)
        if sym == '>=': return int(valor_1 >= valor_2)

    def visitCondicional(self, ctx):
        l = list(ctx.getChildren())
        condicio = self.visit(l[1])
        if condicio == 1: return self.visit(l[3])
        # Executa en cas de condició falsa i expressió a else
        elif len(l) > 5: return self.visit(l[7])

    def visitIteracio(self, ctx):
        l = list(ctx.getChildren())
        condicio = self.visit(l[1])

        while condicio == 1:
            # executa totes les expressions del bloc
            for i in range(3, len(l)-1): self.visit(l[3])
            # actualitza el valor de la condició 
            condicio = self.visit(l[1]) 

    def visitDecFuncio(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        variablesInput = []
        expressions = []

        i = 1 # Nom 
        # Extreu variables
        while l[i].getText() != '{': 
            variablesInput += [l[i].getText()]
            i += 1
        i += 1 # {
        # Extreu expressions
        while l[i].getText() != '}':
            expressions += [l[i]]  
            i += 1

        # Comprova si hi ha variables repetides
        if len(variablesInput) != len(set(variablesInput)):
            errors.append(possibleErrors[1])
            return None

        # Emmagatzema la funció 
        funcions[nom] = Funcio(nom, expressions, variablesInput)
        return f"Funció declarada: {nom} {' '.join(variablesInput)}"

    def visitEvFuncio(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        # Extreu valors per als paramatres
        valors = []
        for val in l[1:]:
            valors += [self.visit(val)]

        if nom in funcions:
            funcio = funcions[nom]
            if len(funcio.variables) != len(valors): errors.append(possibleErrors[3])
            else:
                # Guarda les variables globals per recuperar despres.
                # Afegeix les variables locals al registre de variables global per ser utilitzades
                global variables
                variables_originals = variables
                variables_locals = {}
                for i in range(len(valors)): variables_locals[funcio.variables[i]] = valors[i]
                variables = variables_locals
                
                # Executa les expressions i emmagatzema l'output
                output = 0
                for expr in funcio.expr: 
                    output = self.visit(expr)
                    if output != None: 
                        variables = variables_originals
                        return output
               
                # Retorna les variables global
                variables = variables_originals
                return output
        else:
            errors.append(possibleErrors[2])

    def visitMultiplicacio(self, ctx):
        l = list(ctx.getChildren())
        try: return(self.visit(l[0]) * self.visit(l[2]))
        except: None

    def visitDivisio(self, ctx):
        l = list(ctx.getChildren())
        num = self.visit(l[0])
        den = self.visit(l[2])
        try:
            return(num // den)
        except: 
            errors.append(possibleErrors[0])
            return None

    def visitPotencia(self, ctx):
        l = list(ctx.getChildren()) 
        try: return(self.visit(l[0]) ** self.visit(l[2]))
        except: None

    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        try: return(self.visit(l[0]) + self.visit(l[2]))
        except: None

    def visitResta(self, ctx):
        l = list(ctx.getChildren())
        try: return(self.visit(l[0]) - self.visit(l[2]))
        except: None
