from mathlib.vector import Vector
from camera import IsometricCamera


class Object3d :
    def __init__(self, index_buffer: list[int], vertex_buffer: list[Vector], color: Vector) :
        self.index_buffer = index_buffer
        self.vertex_buffer = vertex_buffer
        self.projection_buffer = [ Vector([]) ] * len(vertex_buffer)
        self.color = color

    def project_geometry(self, camera: IsometricCamera) :
        for i in range(len(self.vertex_buffer)) :
            self.projection_buffer[i] = camera.project(self.vertex_buffer[i])


def create_cube(params: Vector, index: int, color: Vector) -> Object3d :
    vertex_buffer = []
    for i in range(0, 96, 4) :
        vertex_buffer.append(params.sub_vecotr(index+i, index+i+4))
    index_buffer = []
    for i in range(0, 24, 4) :
        index_buffer.extend((i, i+1, i+2))
        index_buffer.extend((i+1, i+2, i+3))
    return Object3d(index_buffer, vertex_buffer, color)

def create_triangle(params: Vector, index: int, color: Vector) -> Object3d :
    vertex_buffer = [
        params.sub_vecotr(index+0, index+4),
        params.sub_vecotr(index+4, index+8),
        params.sub_vecotr(index+8, index+12)
    ]
    indexBuffer = [0, 1, 2]
    return Object3d(indexBuffer, vertex_buffer, color)
