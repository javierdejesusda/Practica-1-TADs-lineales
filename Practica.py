from Stack import Stack

def validate(expresion: str) -> bool:
    
    #Complejidad O(n)
    #Complejidad O(e)
    
    variables: set[str] = set("abcde")
    operadores: set[str] = set("*^+-/")
    parentesis: set[str] = set("()")
    
    if not expresion or \
       expresion[0] not in variables | parentesis or \
       expresion[-1] not in variables | parentesis:
        return False
    for actual, siguiente in zip(expresion, expresion[1:]):
        if (actual in variables and siguiente not in operadores | {')'}) or \
           (actual == ')' and siguiente not in operadores | {')'}) or \
           (actual in operadores and siguiente not in variables | {'('}) or \
           (actual == '(' and siguiente not in variables | {'('}) or \
           (actual not in variables | operadores | parentesis):
            return False
    
    return True



def check_parenthesis(expresion: str) -> bool:
    
    #Complejidad O(n)
    #Complejidad O(e)
    
    pila = Stack()

    # comentario de prueba
    
    for elemento in expresion:
        if elemento == "(":
            pila.push(elemento)
        elif elemento == ")":
            if pila.empty():
                return False
            pila.pop()
    
    return pila.empty()



def to_postfix(expresion: str) -> str:
    
    #Complejidad O(n)
    #Complejidad O(e)
    
    pila = Stack()
    postfija: list[str] = []
    operadores: dict[str, int] = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}

    for elemento in expresion:
        if elemento.isalpha():
            postfija.append(elemento)
        elif elemento == "(":
            pila.push(elemento)
        elif elemento == ")":
            while not pila.empty() and pila.peek() != "(":
                postfija.append(pila.pop())
            pila.pop()
        elif elemento in operadores:
            while not pila.empty() and pila.peek() in operadores and \
                operadores[pila.peek()] >= operadores[elemento]:
                postfija.append(pila.pop())
            pila.push(elemento)

    while not pila.empty():
        postfija.append(pila.pop())

    return "".join(postfija)



def read_line(file) -> tuple[float] | None: 
    
    # Complejidad O(n)
    # O(e)
    
        line = file.readline() 
        if line == '': 
            return None 
        else: 
            values: list = line.split(',') 
            for i in range(len(values)): 
                values[i] = float(values[i]) 
            return tuple(values) 
        
        
    
def calculate(expresion: str, valores: dict[str, float]) -> int:
    
    # Complejidad O(n)
    # O(e)
    
    pila = Stack()
    operadores = {"^": lambda a, b: a ** b,
                  "*": lambda a, b: a * b,
                  "/": lambda a, b: a // b,
                  "+": lambda a, b: a + b,
                  "-": lambda a, b: a - b}

    for elemento in expresion:
        if elemento.isalpha():  
            pila.push(valores[elemento])
        elif elemento in operadores:  
            b, a = pila.pop(), pila.pop()
            pila.push(operadores[elemento](a, b))

    return pila.pop()



    
def insertar_valor(acumulado, elemento):
    
    # Complejidad O(log k)
    
    izquierda, derecha = 0, len(acumulado)
    
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if acumulado[medio][0] < elemento[0]:
            derecha = medio 
        else: 
            izquierda = medio + 1
    acumulado.insert(izquierda, elemento)

  
    
def main():
    
    # Complejidad O(n * m * log k)
    # O(nl * l * log k)

    expresion = str(input("Introduzca la expresión: "))

    if not validate(expresion):
        print("Estructura incorrecta")
        return
    if not check_parenthesis(expresion):
        print("Paréntesis incorrectos")
        return

    postfija = to_postfix(expresion)
    print(f"Notación postfija: {postfija}")

    fichero = str(input("Introduzca el nombre del fichero en el que están los datos: "))
    k_valores = int(input("Introduzca el número k de valores más altos que desea: "))
    acumulado = []

    with open(fichero, "r") as file:
        for elementos in iter(lambda: read_line(file), None):  
            valores = dict(zip("abcde", elementos))
            resultado = calculate(postfija, valores)

            if len(acumulado) < k_valores:
                insertar_valor(acumulado, (resultado, valores))
            elif resultado > acumulado[-1][0]:
                acumulado.pop()
                insertar_valor(acumulado, (resultado, valores))

    for resultado, valores in acumulado:
        print(f"{resultado:.4f} para los valores: {tuple(valores.values())}")

if __name__ == "__main__":
    main()



