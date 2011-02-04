
import os
import string
from lipsum import Generator, MarkupGenerator

generator = Generator()
markup_gen = MarkupGenerator()

_MAGIC_NUMBER = 5

def create_dirs():
    for dir in generator.generate_sentence().split(' '):
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        dir = dir.translate(string.maketrans("",""), string.punctuation).lower()
        print dir
        try:
            os.mkdir(dir)
        except OSError:
            print "dir '%s' already exists" % dir
        index = open('%s/index.html' % dir, 'wb')
        index.write(markup_gen.generate_paragraphs_html_p(_MAGIC_NUMBER))
        index.close()

def main():
    create_dirs()
