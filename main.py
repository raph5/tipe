from renderer import render
from mathlib.autodiff import Var
from mathlib.vector import Vector
from imagelib import loadImage, saveImage
import sys


WIDTH = 100
HEIGHT = 100
VITESSE = 1 / WIDTH


def main() :
    sys.setrecursionlimit(WIDTH*HEIGHT*10)

    # createReference()

    referenceImage = loadImage("run0/reference.png")
    params = Vector([ Var(0), Var(0), Var(0) ])

    for i in range(10) :
        image = render(params, WIDTH, HEIGHT)
        saveImage(image, f"run0/render{i}.png", WIDTH, HEIGHT)
        loss = (referenceImage - image).norme()
        loss.retour()

        print("loss :", loss.valeur)
        print("gradient :", [ c.adjoint for c in params ])

        for p in params :
            p.valeur -= VITESSE * p.adjoint


def createReference() :
    params = Vector([ Var(1), Var(0.6), Var(0.4) ])
    image = render(params, WIDTH, HEIGHT)
    saveImage(image, "run0/reference.png", WIDTH, HEIGHT)


if __name__ == "__main__" :
    main()
