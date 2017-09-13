#!/usr/bin/python

import subprocess
import time

while(True) :

    output = subprocess.check_output(['bash','-c', "acpi"])
    outlist = output.split()

    if outlist[2] == b'Discharging,' :
        subprocess.call(['notify-send', 'Charger Removed', 'Please reinsert it']);
    time.sleep(900)
