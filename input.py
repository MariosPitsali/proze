import argparse

parser = argparse.ArgumentParser()
parser.add_argument("word", help="word to find rhymes with")

args = parser.parse_args()
print (args.word)