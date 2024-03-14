#Aqui ficarão como as séries utilizadas para o calculo de cada função
#Fonte: https://en.wikipedia.org/wiki/Taylor_series

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

# (?) Considerar numeros negativos??? (A série seria diferente)
#ln(x) sendo x um número real calculado pela soma da série x - x^2/2 + x^3/3 - x^4/4 + ... + (-1)^(n-1) * x^n/n
def ln(x):
    n = 50
    ln = 0
    for i in range(1, n+1):
        ln += ((-1)**(i-1) * (x**i))/i
    return ln

print