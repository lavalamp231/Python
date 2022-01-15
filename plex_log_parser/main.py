import os
import sys

dir_path = r"/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/"

os.chdir(dir_path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            listofwords = ["gmail", "itary"]
            if all(x in line for x in listofwords):
                print(line)

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if "Plex Media Server" in file:
        #print(file)
        file_path = f"{dir_path}{file}"
  
        # call read text file function
        read_text_file(file_path)