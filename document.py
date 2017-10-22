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
            time.sleep(random.randint(delay[0], delay[1]))

    def _retrieve_pages(self, text):
        """ Return indexed list of Page classes """

        term_height = Terminal().height - 10          # Gee, I wonder
        text_height = text.count('\n')                # Num lines
        pages_reqd  = -(-text_height // term_height)  # Ceiling

        #print(f"term_height: {term_height}, text_height: {text_height}, pages: {pages_reqd}")

        # Clean text (rm runs of newlines)
        text  = re.sub(r"^\s*$", "", text)

        # Split text into chunks we can display at a time
        pages = re.findall(r".*\n"*term_height, text)

        return pages

    def _is_file(self, f):
        """ Determine whether str passed is a valid file path """
        return (f.count('\n') < 1 or os.path.isfile(f))

class Page():
    def __init__(self, document):
        #print(f"Page::__init__({self}, {len(document)})")
        self.doc = document

    def draw(self):
        """ Dump page to stdout """
        sys.stdout.write(self.doc)

class Line():
    """ TODO """
    pass
class Word():
    """ TODO """
    pass
class Char():
    """ TODO """
    pass

