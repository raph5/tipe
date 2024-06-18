from __future__ import annotations
import math


# [ (adjoint, derivee_locale), (...), ... ]
type DeriveeLocale = list[tuple[Var, float]]


class Var :
    def __init__(self, value: float, local_derivatives: DeriveeLocale = []) -> None :
        # la valeur de la variable
        self.value = value
        # l'adjoint de la variable
        self.adjoint = 0
        # dérivée de la variable par rapport à ses parents
        # une variable parent est une variable qui intervient dans le calcul de
        # cette variable
        # par exemple a est un parent de a+b
        self.__local_derivatives = local_derivatives

    # attention à ne pas appeler cette méthod plus d'une fois
    def reverse_path(self, child_adjoint: float = 1) -> None :
        self.__reset_adjoints()
        self.__reverse_path(child_adjoint)
    def __reverse_path(self, child_adjoint: float) -> None :
        for parent_var, derivee_locale in self.__local_derivatives :
            parent_var.adjoint += child_adjoint * derivee_locale
            parent_var.__reverse_path(child_adjoint * derivee_locale)
    def __reset_adjoints(self) :
        self.adjoint = 0
        for parent_var, _ in self.__local_derivatives :
            parent_var.__reset_adjoints()


    def __str__(self) :
        return str(self.value)

    def __neg__(self) -> Var :
        return Var(-self.value, [(self, -1)])

    def __add__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.value + b, [(self, 1)])
        return Var(self.value + b.value, [(self, 1), (b, 1)])

    def __sub__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.value - b, [(self, 1)])
        return Var(self.value - b.value, [(self, 1), (b, -1)])

    def __mul__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.value * b, [(self, b)])
        return Var(self.value * b.value, [(self, b.value), (b, self.value)])

    def __truediv__(self, b: Var|int|float) -> Var :
        if isinstance(b, (int, float)) :
            return Var(self.value / b, [(self, 1/b)])
        return Var(
            self.value / b.value,
            [(self, 1 / b.value), (b, -self.value / b.value**2)]
        )

    def __pow__(self, k: int|float|Var) -> Var :
        if isinstance(k, (int, float)) :
            return Var(self.value ** k, [(self, k * self.value ** (k-1))])
        return Var(
            self.value ** k.value,
            [(self, k.value * self.value ** (k.value - 1)), (k, (self.value ** k.value) * math.log(self.value))]
        )


def exp(a: Var) -> Var :
    return Var(math.exp(a.value), [(a, math.exp(a.value))])

def log(a: Var) -> Var :
    return Var(math.log(a.value), [(a, 1/ a.value)])

def sin(a: Var) -> Var :
    return Var(math.sin(a.value), [(a, math.cos(a.value))])

def cos(a: Var) -> Var :
    return Var(math.cos(a.value), [(a, -math.sin(a.value))])

def abs(a: Var) -> Var :
    return a if a.value >= 0 else -a
