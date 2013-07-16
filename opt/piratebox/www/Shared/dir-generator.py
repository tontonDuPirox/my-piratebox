#!/usr/bin/python
# coding=utf8
# -*- coding: utf8 -*-

import os
import os.path

def get_template(name, file):
    printLine = False
    ofi = open(os.path.realpath(file), 'r')
    for line in ofi:
        if printLine == True:
            print line

        if line == "<!-- ÷÷ " + name + " start ++ -->\n":
            printLine = True
        if line == "<!-- ÷÷ " + name + " end ++ -->\n":
            printLine = False

get_template('header', 'shared.html')

print '<table class="table"><thead><tr><th>Nom du fichier</th><th>Taille</th></tr></thead><tbody>'

for name in os.listdir('.'):
    if name != "dir-generator.py" and name != "shared.html":
        real_path = os.path.realpath(name)
        if os.path.isfile(real_path):
            size = os.path.getsize(real_path)
            fileSize = str(size) + "o"
            if (size > 1024):
                fileSize = str(round(size / 1024, 2)) + " Ko"
            if (size > 1024 * 1024.0):
                fileSize = str(round(size / (1024.0 * 1024.0), 2)) + " Mo"
            if (size > 1024 * 1024 * 1024):
                fileSize = str(round(size / (1024.0 * 1024.0 * 1024.0), 2)) + " Go"

            print '<tr><td><a href="/Shared/' + name + '">' + name + '</a></td><td>' + fileSize + '</td></tr>'

print '</tbody></table>'

get_template('footer', 'shared.html')
