#Aqui ficarão como as séries utilizadas para o calculo de cada função
#Fonte: https://en.wikipedia.org/wiki/Taylor_series
#Fonte: https://en.wikipedia.org/wiki/Leibniz_formula_for_π

def fatorial(n):
    if n < 1 :
        return 1
    else:
        return n * fatorial(n-1)

#e^x sendo x um número real calculado pela soma da série 1 + x + x^2/2! + x^3/3! + x^4/4! + ... + x^n/n!
def exponencialx(x):
    n = 50
    e = 1
    for i in range(1, n+1):
        e += (x**i)/fatorial(i)
    return e

#ln(x) esta quebrado
# (?) Considerar numeros negativos??? (A série seria diferente)  -1 < x < 1
#ln(x) sendo x um número real calculado pela soma da série x - x^2/2 + x^3/3 - x^4/4 + ... + (-1)^(n-1) * x^n/n
def ln_using_mercator(y):
    n = 100
    
    x = (y - 1) / (y + 1)
    ln_y = 0
    for i in range(n):
        ln_y += (1 / (2*i + 1)) * (x ** (2*i + 1))
    
    return 2 * ln_y

def log_base10(x):
    return ln_using_mercator(x) / ln_using_mercator(10)

def sqrt_newton(x, tolerance=1e-10):
    n = 100
    y = x
    for _ in range(n):
        y_next = 0.5 * (y + x / y)
        if abs(y - y_next) < tolerance:
            break
        y = y_next
    
    return y

#π sendo calculado pela série de Leibniz
def pi():
    n = 100000
    pi = 0
    for i in range(0, n):
        pi += ((-1)**i)/(2*i+1)
    return pi*4

#sen(x) sendo x um número real calculado pela soma da série x - x^3/3! + x^5/5! - x^7/7! + ... + (-1)^(n-1) * x^(2n-1)/(2n-1)!
def senx(x):
    n = 50
    sen = 0
    for i in range(1, n+1):
        sen += (((-1)**(i+1)) * (x**(2*i-1))/fatorial(2*i-1))
    return sen

#cos(x) sendo x um número real calculado pela soma da série 1 - x^2/2! + x^4/4! - x^6/6! + ... + (-1)^n * x^2n/(2n)!
def cosx(x):
    n = 50
    cos = 1
    for i in range(1, n+1):
        cos += (((-1)**i) * (x**(2*i))/fatorial(2*i))
    return cos

def tanx(x):
    return senx(x)/cosx(x)

def menu():
    print("Escolha uma operação")
    print("---Menu de Opções---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("6 - Seno")
    print("7 - Cosseno")
    print("8 - Tangente")
    print("9 - Exponencial (e^x) (unário)")
    print("10 - Logaritmo Neperiano (ln)")
    print("11 - Raiz Quadrada")
    print("12 - Fatorial")
    print("13 - Logaritmo Natural (base 10)")
    print("14 - Resetar Calculadora")
    print("15 - Sair")