import os
import sys
import re

dir_path = r"/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/"

os.chdir(dir_path)
user_dict = dict()

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            listofwords = ["WAN", "title="]
            if all(x in line for x in listofwords):
                movie = re.search('title=(.+?) ', line).group(1)
                user = re.search('Signed-in Token \((.+?)\) ', line).group(1)
                ip_address = re.search('Request: \[(.+?):', line).group(1)
                date = re.search('^(.+?)\[', line).group(1)
                Plex_device_name = re.search('X-Plex-Device-Name => (.+?)\ \/', line).group(1)
                user_dict[date] = {'User': user, 'Movie': movie, 'IP address': ip_address, 'Plex_device_name': Plex_device_name}
                #print(user_dict)
                # print(user)
                # print(movie)
                # print(ip_address)
                # print(date)
                
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if "Plex Media Server" in file:
        file_path = f"{dir_path}{file}"
        # call read text file function
        read_text_file(file_path)

# create a dict with user. Need item played, IP, user (key), date, x-plex-device-name

print(user_dict)