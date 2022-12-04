# Generated from Funx.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
else:
    from FunxParser import FunxParser

# This class defines a complete generic visitor for a parse tree produced by FunxParser.

class FunxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FunxParser#root.
    def visitRoot(self, ctx:FunxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Igualtat.
    def visitIgualtat(self, ctx:FunxParser.IgualtatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Condicional.
    def visitCondicional(self, ctx:FunxParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Iteracio.
    def visitIteracio(self, ctx:FunxParser.IteracioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#DecFuncio.
    def visitDecFuncio(self, ctx:FunxParser.DecFuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#EvFuncio.
    def visitEvFuncio(self, ctx:FunxParser.EvFuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Assignacio.
    def visitAssignacio(self, ctx:FunxParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Variable.
    def visitVariable(self, ctx:FunxParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Divisio.
    def visitDivisio(self, ctx:FunxParser.DivisioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Multiplicacio.
    def visitMultiplicacio(self, ctx:FunxParser.MultiplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#ParentExpr.
    def visitParentExpr(self, ctx:FunxParser.ParentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#DecFuncioInput.
    def visitDecFuncioInput(self, ctx:FunxParser.DecFuncioInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Valor.
    def visitValor(self, ctx:FunxParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Suma.
    def visitSuma(self, ctx:FunxParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#CondicionalInput.
    def visitCondicionalInput(self, ctx:FunxParser.CondicionalInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#EvFuncioInput.
    def visitEvFuncioInput(self, ctx:FunxParser.EvFuncioInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#IteracioInput.
    def visitIteracioInput(self, ctx:FunxParser.IteracioInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#IgualtatInput.
    def visitIgualtatInput(self, ctx:FunxParser.IgualtatInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Potencia.
    def visitPotencia(self, ctx:FunxParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Resta.
    def visitResta(self, ctx:FunxParser.RestaContext):
        return self.visitChildren(ctx)



del FunxParser