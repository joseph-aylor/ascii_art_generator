import os

class AsciiImage:
    def __init__(self, characters):
        self.characters = characters

    def display(self, line_width=2):
        print(self.as_text(line_width))

    def as_text(self, line_width=1):
        text = ""
        # Too much nesting. Fix this.
        for row in self.characters:
            for value in row:
                text += AsciiImage._display_value(value, line_width)
            text += os.linesep
        return text

    def _display_value(value, line_width):
        text = ""
        for i in range(line_width):
            text += value
        return text
