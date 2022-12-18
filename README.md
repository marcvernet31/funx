# Funx
L'interpret de Funx és un projecte desenvolupat per a l'assignatura de [Llenguatges de Programació](https://www.fib.upc.edu/ca/estudis/graus/grau-en-enginyeria-informatica/pla-destudis/assignatures/LP) de la UPC. Aquest projecte consisteix en desenvolupar un intèrpret per a Funx. Funx és un llenguatge ideat especificament per aquest projecte i molt simple, les especificacions es poden trobar [aqui](https://github.com/gebakx/lp-funcions). A més a més, el projecte també conté una interfície gràfica a través de la qual es pot interactuar amb el llenguatge.


## El llenguatge
La gramatica del llenguatge esta descrita amb [ANTLR4](https://www.antlr.org/) i implementat completament amb Python. 
Les especificacions del llenguatge es poden trobar en l'enunciat original, però un resum de les funcionalitats amb caracteristiques particulars de la implementació:
```
# expressions
3 + 4  # 7
3 * 4  # 12
3 / 0  # None (Divisions per zero retornen 'none' com a error)

# assignació
x <- 1  
y <- x + 1
z <- 5*7

# condicionals
# Operadors disponibles =, !=, <, >, <=, >=
x = 0  # 1 (les expressions retornen 1 per cert i 0 per fals)
x = 3  # 0
if x = y { z <- 1 }
if x = y { z <- 1 } else { z <- 2 }

# iteració
while a > 0 { a <- a / 2 }

# declaració de funcions
# Les funcions poden declarar variables internes
Mul x y {x * y}
Op x y { 
	a <- x + 1 
	b <- y + 1 
	a + b 
}

# evaluar funcions
Mul 3 3  # 9

```

Els blocs d'expressions (delimitats per `{}`) poden contenir multiples expressions en tots elc casos (funcions, `while`, `if` i `else`). El bloc retorna com a resultat el valor de l'evaluació l'última expressió.

L'intèrpret de Funx és capaç de detectar els seguents errors
	- Divisió per zero
    - Nom repetit de variable en la declaració d'una funció 
    - La funció cridada no existeix
    - Nombre de variables incorrecte en la crida d'una funció


## La interfície
La interfície web es la eina que permet a l'usuari executar comandes de Funx. Esta construida en Python utilitzant el framework Flask. També té alguns detalls afegits amb la llibreria de css [Bulma](https://bulma.io/), per fer-ne l'estètica una mica més atractiva. 

![Captura de pantalla de l'interfície](file:///ui.png)

La part principal és la Consola, on l'usuari pot introduir comandes individuals de Funx i executar-les amb un click.  Un cop executat, tant la comanda com el seu resultat es mostren a l'esquerra. Totes les funcions declarades es mostren a l'apartat de Funcions.
 
Les funcions declarades que ja existien es sobreescriuen.

Com a funcionalitat extra, hi ha un botó "Clear" que serveix per esborrar l'historial de comandes i les funcions declarades. Tant les funcions com l'historial de comandes s'emmagatzemen en fitxes json externs, als quals s'accedeix mitjançant la llibreria [tinydb](https://tinydb.readthedocs.io/en/latest/). D'aquesta manera, el context de l'usuari no es perd entre sessions.

## Instruccions d'us

```
# Construir els visitadors a partir de la gramàtica
$> antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g

# Iniciar l'aplicació Flask
$> flask --app base run
```
Un cop iniciada l'aplicació Flask, es pot accedir a `http://localhost:5000/`.
