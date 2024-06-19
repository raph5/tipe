from __future__ import annotations
from mathlib.autodiff import Var
from mathlib.vector import Vector


class Matrix :
    def  __init__(self, coord: list[list[Var]]) :
        columns = len(coord[0])
        assert len(coord) > 0
        assert columns > 0
        for i in range(1, len(coord)) :
            assert len(coord[i]) == columns
        self.coord = coord

    def __getitem__(self, c: tuple[int, int]) :
        return self.coord[c[0]][c[1]]
    def __str__(self) :
        return str([ [ r.value for r in c ] for c in self.coord ])

    def __add__(self, b: Matrix|Var|int|float) -> Matrix :
        if isinstance(b, (int, float, Var)) :
            mat = []
            n = len(self.coord)
            m = len(self.coord[0])
            for i in range(n) :
                row = []
                for j in range(m) :
                    row.append(self[i, j] + b)
                mat.append(row)
            return Matrix(mat)
        mat = []
        n = len(self.coord)
        m = len(self.coord[0])
        assert n == len(b.coord)
        assert m == len(b.coord[0])
        for i in range(n) :
            row = []
            for j in range(m) :
                row.append(self[i, j] + b[i, j])
            mat.append(row)
        return Matrix(mat)

    def __sub__(self, b: Matrix|Var|int|float) -> Matrix :
        if isinstance(b, (int, float, Var)) :
            mat = []
            n = len(self.coord)
            m = len(self.coord[0])
            for i in range(n) :
                row = []
                for j in range(m) :
                    row.append(self[i, j] - b)
                mat.append(row)
            return Matrix(mat)
        mat = []
        n = len(self.coord)
        m = len(self.coord[0])
        assert n == len(b.coord)
        assert m == len(b.coord[0])
        for i in range(n) :
            row = []
            for j in range(m) :
                row.append(self[i, j] - b[i, j])
            mat.append(row)
        return Matrix(mat)

    def __mul__(self, b: Matrix|Var|int|float) -> Matrix :
        if isinstance(b, (int, float, Var)) :
            mat = []
            n = len(self.coord)
            m = len(self.coord[0])
            for i in range(n) :
                row = []
                for j in range(m) :
                    row.append(self[i, j] * b)
                mat.append(row)
            return Matrix(mat)
        mat = []
        l = len(b.coord[0])
        n = len(self.coord)
        m = len(self.coord[0])
        assert len(b.coord) == m
        for i in range(n) :
            row = []
            for j in range(l) :
                a = self[i, 0] * b[0, j]
                for k in range(1, m) :
                    a += self[i, k] * b[k, j]
                row.append(a)
            mat.append(row)
        return Matrix(mat)

    def __truediv__(self, b: Var|int|float) -> Matrix :
        mat = []
        n = len(self.coord)
        m = len(self.coord[0])
        for i in range(n) :
            row = []
            for j in range(m) :
                row.append(self[i, j] / b)
            mat.append(row)
        return Matrix(mat)

    def mulvec(self, b: Vector) -> Vector :
        vec = []
        n = len(self.coord)
        m = len(self.coord[0])
        assert len(b.coord) == m
        for i in range(n) :
            a = self[i, 0] * b[0]
            for j in range(m) :
                a = self[i, j] * b[j]
            vec.append(a)
        return Vector(vec)


def unit_matrix(size: int) -> Matrix :
    mat = []
    for i in range(size) :
        row = []
        for j in range(size) :
            row.append(Var(1) if i == j else Var(0))
        mat.append(row)
    return Matrix(mat)
