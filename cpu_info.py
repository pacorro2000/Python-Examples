#!/usr/bin/env python

"""
Obteniendo informacion del CPU
"""

from __future__ import print_function
from collections import OrderedDict
import pprint

def cpuinfo():
    cpuinfo=OrderedDict()
    procinfo=OrderedDict()

    nprocs = 0
    with open("/proc/cpuinfo") as f:
        for line in f:
            procinfo=OrderedDict()
        else:
            if len(line.split(":")) == 2:
                procinfo[line.split(":")[0].strip()] = line.split(":")[1].strip()
            else:
                procinfo[line.split(":")[0].strip()] = ""

    return cpuinfo

if __name__ == '__main__':
    cpuinfo = cpuinfo()
    for processor in cpuinfo.keys():
        print(cpuinfo[processor]["model name"])
