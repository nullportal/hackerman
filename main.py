import os
import sys
import time
import random
import requests
import subprocess

""" Print cool hacker-looking stuff to terminal """

def main(args):
    t = Terminal()

    print(f"term area:          {t.area}")
    print(f"term dimensions:    {t.dimensions}")
    print(f"term width:         {t.width}")
    print(f"term height:        {t.height}")
    print(f"term centre:        {t.centre}")

    pos      = 0,0

    i    = 1
    while True:

        for j in range(t.width):
            time.sleep(0.01)

            x,y = 0, i
            x  += j

            t.draw_char(ch=str(i), pos=(x,y))

        i += 1

        for k in range(t.width):
            time.sleep(0.01)

            x,y = t.width, i
            x  -= k

            t.draw_char(ch=str(i), pos=(x,y))

        i += 1

        # Start over
        if i == t.height:
            i = 1


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


if __name__ == "__main__": main(sys.argv)
