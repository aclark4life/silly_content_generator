
import os
import string
from lipsum import Generator

lipsum = Generator()

def create_dirs():
    for dir in lipsum.generate_sentence().split(' '):
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        dir = dir.translate(string.maketrans("",""), string.punctuation).lower()
        print dir
        try:
            os.mkdir(dir)
        except OSError:
            print "dir '%s' already exists" % dir

def main():
    create_dirs()
