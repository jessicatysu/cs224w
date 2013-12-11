#!/usr/bin/python

f = open('blah.table')
out = open('blah.table2', 'w')

for line in f:
    s = line.split()
    out.write(line.strip() + " & " + str((float(s[2]) - float(s[4])) /
    float(s[2])) + "\n")
