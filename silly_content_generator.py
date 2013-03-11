from lipsum import Generator, MarkupGenerator
import argparse
import os
import string


generator = Generator()
markup_gen = MarkupGenerator()
parser = argparse.ArgumentParser(description='Create some content.')
parser.add_argument("-i", "--index")  # Name of index file e.g. index.html


INDEX = 'index.html'
NUM = 5


def create_index(outfile):
    index = open(outfile, 'wb')
    index.write(markup_gen.generate_paragraphs_html_p(NUM))
    index.close()


def create_dirs(index):
    for directory in generator.generate_sentence().split(' '):
        # http://stackoverflow.com/questions/265960
        directory = directory.translate(
            string.maketrans("", ""), string.punctuation).lower()
        print "Created: %s" % directory
        try:
            os.mkdir(directory)
        except OSError:
            print "-> Directory '%s' already exists" % directory
        outfile = '%s/%s' % (directory, index)
        create_index(outfile)


def main():
    args = parser.parse_args()
    index = INDEX
    if args.index:
        index = args.index
    create_index(index)
    create_dirs(index)
