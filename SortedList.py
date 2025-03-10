## Insercción binaria, nos queda la complejidad en O(nl∗(l+e+k))
class SortedList:
    def __init__(self, k):
        self.k = k
        self.acumulado = []

    def insertar(self, valor, elementos):
        if len(self.acumulado) < self.k:
            self._insercion_binaria(valor, elementos)
        else:
            if valor > self.acumulado[-1][0]:
                self._insercion_binaria(valor, elementos)
                self.acumulado.pop()

    def _insercion_binaria(self, valor, elementos):
        izquierda, derecha = 0, len(self.acumulado)
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            if self.acumulado[medio][0] > valor:
                izquierda = medio + 1
            else:
                derecha = medio
        self.acumulado.insert(izquierda, (valor, elementos))

    def obtener_resultados(self):
        return self.acumulado
    
# Utilizando un min-heap nos queda la complejidad O(nl∗(l+e+log k))

"""
class SortedList:
    def __init__(self, k: int):
        self.k = k
        self.acumulado = [] 

    def _padre(self, indice: int) -> int:
        return (indice - 1) // 2

    def _hijo_izquierdo(self, indice: int) -> int:
        return 2 * indice + 1

    def _hijo_derecho(self, indice: int) -> int:
        return 2 * indice + 2

    def _intercambio(self, i: int, j: int):
        self.acumulado[i], self.acumulado[j] = self.acumulado[j], self.acumulado[i]

    def _heapify_arriba(self, indice: int):
        while indice > 0 and self.acumulado[indice][0] < self.acumulado[self._padre(indice)][0]:
            self._intercambio(indice, self._padre(indice))
            indice = self._padre(indice)

    def _heapify_abajo(self, indice: int):
        menor = indice
        izquierda = self._hijo_izquierdo(indice)
        derecha = self._hijo_derecho(indice)


        if izquierda < len(self.acumulado) and self.acumulado[izquierda][0] < self.acumulado[menor][0]:
            menor = izquierda
        if derecha < len(self.acumulado) and self.acumulado[derecha][0] < self.acumulado[menor][0]:
            menor = derecha


        if menor != indice:
            self._intercambio(indice, menor)
            self._heapify_abajo(menor)

    def insertar(self, resultado: float, valores: dict[str, float]):
        if len(self.acumulado) < self.k:
            self.acumulado.append((resultado, valores))
            self._heapify_arriba(len(self.acumulado) - 1)
        else:
            if resultado > self.acumulado[0][0]:
                self.acumulado[0] = (resultado, valores)
                self._heapify_abajo(0)

    def obtener_resultados(self):
        return sorted(self.acumulado, reverse=True, key=lambda x: x[0])

        """
