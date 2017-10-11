#!/usr/bin/env python
import sys
import os


mount_point_path = "/Plex_backup"
mp = os.path.ismount(mount_point_path)

def(mount_plexbackup):

	if mp == True:
		print("No errors. Starting rsync.")
		os.cmd ("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/")
		os.cmd ("rsync -av /Storage2/Movies/ /Plex_backup/Movies/")
	else:
		os.cmd ("mount /Plex_backup")
		if mp == False:
			print("NAS was not mounted exiting")
			return()
		else:
			print("NAS was mounted. Starting rsync now.")
			os.cmd ("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/")
			os.cmd ("rsync -av /Storage2/Movies/ /Plex_backup/Movies/")			

		 
