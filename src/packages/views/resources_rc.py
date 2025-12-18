# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xae\
Q\
PushButton {\x0a   \
 font-size: 14px\
;\x0a    padding: 1\
0px;\x0a    text-tr\
ansform: upperca\
se;\x0a    border-r\
adius: 10px;\x0a   \
 background-colo\
r: #f0f0f0;\x0a}\x0a\x0aQ\
PushButton:hover\
 {\x0a    backgroun\
d-color: steelbl\
ue;\x0a    border-c\
olor: darkblue;\x0a\
    color: white\
;\x0a}\x0a\x0aQPushButton\
#psb_exit {\x0a    \
padding: 5px;\x0a}\x0a\
\x0aQLabel#lbl_app_\
title {\x0a    font\
-size: 22px;\x0a   \
 font-weight: bo\
ld;\x0a    color: b\
lue;\x0a    text-tr\
ansform: upperca\
se;\x0a    text-ali\
gn: center;\x0a}\
\x00\x00\x00\xa3\
Q\
MainWindow {\x0a   \
 background-colo\
r: qlineargradie\
nt(spread:pad, x\
1:0, y1:0, x2:1,\
 y2:1, stop:0 rg\
ba(188, 81, 255,\
 247), stop:0.95\
9596 rgba(140, 2\
55, 255, 255));\x0a\
}\x0a\
"

qt_resource_name = b"\
\x00\x06\
\x07\xac\x02\xc3\
\x00s\
\x00t\x00y\x00l\x00e\x00s\
\x00\x13\
\x02\x93\x96\xa3\
\x00m\
\x00a\x00i\x00n\x00_\x00m\x00e\x00n\x00u\x00_\x00s\x00t\x00y\x00l\x00e\x00.\x00q\
\x00s\x00s\
\x00\x15\
\x0b\xe6`\xe3\
\x00m\
\x00a\x00i\x00n\x00_\x00w\x00i\x00n\x00d\x00o\x00w\x00_\x00s\x00t\x00y\x00l\x00e\
\x00.\x00q\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9b2U#y\
\x00\x00\x00>\x00\x00\x00\x00\x00\x01\x00\x00\x01\xb2\
\x00\x00\x01\x9b2U#r\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
