from lipsum import Generator, MarkupGenerator
import os
import string


generator = Generator()
markup_gen = MarkupGenerator()


NUM = 5


def create_index(outfile):
    index = open(outfile, 'wb')
    index.write(markup_gen.generate_paragraphs_html_p(NUM))
    index.close()


def create_dirs():
    for dir in generator.generate_sentence().split(' '):
        # http://stackoverflow.com/questions/265960
        dir = dir.translate(
            string.maketrans("", ""), string.punctuation).lower()
        print dir
        try:
            os.mkdir(dir)
        except OSError:
            print "dir '%s' already exists" % dir
        outfile = '%s/index.html' % dir
        create_index(outfile)


def main():
    create_index('index.html')
    create_dirs()
