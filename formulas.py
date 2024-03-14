#Aqui ficarão como as séries utilizadas para o calculo de cada função
#Fonte: https://en.wikipedia.org/wiki/Taylor_series
#Fonte: https://en.wikipedia.org/wiki/Leibniz_formula_for_π

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

#e^x sendo x um número real calculado pela soma da série 1 + x + x^2/2! + x^3/3! + x^4/4! + ... + x^n/n!
def exponcialx(x):
    n = 50
    e = 1
    for i in range(1, n+1):
        e += (x**i)/fatorial(i)
    return e

#ln(x) esta quebrado
# (?) Considerar numeros negativos??? (A série seria diferente)  -1 < x < 1
#ln(x) sendo x um número real calculado pela soma da série x - x^2/2 + x^3/3 - x^4/4 + ... + (-1)^(n-1) * x^n/n
#def ln(x):
#    n = 100
#    ln = 0
#    for i in range(1, n+1):
#        ln += (((-1)**(i+1)) * (x**i)/i)
#    return ln

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