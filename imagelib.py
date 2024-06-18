from PIL import Image
from mathlib.vector import Vector
from mathlib.autodiff import Var


def save_image(image_vector: Vector, path: str, width: int, height: int) -> None :
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for x in range(width) :
        for y in range(height) :
            pixels[x, y] = (
                int(image_vector[3*width*y + x*3 + 0].value * 255),
                int(image_vector[3*width*y + x*3 + 1].value * 255),
                int(image_vector[3*width*y + x*3 + 2].value * 255)
            )
    image.save(path)
    print(f"image saved at {path}")


def load_image(image_path: str) -> Vector :
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()
    image_vector = []
    for y in range(height) :
        for x in range(width) :
            red, green, blue = pixels[x, y]
            image_vector += [ Var(red/255), Var(green/255), Var(blue/255) ]
    return Vector(image_vector)
