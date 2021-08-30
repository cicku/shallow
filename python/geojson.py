#!/usr/bin/python3

#
# A very simple script to truncate coordinates generated from http://geojson.io/
#

def containsNumber(v):
    if True in [ch.isdigit() for ch in v]:
        return True
    return False

def containsDash(v):
    if True in [ch == "-" for ch in v]:
        return True
    return False

o = open("2.geojson", 'w')

with open("1.geojson", 'r') as f:
    lines = f.readlines()
    for line in lines:
        if containsNumber(line) == True and containsDash(line) == False:
            line = line[0:27] + '\n'
            o.write(line)
        elif containsNumber(line) == True and containsDash(line) == True:
            line = line[0:28] + ',' + '\n'
            o.write(line)
        #elif containsNumber(line) == False:
        #    o.write(line)
        else:
            o.write(line)
o.close()
