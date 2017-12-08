#!/usr/bin/env python

import os
import sys
import bs4 as bs
import urllib
from subprocess import call

# Variables
sauce = urllib.urlopen('http://shenanigansnightclub.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
f = open("/tmp/shenanigansnightclub.txt", "w")

# Creating file

def main():
    print("This is sparta!")
    link_populate()

def link_populate():
    for url in soup.find_all('a'):
        f.write(str(url.get('href')) + "\n")


main()
