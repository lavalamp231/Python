#!/usr/bin/env python

import os
import sys
import bs4 as bs
import urllib
from subprocess import call

# Variables
sauce = urllib.urlopen('https://hackingvision.com/2017/09/22/kali-linux-ebooks-download-pdf-2017/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
f = open("/tmp/books.txt", "w")


# Creating file

def main():
    print("Creating txt file in tmp directory")
    link_populate()
    parse_pdf()

def link_populate():
    for url in soup.find_all('a'):
        f.write(str(url.get('href')) + "\n")
    f.close

def parse_pdf():
    for line in f.append():
        if "arthur" in line:
            f.write(str(line) + "\n")
    f.close

main()
