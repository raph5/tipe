from mathlib.vector import Vector


class IsometricCamera :
    def project(self, vector: Vector) -> Vector :
        return vector

# Pour rajouter une caméra en persepective linéaire il ne faut pas oublier de
# refaire l'interrpolation de la coordonée z au moment du path tracing
# voire : https://www.scratchapixel.com/lessons/3d-basic-rendering/rasterization-practical-implementation/visibility-problem-depth-buffer-depth-interpolation.html
