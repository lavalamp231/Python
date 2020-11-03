import os
import sys
from pynetgear import Netgear
import json
import pymsteams
import time
import re
import pandas as pd

cwd = os.getcwd()
to_remove = ['signal', 'link_rate', 'allow_or_block', 'device_type', 'device_model', 'ssid', 'conn_ap_mac']

def get_p():
    token_location = (cwd + '\\pfile')
    open_token_file = open(token_location, 'r')
    read_token_file = open_token_file.read()
    open_token_file.close()
    return read_token_file

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

netgear = Netgear(password=get_p())
node_list1 = []
node_list2 = []

def get_nodes(mylist):
    for i in netgear.get_attached_devices():
        i = str(i)
        i = i.replace("Device", "",)
        remove_parenthesis = i.replace("(", "{").replace(")", "}")
        f = remove_parenthesis.replace("=", " : ").replace("'", '"')
        a = re.sub(r'\s:', '" :', f)
        a = re.sub(r', ', ', "', a)
        a = re.sub(r'{n', '{"n', a)
        a = re.sub(r'(\s)None', ' "None"', a)
        a = re.sub(r'55" TCL', '55 TCL', a)
        #print(a)
        j = json.loads(a)
        for item in to_remove:
            j.pop(item)
        print(j)
        if j not in mylist:
            mylist.append(j)

get_nodes(node_list1)

df = pd.DataFrame(node_list1)

#df = df.drop(columns=to_remove)


send_microsoft_teams_a_message("start of script:")
send_microsoft_teams_a_message(str(df))

while True:
    time.sleep(30)
    get_nodes(node_list2)
    df2 = pd.DataFrame(node_list2)
    #df2 = df2.drop(columns=to_remove)
    print(len(node_list1))
    print("df2 from while loop")
    print(df2)
    if len(df2) > len(df):
        df = pd.concat([df, df2])
        df = df.drop_duplicates()
        send_microsoft_teams_a_message("node has joined.")
        print("message sent")
        print("df from if df2 > df")
        print(df)
        print("df2 from if df2 > df")
        print(df2)
        # can take last entry in dataframe then add it to df
    if len(df2) < len(df):
        print("df from if df2 < df")
        print(df)
        print("df2 from if df2 < df")
        print(df2)
        send_microsoft_teams_a_message("node has left")
        print("message sent")
            