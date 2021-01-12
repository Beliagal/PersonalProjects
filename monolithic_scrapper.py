#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import unicodedata
import collections
import os
import errno
from pathlib import Path

def create_directory ():
    try:
        os.mkdir ('webs_scrapped')
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

def make_url_to_scrap():

    def create_file ():
        
        print ('Previous files: \n' , sorted(os.listdir ('.')))
        file_to_create = input ('\nPlease, insert name for file. >>>\n')
        global file_name
        file_name = file_to_create + '.txt'

        for name in file_name:

            if Path (file_name).is_file():
                print ('File exist. Select new name.')
                create_file ()

        url = input ('\nPlease, insert url to extract text. >>>\n')
        response = requests.get (url)

        soup = BeautifulSoup (response.text, "html.parser")
        paragraph_text = soup.findAll ('p')

        global text_without_html_tags
        text_without_html_tags = re.sub('<[^>]*>', '', str (paragraph_text))

        with open (file_name, 'w') as document:
            document.write (str (text_without_html_tags) )

    def select_action ():

        action = input ('\nSelect option to start:\n[1] Create new file.\n[2] Open old file.\n')

        if action == '1':
            create_file ()
            
        elif action == '2':
            print (sorted(os.listdir ('.')))
            global file_name
            file_selected = input ('\nWhich file do you want to open? >>>\n')
            file_name = file_selected + '.txt'

    select_action ()
    
    return

class Frequency ():

    def __init__ (self, archive):

        self.archive = archive

    def counter (self):
        
        document_text = open (file_name, 'r')
        text_string = document_text.read().lower()
        match_pattern = str (re.findall (r'[a-z]{1,30}', str(unicodedata.normalize ('NFD', text_string).encode('ascii', 'ignore'))))
        global counter_words
        counter_words = collections.Counter (match_pattern.split())
        for word, countered in counter_words.most_common():
            print(f"{word} has been written {countered} {'times' if countered > 1 else 'time'}.")

class Maximum_repeat (Frequency):

    def __init__ (self, archive):

        self.archive = archive

    def counter (self):

        document_text = open (file_name, 'r')
        text_string = document_text.read().lower()
        match_pattern = str (re.findall (r'[a-z]{1,30}', str(unicodedata.normalize('NFD', text_string).encode('ascii', 'ignore'))))
        counter_words = collections.Counter (match_pattern.split())
        for word, countered in counter_words.most_common(1):
            print(f"{word} is the most written with {countered} {'times'}.")

def initiate_program ():

    create_directory ()
    os.chdir ('webs_scrapped')
    make_url_to_scrap ()

    select = input ('\nPlease, select what option do you want:\n[1] Count words.\n[2] Most repeated word.\n\n    Select option: >>> ')

    if select == '1':
        myscrap = Frequency(file_name)
        myscrap.counter()

    elif select == '2':
        myCounter = Maximum_repeat(file_name)
        myCounter.counter()

    else:
        print ('Wrong option.')

    return

initiate_program ()