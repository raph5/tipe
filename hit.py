from mathlib.autodiff import Var
from mathlib.vector import Vector
from object3d import Object3d


class Hit :
    def __init__(self, object3d: Object3d, v1: Vector, v2: Vector, v3: Vector, lambda1: Var, lambda2: Var, lambda3: Var) :
        self.object3d = object3d
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.lambda3 = lambda3

    def getZ(self) -> Var :
        return self.v1[2]*self.lambda1 + self.v2[2]*self.lambda2 + self.v3[2]*self.lambda3

    def getNormal(self) -> Vector :
        return (self.v1 - self.v2).cross(self.v1 - self.v3).normalize()

    def getObjectColor(self) -> Vector :
        return self.object3d.color
