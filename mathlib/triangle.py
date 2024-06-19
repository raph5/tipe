from mathlib.vector import Vector
from mathlib.autodiff import Var


# https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Vertex_approach
def barycentric_coordinates(pt: Vector, v1: Vector, v2: Vector, v3: Vector) -> tuple[bool, Var, Var, Var] :
    v1y_minus_v2y = v1[1] - v2[1]
    v2y_minus_v3y = v2[1] - v3[1]
    v3y_minus_v1y = v3[1] - v1[1]

    # deux fois l'aire signé du triangle
    area = v1[0]*v2y_minus_v3y + v2[0]*v3y_minus_v1y + v3[0]*v1y_minus_v2y
    if area.value == 0 :
        return False, Var(0), Var(0), Var(0)

    lambda1 = (v2[0]*v3[1] - v3[0]*v2[1] + pt[0]*v2y_minus_v3y + pt[1]*(v3[0] - v2[0])) / area
    lambda2 = (v3[0]*v1[1] - v1[0]*v3[1] + pt[0]*v3y_minus_v1y + pt[1]*(v1[0] - v3[0])) / area
    lambda3 = (v1[0]*v2[1] - v2[0]*v1[1] + pt[0]*v1y_minus_v2y + pt[1]*(v2[0] - v1[0])) / area

    return True, lambda1, lambda2, lambda3
