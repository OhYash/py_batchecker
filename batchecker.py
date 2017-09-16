#!/usr/bin/python

import subprocess
import time

while(True) :

    output = subprocess.check_output(['bash','-c', "acpi"])
    outlist = output.split()
    subsentence = "Battery : "+outlist[3].decode("utf-8")
    subsentence = subsentence[:-2]+'%'
    print(subsentence)

    if outlist[2] == b'Discharging,' :
        subprocess.call(['notify-send', 'Charger Removed', subsentence])
    time.sleep(600)
