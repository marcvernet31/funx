if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor


global variables
variables = {}

global funcions
funcions = {}

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
        print("Out: ", self.visit(l[0]))

    def visitParentExpr(self, ctx):
        l = list(ctx.getChildren())        
        return self.visit(l[1])

    def visitAssignacio(self, ctx):
        l = list(ctx.getChildren())
        variable = l[0].getText()
        valor = self.visit(l[2])
        variables[variable] = valor


    ##### IGUALTATS #####
    def visitIgualtatInput(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]))
    
    def visitIgualtat(self, ctx):
        l = list(ctx.getChildren())

        # Extreu valor de l'esquerra
        valor_1 = 0
        if l[0].getText() in variables: valor_1 = variables[l[0].getText()]

        # Extreu valor de la dreta
        valor_2 = 0
        if FunxParser.symbolicNames[l[2].getSymbol().type] == 'NUM': valor_2 = int(l[2].getText())
        elif l[2].getText() in variables: valor_2 = variables[l[2].getText()]
        
        # Calcula la igualtat
        if l[1].getText() == '=': return int(valor_1 == valor_2)
        if l[1].getText() == '!=': return int(valor_1 != valor_2)
        if l[1].getText() == '<': return int(valor_1 < valor_2)
        if l[1].getText() == '>': return int(valor_1 > valor_2)
        if l[1].getText() == '<=': return int(valor_1 <= valor_2)
        if l[1].getText() == '>=': return int(valor_1 >= valor_2)


    ##### CONDICIONAL #####
    def visitCondicionalInput(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]))

    def visitCondicional(self, ctx):
        l = list(ctx.getChildren())
        cond = self.visit(l[1])

        if cond: self.visit(l[3])
        elif len(l) > 5: self.visit(l[7])


    ##### WHILE #####
    def visitIteracioInput(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]))

    def visitIteracio(self, ctx):
        l = list(ctx.getChildren())
        cond = self.visit(l[1])
        while cond:
            for i in range(3, len(l)-1): self.visit(l[3])
            cond = self.visit(l[1])


    ##### FUNCIONS #####
    def visitDecFuncioInput(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]))

    def visitDecFuncio(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        variablesInput = []
        expressions = []

        i = 1
        # Extreu variables
        while l[i].getText() != '{': 
            variablesInput += [l[i].getText()]
            i += 1
        i += 1 # avoid  {
        # Extreu expressions
        while l[i].getText() != '}':
            print(l[i].getText())
            expressions += [l[i]]  
            i += 1

        #print(nom, " -> ", variablesInput, " ->  exp: ", len(expressions))
        funcions[nom] = Funcio(nom, expressions, variablesInput)


    def visitEvFuncioInput(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]))

    def visitEvFuncio(self, ctx):
        # Suma x y {x + y}
        # Suma (2 * 3) 4 
        # Fibo n { if n < 2 { n } (Fibo n-1) + (Fibo n-2)}
        # Euclides a b {while a != b{if a > b {a <- a - b}else{b <- b - a}}a}
        l = list(ctx.getChildren())
        nom = l[0].getText()
        valors = []
        for val in l[1:]:
            valors += [self.visit(val)]

        if nom in funcions:
            funcio = funcions[nom]
            if len(funcio.variables) != len(valors): print('error variables incorrectes')
            else:
                ## guarda les variables globals per recuperar despres
                ## Afegeix les variables locals al registre de variables global 
                # per ser utilitzades
                global variables
                variables_originals = variables
                variables_locals = {}
                for i in range(len(valors)): variables_locals[funcio.variables[i]] = valors[i]
                variables = variables_locals
                
                # Executa les expressions i emmagatzema l'output
                output = 0
                for expr in funcio.expr: 
                    #print(self.visit(expr))
                    output = self.visit(expr)
               
                variables = variables_originals
                return output

        else:
            print('error nom no trobat')


    ##### OPERACIONS #####

    def visitMultiplicacio(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]) * self.visit(l[2]))

    def visitDivisio(self, ctx):
        # possible error al dividir per zero?
        l = list(ctx.getChildren())
        num = self.visit(l[0])
        den = self.visit(l[2])
        if den == 0: print('Error')
        else:
            return(num // den)

    def visitPotencia(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]) ** self.visit(l[2]))

    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]) + self.visit(l[2]))

    def visitResta(self, ctx):
        l = list(ctx.getChildren())
        return(self.visit(l[0]) - self.visit(l[2]))


    ##### VALORS I VARIABLES #####

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        if l[0].getText() in variables: return variables[l[0].getText()]
        else: return 0
