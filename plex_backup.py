#!/usr/bin/env python
import sys
import os


mount_point_path = "/Plex_backup"
mp = os.path.ismount(mount_point_path)
mount_plex = "mount /Plex_backup"
rsync_command = ["rsync -av /Storage2/Movies/ /Plex_backup/Movies/", "rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/"]

def mount_plexbackup():

	if mp == True:
		print("No errors. Starting rsync.")
		os.cmd(rsync_command)
	else:
		os.cmd(mount_plex)
		if mp == False:
			print("NAS was not mounted exiting")
		else:
			print("NAS was mounted. Starting rsync now.")
			os.cmd(rsync_command)		

		 
