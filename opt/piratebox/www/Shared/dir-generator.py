#!/usr/bin/python
# coding=utf8
# -*- coding: utf8 -*-

import os
import os.path

movie_types = [ 'mkv', 'mpg','mpeg','avi','wmv' ]
sound_types = [ 'mp3','wav','mp4','wma','aif','aiff','ram', 'midi','mid','asf','au','flac' ]
image_types = [ 'jpg','jpeg','gif','png','tif','tiff','bmp','ico' ]
archive_types = [ 'zip','cab','7z','gz','tar.bz2','tar.gz','tar','rar', ]
document_types = [ 'txt','text','doc','docx','abw','odt','pdf','rtf','tex','texinfo' ]
font_types = [ 'ttf','otf','abf','afm','bdf','bmf','fnt','fon','mgf','pcf','ttc','tfm','snf','sfd' ]
sub_types = [ 'srt' ]

def get_template(name, file):
    printLine = False
    ofi = open(os.path.realpath(file), 'r')
    for line in ofi:
        if line == "<!-- ÷÷ " + name + " end ++ -->\n":
            printLine = False

        if printLine == True:
            print line

        if line == "<!-- ÷÷ " + name + " start ++ -->\n":
            printLine = True

def file_size(file):
    real_path = os.path.realpath(file)
    size = os.path.getsize(real_path)

    fileSize = str(size) + " o"
    if (size > 1024 * 1024 * 1024 * 1024):
        fileSize = str(round(size / (1024.0 * 1024.0 * 1024.0 * 1024.0), 2)) + " To"
    elif (size > 1024 * 1024 * 1024):
        fileSize = str(round(size / (1024.0 * 1024.0 * 1024.0), 2)) + " Go"
    elif (size > 1024 * 1024.0):
        fileSize = str(round(size / (1024.0 * 1024.0), 2)) + " Mo"
    elif (size > 1024):
        fileSize = str(round(size / 1024, 2)) + " Ko"

    return fileSize

def file_type(file):
    type = " - "

    extension = os.path.splitext(file)[1][1:]
    if extension in movie_types:
        type = "Vid&eacute;o"
    elif extension in sound_types:
        type = "Audio"
    elif extension in image_types:
        type = "Image"
    elif extension in archive_types:
        type = "Archive"
    elif extension in document_types:
        type = "Document"
    elif extension in font_types:
        type = "Police"
    elif extension in sub_types:
        type = "Sous titres"

    return type

get_template('header', 'shared.html')

files = os.listdir('.')

if len(files) == 2:
    print '<p>Aucun fichier pour le moment.</p>'
else:
    print '<table class="table"><thead><tr><th>Nom du fichier</th><th>Type</th><th>Taille</th></tr></thead><tbody>'

    for file in files:
        if file != "dir-generator.py" and file != "shared.html":
            real_path = os.path.realpath(file)
            if os.path.isfile(real_path):
                print '<tr><td><a href="/Shared/' + file + '">' + file + '</a></td><td>' + file_type(file) + '</td><td>' + file_size(file) + '</td></tr>'

    print '</tbody></table>'

get_template('footer', 'shared.html')
