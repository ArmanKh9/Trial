#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:51:56 2018

@author: arman
"""

import PIL.Image
img = PIL.Image.open('/home/arman/Desktop/IMG_1586.jpg')
exif_data = img._getexif()
print(exif_data)

import PIL.ExifTags
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

print(exif)