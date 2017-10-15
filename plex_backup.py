#!/usr/bin/env python
import sys
import os
import subprocess
import pdb


mount_point_path = "/Plex_backup"
mp = os.path.ismount(mount_point_path)

#mount_plex = "mount /Plex_backup"
#rsync_command = ["rsync -av /Storage2/Movies/ /Plex_backup/Movies/", "rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/"]
#str_rsync_command = str(rsync_command)

def mount_plexbackup():
    """ """

    mp_is = check_if()
    try:
        if mp_is == False:
            subprocess.call("mount /Plex_backup", shell=True)
    except Exception as e:
        print("shit wrong: {0}".format(e))

    else:
        back_up()
        sys.exit()

    #if mp:
    #    print("No errors. Starting rsync.")
   #     pdb.set_trace()
   #     subprocess.call("rsync -av /Storage2/Movies/ /Plex_backup/Movies/", shell=True)
   #     subprocess.call("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/", shell=True)
   # else:
   #     subprocess.call("mount /Plex_backup", shell=True)
   #     print("NAS could not be mounted. Exiting the script.")
   #     print("NAS was mounted. Starting rsync now.")
   #     subprocess.call("rsync -av /Storage2/Movies/ /Plex_backup/Movies/", shell=True)
   #     subprocess.call("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/", shell=True)

def back_up():
    """ """
    subprocess.call("rsync -av /Storage2/Movies/ /Plex_backup/Movies/", shell=True)
    subprocess.call("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/", shell=True)

def check_if():
    """ """
    if mp:
        return True
    else:
        return False

mount_plexbackup()
