import os
import re
import sys
import time
import random

from terminal.terminal import Terminal

class Document():
    def __init__(self, f):
        """ Accept file or text and build textual representation """
        self.pages = []

        # If this is a file, load text
        if self._is_file(f):
            f = open(f, 'r').read()

        # Populate our one-to-many class relationship
        self.pages.extend([Page(p) for p in self._retrieve_pages(f)])

    def draw(self, delay=(1,5)):
        """ Dump document to stdout with random :delay: dumps
        in the range of delay=(min,max) """

        # TODO Check delay param is valid

        for page in self.pages:
            page.draw()

    def _retrieve_pages(self, text):
        """ Return indexed list of Page classes """

        term_height = Terminal().height - 10          # Gee, I wonder
        text_height = text.count('\n')                # Num lines
        pages_reqd  = -(-text_height // term_height)  # Ceiling

        # Clean text (rm runs of newlines)
        text  = re.sub(r"^\s*$", "", text)

        # Split text into chunks we can display at a time
        pages = re.findall(r".*\n"*term_height, text)

        return pages

    def _is_file(self, f):
        """ Determine whether str passed is a valid file path """
        return (f.count('\n') < 1 or os.path.isfile(f))

class Page():
    def __init__(self, s):
        self.lines = [Line(line + '\n') for line in s.split('\n')]

    def draw(self):
        """ Dump page to stdout """
        for line in self.lines:
            line.draw()

class Line():
    def __init__(self, s):
        """ Split line on words, count whitespace(s) as words, too """
        self.words = [Word(w) for w in re.findall("(\S+|\s)", s)]

    def draw(self):
        for word in self.words:
            word.draw()
            time.sleep(random.uniform(0, 0.3))


class Word():
    def __init__(self, s):
        self.chars = [Char(c) for c in s]

    def draw(self):
        for char in self.chars:
            char.draw()
            time.sleep(random.uniform(0, 0.01))

class Char():
    def __init__(self, c):
        self.text = c

    def draw(self):
        sys.stdout.write(self.text)
        sys.stdout.flush()

