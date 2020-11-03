import os
import sys
from pynetgear import Netgear
import json
import pymsteams
import time
import re
import pandas as pd

cwd = os.getcwd()

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
        mylist.append(j)

get_nodes(node_list1)

column_names = ['Names', 'IP', 'MAC', 'Type']
#df = pd.DataFrame(node_list1)
df = pd.DataFrame(columns=column_names)
df2 = pd.DataFrame(columns=column_names)

for item in node_list1:
    name = item['name']
    ip = item['ip']
    mac = item['mac']
    type_n = item['type']
    my_dict = {'Names': name, 'IP': ip, 'MAC': mac, 'Type': type_n}
    df = df.append(my_dict, ignore_index=True)

send_microsoft_teams_a_message("start of script:")
send_microsoft_teams_a_message(str(df))

while True:
    time.sleep(45)
    get_nodes(node_list2)
    for item in node_list2:
        name2 = item['name']
        ip2 = item['ip']
        mac2 = item['mac']
        type_n2 = item['type']
        my_dict2 = {'Names': name2, 'IP': ip2, 'MAC': mac2, 'Type': type_n2}
        if ip2 not in df2.values:
            df2 = df2.append(my_dict2, ignore_index=True)
        # print("df")
        # print(df)
        # print("df2")
        # print(df2)
        if len(df2) > len(df) and len(node_list1) <= len(df):
            df = pd.concat([df, df2])
            df = df.drop_duplicates()
            send_microsoft_teams_a_message("node has joined.")
            print("message sent")
            print("df from if df2 > df")
            print(df)
            # can take last entry in dataframe then add it to df
        if len(df2) < len(df) and len(node_list1) <= len(df):
            # df = pd.concat([df, df2]) # concat dataframes # Used from https://pythondata.com/quick-tip-comparing-two-pandas-dataframes-and-getting-the-differences/
            # df = df.reset_index(drop=True) # reset the index
            # df_gpby = df.groupby(list(df.columns)) #group by
            # df = [x[0] for x in df_gpby.groups.values() if len(x) == 1] #reindex
            print("df from if df2 < df")
            print(df)
            print("df2 from if df2 < df")
            print(df2)
            if len(df2) > len(df):
                send_microsoft_teams_a_message("node has left")
                print("message sent")
            