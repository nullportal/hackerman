import os
import re
import sys
import time
import random

from terminal.terminal import Terminal

class Document():
    def __init__(self, f):
        """ Take :f: (file or text) and build textual representation """
        self.pages = []

        # If this is a file, load text
        if self._is_file(f):
            f = open(f, 'r').read()

        # Assign here to allow quick dump,
        # if so desired
        self.text = f

        # Populate our one-to-many class relationship
        self.pages.extend([Page(p) for p in self._retrieve_pages(f)])

    def type(self, speed=1):
        """ Type document to stdout at specified :speed: """

        # For our messy circular dependency
        for page in self.pages:
            page.type(speed)

    def draw(self):
        """ Dump document to stdout """
        print(self.text)

    def _retrieve_pages(self, text):
        """ Return indexed list of Page classes """

        term_height = Terminal().height - 10          # Gee, I wonder
        text_height = text.count('\n')                # Num lines
        pages_reqd  = -(-text_height // term_height)  # Ceiling

        # Clean text (rm runs of newlines)
        text  = re.sub(r"^\s*$", "", text)

        # Split text into chunks we can display at a time
        pages = re.findall(".*\n"*text_height, text)

        return pages

    def _is_file(self, f):
        """ Determine whether str passed is a valid file path """
        return (f.count('\n') < 1 or os.path.isfile(f))

class Page():
    def __init__(self, s):
        # Grab each line on newline (but add newline char back in)
        self.lines = [Line(line + '\n') for line in s.split('\n')]

    def type(self, speed):
        """ Type page to stdout """
        for line in self.lines:
            line.type(speed)

class Line():
    def __init__(self, s):
        """ Split line on words, count whitespace(s) as words, too """
        self.words = [Word(w) for w in re.findall("(\S+|\s+)", s)]

    def type(self, speed):
        """ Type line to stdout """
        for word in self.words:
            word.type(speed)
            time.sleep(random.uniform(0, 2/speed))


class Word():
    def __init__(self, s):
        """ Break up word into single chars """
        self.chars = [Char(c) for c in s]

    def type(self, speed):
        """ Type word to stdout """
        for char in self.chars:
            char.type()
            time.sleep(random.uniform(0, 1/speed))

class Char():
    def __init__(self, c):
        self.text = c

    def type(self):
        """ Just dump char to stdout """
        sys.stdout.write(self.text)
        sys.stdout.flush()  # Ensure we write before newline

