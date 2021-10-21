import os


# Summary: I am trying to update the named files containing the A RECORDS and reverse DNS. If the hostname already exists in the file 
# then ask if they want to update it. If it does not exist then add entry to the A RECORD file. 



i = os.getcwd()

input_hostname = input("What is the hostname:\n")
input_hostname = input_hostname + "."
esxi_com = i + "\\dns_files\\esxi.com.txt"
d = "/var/named/esxi.com"

def check_esxi_com():
    with open(d) as x:
        data = x.read()
        print(data)     
        for line in data.split("\n"):
            if "IN A" in line: 
                print(line.split(" "))
                list_line = line.split(" ")
                if input_hostname in list_line:
                    a = input("hostname already exists - would you like to update the hostname in the DNS record? y = yes; n = no")
                    if a == int or a != "y" or a != "n":
                        a = input("hostname already exists - would you like to update the DNS record? y = yes; n = no")
                    elif a == "y":
                        line_to_replace = input_hostname + "IN A " + list_line[3]
                        return str(line_to_replace)
                    elif a == "n":
                        exit()
                else:
                    return False # not replacing; hostname was not found in the file

result = check_esxi_com()

def update_esxi_com():
    with open(esxi_com, "a+") as x:
        if result == False: # adding entry
            ip = input("What is the ip you are adding for " + input_hostname)
            x.write("\n" + input_hostname + " IN A" + ip)
        else: # replacing the line
            ip = input("Replacing " + input_hostname + "ip. What is the new ip:")
            print("replacing " + input_hostname + "'s IP in esxi.com")
            x.replace(result, input_hostname + " IN A " + ip)


update_esxi_com()