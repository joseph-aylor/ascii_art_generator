#!/usr/bin/env python3
import ascii_generator
import sys

from PIL import Image
from os import get_terminal_size

import argparse

if __name__ == '__main__':
    # Full ascii pallet is below, but it doesn't look great
    # chars = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

    parser = argparse.ArgumentParser(
        prog = "Ascii Art Generator",
        description = "Converts images to strings",
        epilog = "End of help"
    )

    parser.add_argument('image_file')
    parser.add_argument('-p', '--pallet', default=' .\'`^",:;~+-?|*#&%@$')
    parser.add_argument('-d', '--maxdimension', default=get_terminal_size().columns - 100, type=int)

    args = parser.parse_args()

    generator = ascii_generator.AsciiGenerator(args.pallet)
    ascii_image = generator.generate(Image.open(args.image_file), args.maxdimension)
    ascii_image.display()
