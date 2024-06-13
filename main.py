from renderer import render
from mathlib.autodiff import Var
from mathlib.vector import Vector
from imagelib import loadImage, saveImage
import sys


WIDTH = 100
HEIGHT = 100
VITESSE = 0.1 / WIDTH
INERTIE = 0.6


def main() :
    sys.setrecursionlimit(WIDTH*HEIGHT*10)

    # createReference()

    referenceImage = loadImage("run1/reference.png")
    params = Vector([ Var(0), Var(0), Var(0) ])
    delta_params = [0.0, 0.0, 0.0]

    for i in range(20) :
        image = render(params, WIDTH, HEIGHT)
        saveImage(image, f"run1/render{i}.png", WIDTH, HEIGHT)
        loss = (referenceImage - image).norme()
        loss.retour()

        print("loss :", loss.valeur)
        # print("gradient :", [ c.adjoint for c in params ])
        # print("delta :", delta_params)

        for i in range(len(params)) :
            delta_p = INERTIE * delta_params[i] + VITESSE * params[i].adjoint
            params[i].valeur -= delta_p
            delta_params[i] = delta_p


def createReference() :
    params = Vector([ Var(1), Var(0.6), Var(0.4) ])
    image = render(params, WIDTH, HEIGHT)
    saveImage(image, "run1/reference.png", WIDTH, HEIGHT)


if __name__ == "__main__" :
    main()
