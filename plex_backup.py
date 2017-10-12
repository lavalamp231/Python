#!/usr/bin/env python
import sys
import os
import subprocess

mount_point_path = "/Plex_backup"
mp = os.path.ismount(mount_point_path)
mount_plex = "mount /Plex_backup"
rsync_command = ["rsync -av /Storage2/Movies/ /Plex_backup/Movies/", "rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/"]
str_rsync_command = str(rsync_command)

def mount_plexbackup():

	if mp == True:
		print("No errors. Starting rsync.")
		subprocess.call("rsync -av /Storage2/Movies/ /Plex_backup/Movies/", shell=True)
		subprocess.call("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/", shell=True)
	else:
		subprocess.call("mount /Plex_backup", shell=True)
		if mp == False:
			print("NAS was not mounted exiting")
		else:
			print("NAS was mounted. Starting rsync now.")
		subprocess.call("rsync -av /Storage2/Movies/ /Plex_backup/Movies/", shell=True)
		subprocess.call("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/", shell=True)		

mount_plexbackup()
		 
