#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import unicodedata

url = "https://elpais.com/economia/2020/11/25/actualidad/1606309651_814788.html" 
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

body_text = soup.find_all('p', 'Paragraph')
body_without_html_tags = re.sub('<.*?>', '', str(body_text))

document = open('file_to_scrap.txt', 'w')
document.write(str(body_without_html_tags))
document.close

document_text = open ('file_to_scrap.txt', 'r')
text_string = document_text.read().lower()
output = unicodedata.normalize('NFD', text_string).encode('ascii', 'ignore')
match_pattern = re.findall(r'[a-z]{1,30}', str(output))

class words_frequency():

    def __init__(self, archive):

        self.archive = archive

    def counter(self):

        frequency = {}
        
        for word in match_pattern:
            count = frequency.get(word,0)
            frequency[word] = count + 1

        frequency_list = sorted(frequency.keys())

        for words in frequency_list:
            print (words, frequency[words])

myCounter = words_frequency('file_to_scrap.txt')
myCounter.counter()