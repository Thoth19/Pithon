#!/usr/bin/python

import sys


f     = open(str(sys.argv[1]))
f_new = open("new_" + str(sys.argv[1]),'w+')
for line in f:
    assert("while" not in line)
    assert("for" not in line)
    new_line = line.replace("whale", "while")
    new_line = new_line.replace("wail", "while")
    #new_line = new_line.replace("4", "for")
    new_line = new_line.replace("fur", "for")
    f_new.write(new_line)

f.close()
f_new.close()