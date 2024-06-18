from renderer import render
from mathlib.autodiff import Var
from mathlib.vector import Vector
from imagelib import load_image, save_image
import sys


WIDTH = 50
HEIGHT = 50
VITESSE = 0.2 / WIDTH
INERTIE = 0.6


def main() :
    sys.setrecursionlimit(WIDTH*HEIGHT*100)

    # create_reference()

    reference_image = load_image("run2/reference.png")
    params = Vector([
        Var(0), Var(0), Var(0),  # default color
        Var(0), Var(0), Var(0),  # triangle color
        Var(0.5), Var(0), Var(0), Var(1),  # vertex 1
        Var(-0.5), Var(0.5), Var(0), Var(1),  # vertex 2
        Var(-0.5), Var(-0.5), Var(0), Var(1),  # vertex 3
    ])
    delta_params = [0.0] * len(params)

    for i in range(20) :
        image = render(params, WIDTH, HEIGHT)
        save_image(image, f"run2/render{i}.png", WIDTH, HEIGHT)
        loss = (reference_image - image).norm()
        loss.reverse_path()

        print("loss :", loss.value)
        # print("gradient :", [ c.adjoint for c in params ])
        # print("delta :", delta_params)

        for i in range(len(params)) :
            delta_p = INERTIE * delta_params[i] + VITESSE * params[i].adjoint
            params[i].value -= delta_p
            delta_params[i] = delta_p


def create_reference() :
    params = Vector([
        Var(1), Var(0.6), Var(0.4),  # default color
        Var(0.2), Var(0.6), Var(1),  # triangle color
        Var(0.5), Var(0), Var(0), Var(1),  # vertex 1
        Var(-0.5), Var(0.5), Var(0), Var(1),  # vertex 2
        Var(-0.5), Var(-0.5), Var(0), Var(1),  # vertex 3
    ])
    image = render(params, WIDTH, HEIGHT)
    save_image(image, "run2/reference.png", WIDTH, HEIGHT)


if __name__ == "__main__" :
    main()
