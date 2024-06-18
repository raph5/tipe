from __future__ import annotations
from mathlib.autodiff import Var


class Vector :
    def __init__(self, coordinates: list[Var]) -> None:
        self.coord = coordinates

    def sub_vecotr(self, start: int, end: int) -> Vector :
        return Vector(self.coord[start:end])

    def __getitem__(self, key: int) :
        return self.coord[key]
    def __len__(self) :
        return len(self.coord)
    def __iter__(self) :
        return self.coord.__iter__()
    def __str__(self) :
        return str([ c.value for c in self.coord ])

    def __add__(self, b: Vector|Var|int|float) -> Vector :
        if isinstance(b, (int, float, Var)) :
            return Vector([ self[i] + b for i in range(len(self)) ])
        assert len(self) == len(b)
        return Vector([ self[i] + b[i] for i in range(len(self)) ])

    def __sub__(self, b: Vector|Var|int|float) -> Vector :
        if isinstance(b, (int, float, Var)) :
            return Vector([ self[i] - b for i in range(len(self)) ])
        assert len(self) == len(b)
        return Vector([ self[i] - b[i] for i in range(len(self)) ])

    def __mul__(self, b: Var|int|float) -> Vector :
        return Vector([ self[i] * b for i in range(len(self)) ])

    def __truediv__(self, b: Var|int|float) -> Vector :
        return Vector([ self[i] / b for i in range(len(self)) ])

    def dot(self, b: Vector) -> Var :
        assert len(self) == len(b)
        c = self[0] * b[0]
        for i in range(1, len(self)) :
            c += self[i] * b[i]
        return c

    def cross(self, b: Vector) -> Vector :
        assert len(self) >= 3 and len(b) >= 3
        return Vector([
            self[1]*b[2] - self[2]*b[1],
            self[2]*b[0] - self[0]*b[2],
            self[0]*b[1] - self[1]*b[0]
        ])

    def norm(self) -> Var :
        m = self[0] ** 2
        for i in range(1, len(self)) :
            m += self[i] ** 2
        return m ** 0.5

    def normalize(self) -> Vector :
        return self / self.norm()
