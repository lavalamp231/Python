#!/usr/bin/env python
import sys
import os
import subprocess
import pdb


mount_point_path = "/Plex_backup"
mp = os.path.ismount(mount_point_path)

def main():
    """ """

    mp_is = check_if()
    if mp_is:
        back_up()

def mount_plexbackup():
    """ """
    try:
        subprocess.call("mount /Plex_backup", shell=True)
    except Exception as e:
        print("shit wrong: {0}".format(e))

def back_up():
    """ """
    subprocess.call("rsync -av /Storage2/Movies/ /Plex_backup/Movies/", shell=True)
    subprocess.call("rsync -av /Storage2/TV-Shows/ /Plex_backup/TV-Shows/", shell=True)

def check_if():
    """ """

    if mp:
        return True
    else:
        mount_plexbackup()
        return False

main()
