#!/usr/bin/python

import subprocess
import time

while(True) :

    output = subprocess.check_output(['bash','-c', "acpi"])
    outlist = output.split()
    subsentence = "Battery : " \
    + outlist[3].decode("utf-8")

    if outlist[2] == b'Discharging,' :
        subprocess.call(['notify-send', 'Charger Removed', subsentence])
    elif int(outlist[3].decode("utf-8")[:-2]) >= 90  :
        subprocess.call(['notify-send', 'Remove Charger', subsentence])
    time.sleep(600)
