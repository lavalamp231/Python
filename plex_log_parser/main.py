import os
import re
import json

dir_path = r"/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/"
json_file = r"/Misc/Python_git/plex_log_parser/results.json"

os.chdir(dir_path)

# create a dict with user. Need item played, IP, user (key), date, x-plex-device-name
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
                
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if "Plex Media Server" in file:
        file_path = f"{dir_path}{file}"
        read_text_file(file_path)


#need to read results.json file to work off of then add new entries. 

if bool(user_dict):
    with open(json_file, 'r+') as f:
        d = json.load(f)
        d.update(user_dict)
        f.seek(0)
        json.dump(d, f)