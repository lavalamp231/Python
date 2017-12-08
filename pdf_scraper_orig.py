#!/usr/bin/env python

import os
import sys
import bs4 as bs
import urllib

# Variables
sauce = urllib.urlopen('https://hackingvision.com/2017/09/22/kali-linux-ebooks-download-pdf-2017/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
f = open("/home/andrew/Documents/book.txt", "w")


# Creating file

def main():
    print("This is sparta!")
    link_populate()
    parse_pdf()

def link_populate():
    for url in soup.find_all('a'):
        f.write(str(url.get('href')) + "\n")

def parse_pdf():
    for line in open("/home/andrew/Documents/book.txt", 'r'):
        if "arthur" in line:
            f.write(str(line) + "\n")

main()
