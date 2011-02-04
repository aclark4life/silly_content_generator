
import string
from lipsum import Generator

lipsum = Generator()

def create_dirs():
    for dir in lipsum.generate_sentence().split(' '):
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        print dir.translate(string.maketrans("",""), string.punctuation).lower()


def main():
    create_dirs()
