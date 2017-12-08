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
fr = open("/tmp/books.txt", "r")
p = open("/tmp/links_arthur.txt", "w")

# Creating file

for url in soup.find_all('a'):
    f.write(str(url.get('href')) + "\n")
f.close

for line in fr:
    if "arthur" in line:
        p.write(str(line) + "\n")
fr.close


#for line in fr.read():
#    if "arthur" in line:
#        p.write(str(line) + "\n")
#    f.close
