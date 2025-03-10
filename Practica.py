from Stack import Stack
from SortedList import SortedList

def validate(expresion: str) -> bool:

    variables: set[str] = set("abcde")
    operadores: set[str] = set("*^+-/")
    parentesis: set[str] = set("()")

    if (
        not expresion
        or expresion[0] not in variables | parentesis
        or expresion[-1] not in variables | parentesis
    ):
        return False
    for actual, siguiente in zip(expresion, expresion[1:]):
        if (
            (actual in variables and siguiente not in operadores | {")"})
            or (actual == ")" and siguiente not in operadores | {")"})
            or (actual in operadores and siguiente not in variables | {"("})
            or (actual == "(" and siguiente not in variables | {"("})
            or (actual not in variables | operadores | parentesis)
        ):
            return False

    return True


def check_parenthesis(expresion: str) -> bool:

    pila = Stack()

    for elemento in expresion:
        if elemento == "(":
            pila.push(elemento)
        elif elemento == ")":
            if pila.empty():
                return False
            pila.pop()

    return pila.empty()


def to_postfix(expresion: str) -> str:

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
            while (
                not pila.empty()
                and pila.peek() in operadores
                and operadores[pila.peek()] >= operadores[elemento]
            ):
                postfija.append(pila.pop())
            pila.push(elemento)

    while not pila.empty():
        postfija.append(pila.pop())

    return "".join(postfija)


def read_line(file) -> tuple[float] | None:
    
    line = file.readline()
    if line == "":
        return None
    else:
        values: list = line.split(",")
        for i in range(len(values)):
            values[i] = float(values[i])
        return tuple(values)


def calculate(expresion: str, valores: dict[str, float]) -> int:
    
    pila = Stack()
    operadores = {
        "^": lambda a, b: a**b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }

    for elemento in expresion:
        if elemento.isalpha():
            pila.push(valores[elemento])
        elif elemento in operadores:
            b, a = pila.pop(), pila.pop()
            pila.push(operadores[elemento](a, b))

    return pila.pop()


def main():
    expresion = input("Introduzca la expresión: ")

    if not validate(expresion):
        print("Estructura incorrecta")
        return

    if not check_parenthesis(expresion):
        print("Paréntesis incorrectos")
        return

    postfija = to_postfix(expresion)
    print(f"Notación postfija: {postfija}")

    fichero = input("Introduzca el nombre del fichero en el que están los datos: ")
    k_valores = int(input("Introduzca el número k de valores más altos que desea: "))

    sorted_list = SortedList(k_valores)

    with open(fichero, "r") as file:
        for elementos in iter(lambda: read_line(file), None):
            valores = dict(zip("abcde", elementos))
            resultado = calculate(postfija, valores)
            sorted_list.insertar(resultado, valores)

    for resultado, valores in sorted_list.obtener_resultados():
        print(f"{resultado:.5f} para los valores: {tuple(valores.values())}")


if __name__ == "__main__":
    main()


