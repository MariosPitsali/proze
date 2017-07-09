from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("word", help="Word to find syllables")

args = parser.parse_args()

#parsing word from terminal
word_input = args.word

#getting html code from dictionary.com
word = requests.get("http://www.dictionary.com/browse/%s" %(word_input))
html_doc = BeautifulSoup(word.content, "html.parser")

#fidning html tags to get syllables
syl = html_doc.find_all("span", class_="me")[0].attrs['data-syllable'].split('·')

#printing each syllable and syllable count
print(len(syl), "syllables in word",  word_input)
for syllable in syl:
  print ("Syllable:", syllable, "\n")
