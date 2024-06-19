from renderer import render
from mathlib.autodiff import Var
from mathlib.vector import Vector
from imagelib import load_image, save_image
import sys


WIDTH = 50
HEIGHT = 50
VITESSE = 0.08 / WIDTH
INERTIE = 0.6


def main() :
    sys.setrecursionlimit(WIDTH*HEIGHT*100)

    create_reference()

    reference_image = load_image("run3/reference.png")
    params = Vector([
        Var(1), Var(0.6), Var(0.4),  # default color
        Var(0.2), Var(0.6), Var(1),  # cube color
        Var(0.87), Var(0), Var(-0.5),  # light source

        Var(0.03),  Var(0.19),  Var(0.84), Var(1),  # face 1
        Var(0.71),  Var(-0.36),  Var(0.35), Var(1),
        Var(-0.71),  Var(-0.30),  Var(0.40), Var(1),
        Var(-0.04),  Var(-0.86),  Var(-0.10), Var(1),

        Var(0.04),  Var(0.86),  Var(0.10), Var(1),  # face 2
        Var(0.71),  Var(0.30),  Var(-0.40), Var(1),
        Var(-0.71),  Var(0.36),  Var(-0.35), Var(1),
        Var(-0.04),  Var(-0.19),  Var(-0.84), Var(1),

        Var(0.04),  Var(0.19),  Var(0.84), Var(1),  #  face 3
        Var(0.04),  Var(0.86),  Var(0.10), Var(1),
        Var(-0.71),  Var(-0.30),  Var(0.40), Var(1),
        Var(-0.71),  Var(0.36),  Var(-0.35), Var(1),

        Var(0.71),  Var(-0.36),  Var(0.35), Var(1),  # face 4
        Var(0.71),  Var(0.30),  Var(-0.40), Var(1),
        Var(-0.04),  Var(-0.86),  Var(-0.10), Var(1),
        Var(-0.04),  Var(-0.19),  Var(-0.84), Var(1),

        Var(0.04),  Var(0.19),  Var(0.84), Var(1),  # face 5
        Var(0.04),  Var(0.86),  Var(0.10), Var(1),
        Var(0.71),  Var(-0.36),  Var(0.35), Var(1),
        Var(0.71),  Var(0.30),  Var(-0.40), Var(1),

        Var(-0.71),  Var(-0.30),  Var(0.40), Var(1),  # face 6
        Var(-0.71),  Var(0.36),  Var(-0.35), Var(1),
        Var(-0.04),  Var(-0.86),  Var(-0.10), Var(1),
        Var(-0.04),  Var(-0.19),  Var(-0.84), Var(1),
    ])
    delta_params = [0.0] * len(params)

    for i in range(20) :
        image = render(params, WIDTH, HEIGHT)
        save_image(image, f"run3/render{i}.png", WIDTH, HEIGHT)
        loss = (reference_image - image).norm()
        loss.reverse_path()

        print("loss :", loss.value)
        # print("gradient :", [ c.adjoint for c in params ])
        # print("delta :", delta_params)

        for i in range(9) :
            delta_p = INERTIE * delta_params[i] + VITESSE * params[i].adjoint
            params[i].value -= delta_p
            delta_params[i] = delta_p


def create_reference() :
    params = Vector([
        Var(1), Var(0.6), Var(0.4),  # default color
        Var(0.2), Var(0.6), Var(1),  # cube color
        Var(0.58), Var(0.58), Var(-0.58),  # light source

        Var(0.03),  Var(0.19),  Var(0.84), Var(1),  # face 1
        Var(0.71),  Var(-0.36),  Var(0.35), Var(1),
        Var(-0.71),  Var(-0.30),  Var(0.40), Var(1),
        Var(-0.04),  Var(-0.86),  Var(-0.10), Var(1),

        Var(0.04),  Var(0.86),  Var(0.10), Var(1),  # face 2
        Var(0.71),  Var(0.30),  Var(-0.40), Var(1),
        Var(-0.71),  Var(0.36),  Var(-0.35), Var(1),
        Var(-0.04),  Var(-0.19),  Var(-0.84), Var(1),

        Var(0.04),  Var(0.19),  Var(0.84), Var(1),  #  face 3
        Var(0.04),  Var(0.86),  Var(0.10), Var(1),
        Var(-0.71),  Var(-0.30),  Var(0.40), Var(1),
        Var(-0.71),  Var(0.36),  Var(-0.35), Var(1),

        Var(0.71),  Var(-0.36),  Var(0.35), Var(1),  # face 4
        Var(0.71),  Var(0.30),  Var(-0.40), Var(1),
        Var(-0.04),  Var(-0.86),  Var(-0.10), Var(1),
        Var(-0.04),  Var(-0.19),  Var(-0.84), Var(1),

        Var(0.04),  Var(0.19),  Var(0.84), Var(1),  # face 5
        Var(0.04),  Var(0.86),  Var(0.10), Var(1),
        Var(0.71),  Var(-0.36),  Var(0.35), Var(1),
        Var(0.71),  Var(0.30),  Var(-0.40), Var(1),

        Var(-0.71),  Var(-0.30),  Var(0.40), Var(1),  # face 6
        Var(-0.71),  Var(0.36),  Var(-0.35), Var(1),
        Var(-0.04),  Var(-0.86),  Var(-0.10), Var(1),
        Var(-0.04),  Var(-0.19),  Var(-0.84), Var(1),
    ])
    image = render(params, WIDTH, HEIGHT)
    save_image(image, "run3/reference.png", WIDTH, HEIGHT)


if __name__ == "__main__" :
    main()
