from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("word", help="Word to find syllables")

args = parser.parse_args()


word = args.word
wordz = requests.get("http://www.dictionary.com/browse/%s" %(word))
leword = BeautifulSoup(wordz.content, "html.parser")
syl = leword.find_all("span", class_="me")[0].attrs['data-syllable'].split('·')

print(len(syl), "syllables in word",  word)
for syllable in syl:
  print ("Syllable:", syllable, "\n")
