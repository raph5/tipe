from PIL import Image
from mathlib.vector import Vector
from mathlib.autodiff import Var


def saveImage(imageVector: Vector, path: str, width: int, height: int) -> None :
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for x in range(width) :
        for y in range(height) :
            pixels[x, y] = (
                int(imageVector[3*width*y + x*3 + 0].valeur * 255),
                int(imageVector[3*width*y + x*3 + 1].valeur * 255),
                int(imageVector[3*width*y + x*3 + 2].valeur * 255)
            )
    image.save(path)
    print(f"image saved at {path}")


def loadImage(imagePath: str) -> Vector :
    image = Image.open(imagePath)
    width, height = image.size
    pixels = image.load()
    imageVector = []
    for x in range(width) :
        for y in range(height) :
            red, green, blue = pixels[x, y]
            imageVector += [ Var(red/255), Var(green/255), Var(blue/255) ]
    return Vector(imageVector)
