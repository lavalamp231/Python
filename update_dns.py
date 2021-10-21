import os


# Summary: I am trying to update the named files containing the A RECORDS and reverse DNS. If the hostname already exists in the file 
# then ask if they want to update it. If it does not exist then add entry to the A RECORD file. 



i = os.getcwd()

input_hostname = input("What is the hostname")
input_hostname = input_hostname + "."
esxi_com = i + "\\dns_files\\esxi.com.txt"

def check_esxi_com():
	#d = "/var/named/esxi.com"
	with open(esxi_com) as x:
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
			    		input_ip_replace = input("what is the IP you are replacing")
			    		line_to_replace = input_hostname + "IN A " + list_line[3], input_hostname + "IN A " + input_ip_replace)
			    		return str(line_to_replace)
			    else:
			    	return False # not replacing; hostname was not found in the file

def update_esxi_com():
	with open(esxi_com, "a+") as x:
		if check_esxi_com() == False: # adding entry
			ip = input("What is the ip you are adding for " + input_hostname)
			x.write(input_hostname + " IN A" + ip)
		else: # replacing the line
			ip = input("What is the ip you are replacing for " + input_hostname)
			print("replacing " + input_hostname + "'s IP in esxi.com")
			x.replace(str(check_esxi_com()), input_hostname + " IN A" + ip)


