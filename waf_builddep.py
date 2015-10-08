#!/usr/bin/python
"""
Sample code of running package manager in waf script.
"""

import os
from waflib import Logs

def builddep(ctx):
    osname = platform.linux_distribution()
    if osname[0] == 'Fedora':
        pkg = "dnf"
        if int(osname[1]) <= 21:
            pkg = "yum"
        Logs.info(" \"{0}\" will be used on {1} {2}.".format(pkg,osname[0],osname[1]))
        os.system(pkg+' install libgee-devel -y')
    elif osname[0] == 'Debian':
        pkg = "apt-get"
        os.system(pkg+' --assume-yes install libgee-0.8-dev')
        Logs.info(" \"{0}\" will be used on {1} {2}.".format(pkg,osname[0],osname[1]))
    else:
        Logs.warn('Can\'t do anything here!')
        pass
