#!/usr/bin/env python
import sys
import os


mount_point_path = "/Plex_backup"
mp = os.path.ismount(mount_point_path)
mount_plex = "mount /Plex_backup"
rsync_command = ["rsync -av /Storage2/Movies/ /Plex_backup/Movies/", "rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/"]
str_rsync_command = str(rsync_command)

def mount_plexbackup():

	if mp == True:
		print("No errors. Starting rsync.")
		os.system(rsync_command)
	else:
		os.system(mount_plex)
		if mp == False:
			print("NAS was not mounted exiting")
		else:
			print("NAS was mounted. Starting rsync now.")
			os.system(str_rsync_command)		

mount_plexbackup()
		 
