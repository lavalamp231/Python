# This scripts purpose is to gather do a nmap_version_detection scan of the IPs in the 192.168.0.* subnet and create a spreadsheet. 

import os
import nmap3
import pandas as pd
import time
import pymsteams

# Gathering all the IPs in 192.168.0.* and then appending them into an empty list called ips

####################### GLOBAL VARIBALS #################################
cwd = os.getcwd()
ip_list_1 = []
ip_list_2 = []
nm = nmap3.Nmap()
nm_scan = nmap3.NmapScanTechniques()
host_discovery_results = nm_scan.nmap_ping_scan("192.168.0.*")

#########################################################################


##################### FUNCTIONS ########################################

def get_ips(ips_list):
    for item in host_discovery_results:
        #ip_address = item['addresses'][0]['addr']
        ips_list.append(item)

def get_webhook():
    token_location = (cwd + '\\url')
    open_token_file = open(token_location, 'r')
    read_token_file = open_token_file.read()
    open_token_file.close()
    return read_token_file

def send_microsoft_teams_a_message(message):
    url2 = get_webhook()
    #print(type(url2))
    myTeamsMessage = pymsteams.connectorcard(url2)
    # Add text to the message.
    myTeamsMessage.text(message)
    # send the message.
    myTeamsMessage.send()

def get_difference(dataframe1, dataframe2):
    for element in dataframe1.values:
        if element not in dataframe2.values:
            return element
    else:
        return element


#######################################################################


#Populating the first list to be static for comparison for later
get_ips(ip_list_1)

df1 = pd.DataFrame(ip_list_1)
send_microsoft_teams_a_message("start of script:")
send_microsoft_teams_a_message(str(df1))


##################### While loop start  - Will continuously run to scan network #################


while True:
    ip_list_2 = []
    time.sleep(30)
    get_ips(ip_list_2)
    df2 = pd.DataFrame(ip_list_2)
    if len(df2) > len(df1):
        df1 = pd.concat([df1, df2])
        df1 = df1.drop_duplicates()
        node_added = str(get_difference(df2, df))
        send_microsoft_teams_a_message("node has joined."+ '\n' + node_added)
        print("message sent")
        print("df from if df2 > df1")
        print(df1)
        print("df2 from if df2 > df1")
        print(df2)
        # can take last entry in dataframe then add it to df
    if len(df2) < len(df1):
        print("df from if df2 < df1")
        print(df1)
        print("df2 from if df2 < df1")
        print(df2)
        node_left = str(get_difference(df1, df2))
        send_microsoft_teams_a_message("node left"+ '\n' + node_left)
        print("message sent")
        # Refresh the static df dataframe
        ip_list_1 = []
        get_ips(ip_list_1)
        df1 = pd.DataFrame(ip_list_1)


    