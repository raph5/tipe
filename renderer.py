from mathlib.autodiff import Var
from mathlib.vector import Vector


type Params = Vector


def render(params: Params, width: int, height: int) -> Vector :
    coords = []
    for i in range(width*height) :
        coords += params.coord
    return Vector(coords)
