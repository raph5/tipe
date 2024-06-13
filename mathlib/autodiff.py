from __future__ import annotations
import math


# [ (adjoint, derivee_locale), (...), ... ]
type DeriveeLocale = list[tuple[Var, float]]


class Var :
    def __init__(self, valeur: float, derivees_locales: DeriveeLocale = []) -> None :
        # la valeur de la variable
        self.valeur = valeur
        # l'adjoint de la variable
        self.adjoint = 0
        # dérivée de la variable par rapport à ses parents
        # une variable parent est une variable qui intervient dans le calcul de
        # cette variable
        # par exemple a est un parent de a+b
        self.__derivees_locales = derivees_locales

    # attention à ne pas appeler cette méthod plus d'une fois
    def retour(self, child_adjoint: float = 1) -> None :
        self.__reset_adjoints()
        self.__retour(child_adjoint)
    def __retour(self, child_adjoint: float) -> None :
        for parent_var, derivee_locale in self.__derivees_locales :
            parent_var.adjoint += child_adjoint * derivee_locale
            parent_var.__retour(child_adjoint * derivee_locale)
    def __reset_adjoints(self) :
        self.adjoint = 0
        for parent_var, _ in self.__derivees_locales :
            parent_var.__reset_adjoints()


    def copy(self) -> Var :
        return Var(self.valeur, [(self, 1)])

    def __neg__(self) -> Var :
        return Var(-self.valeur, [(self, -1)])

    def __add__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.valeur + b, [(self, 1)])
        return Var(self.valeur + b.valeur, [(self, 1), (b, 1)])

    def __sub__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.valeur - b, [(self, 1)])
        return Var(self.valeur - b.valeur, [(self, 1), (b, -1)])

    def __mul__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.valeur * b, [(self, b)])
        return Var(self.valeur * b.valeur, [(self, b.valeur), (b, self.valeur)])

    def __truediv__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.valeur / b, [(self, 1/b)])
        return Var(
            self.valeur / b.valeur,
            [(self, 1 / b.valeur), (b, -self.valeur / b.valeur**2)]
        )

    def __pow__(self, k: int|float|Var) -> Var :
        if isinstance(k, (int, float)) :
            return Var(self.valeur ** k, [(self, k * self.valeur ** (k-1))])
        return Var(
            self.valeur ** k.valeur,
            [(self, k.valeur * self.valeur ** (k.valeur - 1)), (k, (self.valeur ** k.valeur) * math.log(self.valeur))]
        )


def exp(a: Var) -> Var :
    return Var(math.exp(a.valeur), [(a, math.exp(a.valeur))])

def log(a: Var) -> Var :
    return Var(math.log(a.valeur), [(a, 1/ a.valeur)])

def sin(a: Var) -> Var :
    return Var(math.sin(a.valeur), [(a, math.cos(a.valeur))])

def cos(a: Var) -> Var :
    return Var(math.cos(a.valeur), [(a, -math.sin(a.valeur))])
