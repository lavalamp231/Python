import os
import sys

dir_path = r"/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/"
file_path = r"/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/Plex Media Server.log"
#log_dir = '/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Logs/Plex\ Media\ Server.1.log'
# with open(file_path, "r") as r:
#     for line in r:
#         if "gmail" in line:
#             print(line)


os.chdir(dir_path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if "Server" in file:
        print(file)
        file_path = f"{dir_path}{file}"
  
        # call read text file function
        read_text_file(file_path)