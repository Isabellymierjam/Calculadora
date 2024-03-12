numero_1 = int(input("informe o primeiro número"))
numero_2 = int(input("informe o segundo número"))
operador= input("informe o operador\n+ adição\n- subtração\n* multiplicação\n/ divisão\n=>")

if operador == "+":
    resultado = numero_1 + numero_2
elif operador == "-":
    resultado = numero_1 - numero_2
elif operador == "*":
    resultado = numero_1 * numero_2
elif operador == "/":
    resultado = numero_1 / numero_2
else:
    print( "Operação inválida")

def adição(a,b):
    return a+b

def divisão(a,b):
    if b != 0:
        return a/b
    else:
        return " Não é possível..."

def multiplicação(a,b):
     return a*b

def subtração(a,b):
    return a-b

if operador == "+":
    print("o resultado é", adição(numero_1,numero_2))
if operador == "/":
    print("o resultado é", divisão(numero_1,numero_2))
if operador == "*":
    print("o resultado é", multiplicação(numero_1,numero_2))
if operador == "-":
    print("o resultado é", subtração(numero_1,numero_2))


