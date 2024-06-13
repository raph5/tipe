from mathlib.vector import Vector


class Object3d :
    def __init__(self, indexBuffer: list[int], vertexBuffer: Vector) :
        self.indexBuffer = indexBuffer
        self.vertexBuffer = vertexBuffer

    # def rayColor(x: float, y: float) -> (Var, Var, Var) :
    #     return (Var(0), Var(0), Var(0))
