import requests
import argparse
import os

api_key = os.getenv('WORDS_API_KEY')

parser = argparse.ArgumentParser()

parser.add_argument("word", help="word to search for synonyms")

args = parser.parse_args()

word = args.word
print (word)

r = requests.get('http://words.bighugelabs.com/api/2/%s/%s/json' %(api_key, word))
content = r.text
print (content)
