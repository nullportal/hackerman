import sys
import time

from terminal.terminal import Terminal

def main(args):
    """ Print cool hacker-looking stuff to terminal """

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

if __name__ == "__main__": main(sys.argv)
