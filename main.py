import ascii_generator

from PIL import Image

generator = ascii_generator.AsciiGenerator()
ascii_image = generator.generate(Image.open('tests/fixtures/test.png'), 10)
ascii_image.display()
print('done')
