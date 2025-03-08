# python -m pytest test.py -v

from Practica import validate, check_parenthesis, to_postfix, calculate

class TestValidate:
    def test_expresion_vacia(self):
        assert validate("") == False
    
    def test_expresion_valida_simple(self):
        assert validate("a+b") == True
    
    def test_expresion_valida_compleja(self):
        assert validate("(a+b)*(c-d)") == True
    
    def test_expresion_invalida_inicio(self):
        assert validate("+a") == False
    
    def test_expresion_invalida_fin(self):
        assert validate("a+") == False
    
    def test_expresion_invalida_operadores_consecutivos(self):
        assert validate("a++b") == False
    
    def test_expresion_invalida_variables_consecutivas(self):
        assert validate("ab+c") == False
    
    def test_expresion_invalida_caracter_no_permitido(self):
        assert validate("a+2") == False
    
    def test_expresion_valida_con_parentesis(self):
        assert validate("(a+b)") == True
    
    def test_expresion_valida_compleja_variables(self):
        assert validate("a+b*c^d/e") == True


class TestCheckParenthesis:
    def test_parentesis_balanceados(self):
        assert check_parenthesis("(a+(b*c))") == True
    
    def test_parentesis_no_balanceados_falta_cierre(self):
        assert check_parenthesis("(a+(b*c)") == False
    
    def test_parentesis_no_balanceados_falta_apertura(self):
        assert check_parenthesis("a+(b*c))") == False
    
    def test_sin_parentesis(self):
        assert check_parenthesis("a+b*c") == True
    
    def test_parentesis_anidados(self):
        assert check_parenthesis("((((a))))") == True
    
    def test_expresion_con_parentesis_vacios(self):
        assert check_parenthesis("()") == True
    
    def test_expresion_parentesis_intercalados(self):
        assert check_parenthesis("()(()())") == True


# Tests para la función to_postfix
class TestToPostfix:
    def test_expresion_simple(self):
        assert to_postfix("a+b") == "ab+"
    
    def test_expresion_con_precedencia(self):
        assert to_postfix("a+b*c") == "abc*+"
    
    def test_expresion_con_parentesis(self):
        assert to_postfix("(a+b)*c") == "ab+c*"
    
    def test_expresion_compleja(self):
        assert to_postfix("a+b*c-d/e^f") == "abc*+def^/-"
    
    def test_expresion_multiple_parentesis(self):
        assert to_postfix("(a+b)*(c-d)") == "ab+cd-*"
    
    def test_parentesis_anidados(self):
        assert to_postfix("((a+b)*c)") == "ab+c*"
    
    def test_expresion_todos_operadores(self):
        assert to_postfix("a^b*c/d+e-a") == "ab^c*d/e+a-"
    
    def test_expresion_solo_variable(self):
        assert to_postfix("a") == "a"
    
    def test_expresion_parentesis_vacios(self):
        # En un caso real, esto podría no ser una expresión válida,
        # pero la función to_postfix debería manejarla
        assert to_postfix("()") == ""

class TestCalculate:
    def test_expresion_simple_suma(self):
        # a+b -> ab+
        expresion = "ab+"
        valores = {"a": 5, "b": 3}
        assert calculate(expresion, valores) == 8
    
    def test_expresion_simple_resta(self):
        # a-b -> ab-
        expresion = "ab-"
        valores = {"a": 10, "b": 4}
        assert calculate(expresion, valores) == 6
    
    def test_expresion_simple_multiplicacion(self):
        # a*b -> ab*
        expresion = "ab*"
        valores = {"a": 7, "b": 6}
        assert calculate(expresion, valores) == 42
    
    def test_expresion_simple_division(self):
        # a/b -> ab/
        expresion = "ab/"
        valores = {"a": 20, "b": 5}
        assert calculate(expresion, valores) == 4
    
    def test_expresion_simple_potencia(self):
        # a^b -> ab^
        expresion = "ab^"
        valores = {"a": 2, "b": 3}
        assert calculate(expresion, valores) == 8
    
    def test_expresion_compleja_ejemplo_enunciado(self):
        # a+(b*c+d)-e -> abc*d++e-
        expresion = "abc*d++e-"
        valores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
        # Resultado esperado: 1+(2*3+4)-5 = 6
        assert calculate(expresion, valores) == 6
    

    

