
from lipsum import Generator

lipsum = Generator()

def create_dirs():
    for dir in lipsum.generate_sentence().split(' '):
        print dir

def main():
    create_dirs()
