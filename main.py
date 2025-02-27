# To make this run on startup, add the following line to /etc/rc.local:
# python <path_to_this_script.py> &

# python 2.7

import time, sys
import os
import subprocess
from subprocess import Popen

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SOUND_FILE = os.path.join(SCRIPT_DIR, '03-White-Noise-10min.mp3')

sound_proc = Popen(["omxplayer", "-o", "local", "--loop", SOUND_FILE])
term_proc = None

print "Disabling WiFi in 2 mins."
time.sleep(2*60)
print "Disabling WiFi..."
term_proc = Popen(["ifconfig", "wlan0", "down"])

while(True):
    time.sleep(10)
    print "OliveMusicBox running."
