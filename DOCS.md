
# Différenciation automatique

Exemple :
```py
def f(a, b) :
    c = a / b
    d = exp(b)
    e = sin(c)
    f = c - d
    g = e + f
    return h = f * g

def main() :
    a = Var(1.5)
    b = Var(0.5)
    c = f(a, b)
    c.retour()
    print("valeur de f(a, b) :", h.valeur)
    print("dérivée de f(a, b) par rapport à a :", a.adjoint)
    print("dérivée de f(a, b) par rapport à b :", b.adjoint)
