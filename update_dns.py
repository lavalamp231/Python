import os


# Summary: I am trying to update the named files containing the A RECORDS and reverse DNS. If the hostname already exists in the file 
# then ask if they want to update it. If it does not exist then add entry to the A RECORD file. 



i = os.getcwd()

# input_hostname = input("What is the hostname")
# input_ip = input("what is the IP")
# input_hostname = input_hostname + "."

def get_esxi_com():
	esxi_com = i + "\\dns_files\\esxi.com.txt"
	#d = "/var/named/esxi.com"
	with open(esxi_com) as x:
		data = x.read()
		for line in data.split("\n"):
			if "IN A" in line: 
			    print(line.split(" "))
			    list_line = line.split(" ")
			    if input_hostname in list_line:
			    	a = input("hostname already exists - would you like to update the hostname in the DNS record? y = yes; n = no")
			    	if a == int or a != "y" or a != "n":
			    		a = input("hostname already exists - would you like to update the DNS record? y = yes; n = no")
			    	if a == "y":
			    		input_ip_replace = input("what is the IP you are replacing")
			    		line.replace(input_hostname + "IN A " + list_line[3], input_hostname + "IN A " + input_ip_replace)
			    else:
			    	b = input


get_esxi_com()