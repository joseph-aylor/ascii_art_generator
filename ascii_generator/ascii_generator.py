from PIL import Image
from ascii_generator.ascii_image import AsciiImage


class AsciiGenerator:
    def __init__(self, translation_chars=" .:-=+*#%@"):
        self.translation_chars = translation_chars

    def pallette_display(self):
        for color in range(256):
            display = self._pallette_value(color)
            print(f"{color} => {display}")

    def generate(self, image, max_dimension=100):
        gray_image = image.convert('L')
        gray_image = AsciiGenerator._scale_image(gray_image, max_dimension)

        ascii_image = []
        for y in range(gray_image.height):
            ascii_image.append([])
            for x in range(gray_image.width):
                color = gray_image.getpixel((x, y))
                ascii_image[-1].append(self._pallette_value(color))
        return AsciiImage(ascii_image)

    def _pallette_value(self, color):
        translation_factor = 256/len(self.translation_chars)
        return self.translation_chars[int(color / translation_factor)]

    def _scale_image(image, max_dimension):
        image_dimension = 0
        if image.height > image.width:
            image_dimension = image.height
        else:
            image_dimension = image.width

        new_height = int((image.height / image_dimension) * max_dimension)
        new_width = int((image.width / image_dimension) * max_dimension)

        return image.resize((new_width, new_height), Image.ANTIALIAS)
