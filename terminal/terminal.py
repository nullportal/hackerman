import sys
import subprocess

class Terminal():
    def __init__(self):
        self.__height, self.__width = [int(n) for n in subprocess.check_output(["stty", "size"]).split()]

    def draw_char(self, ch='x', pos=(-1,-1)):
        """ TODO Draw a character at a specific position - refresh screen """
        out_str = ''
        for col in range(self.height):
            for row in range(self.width):

                if (row, col) == pos:
                    out_str += ch
                else:
                    out_str += ' '

            out_str += '\n'

        sys.stdout.write(out_str)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def area(self):
        return self.__width * self.height

    @property
    def dimensions(self):
        return self.__width, self.height

    @property
    def centre(self):
        return int(self.width  / 2), int(self.height / 2)

