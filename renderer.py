import random
from math import inf
from camera import IsometricCamera
from mathlib.autodiff import Var, abs
from mathlib.triangle import barycentric_coordinates
from mathlib.vector import Vector
from object3d import Object3d, create_cube, create_triangle
from hit import Hit


LIGHT_SOURCE = Vector([ Var(1), Var(-1), Var(1) ]).normalize()
SAMPLE_SIZE = 2


def render(params: Vector, width: int, height: int) -> Vector :
    random.seed(0)

    # initialisation de la scène
    camera = IsometricCamera()
    default_color = params.sub_vecotr(0, 3)
    triangle_color = params.sub_vecotr(3, 6)
    scene = [
        create_triangle(params, 6, triangle_color)
        # create_cube(params, 6, cube_color)
    ]

    # projette les vertex de chaque objects dans l'espace caméra
    for o in scene :
        o.project_geometry(camera)

    # calcul les pixel values
    pixel_values = []
    pixel_width = 2/width
    pixel_height = 2/height
    for y in range(height) :
        for x in range(width) :
            color = Vector([ Var(0), Var(0), Var(0) ])
            for i in range(SAMPLE_SIZE) :
                ray_x = -1 + pixel_width*x + pixel_width*random.random()
                ray_y = -1 + pixel_height*y + pixel_height*random.random()
                color += trace_path(Var(ray_x), Var(ray_y), scene, default_color)
            color /= SAMPLE_SIZE
            pixel_values.extend(color.coord)

    return Vector(pixel_values)


def trace_path(x: Var, y: Var, scene: list[Object3d], default_color: Vector) -> Vector :
    hit: Hit|None = None

    for o in scene :
        maxZ = -inf
        for i in range(0, len(o.index_buffer), 3) :
            v1 = o.projection_buffer[o.index_buffer[i+0]]
            v2 = o.projection_buffer[o.index_buffer[i+1]]
            v3 = o.projection_buffer[o.index_buffer[i+2]]
            lambda1, lambda2, lambda3 = barycentric_coordinates(Vector([x, y]), v1, v2, v3)
            if lambda1.value>0 and lambda2.value>0 and lambda3.value>0 :
                h = Hit(o, v1, v2, v3, lambda1, lambda2, lambda3)
                z = h.getZ()
                if z.value > maxZ :
                    maxZ = z.value
                    hit = h

    if hit == None :
        return default_color

    normal = hit.getNormal()
    color = hit.getObjectColor()
    return color * abs(normal.dot(LIGHT_SOURCE))
