# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x02R\
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
}\x0a\x0aQPushButton {\
\x0a    font-size: \
14px;\x0a    paddin\
g: 10px;\x0a    tex\
t-transform: upp\
ercase;\x0a    bord\
er-radius: 10px;\
\x0a    background-\
color: #f0f0f0;\x0a\
}\x0a\x0aQPushButton:h\
over {\x0a    backg\
round-color: ste\
elblue;\x0a    bord\
er-color: darkbl\
ue;\x0a    color: w\
hite;\x0a}\x0a\x0aQPushBu\
tton#psb_exit {\x0a\
    padding: 5px\
;\x0a}\x0a\x0aQLabel#lbl_\
app_title {\x0a    \
font-size: 22px;\
\x0a    font-weight\
: bold;\x0a    colo\
r: blue;\x0a    tex\
t-transform: upp\
ercase;\x0a    text\
-align: center;\x0a\
}\
"

qt_resource_name = b"\
\x00\x06\
\x07\xac\x02\xc3\
\x00s\
\x00t\x00y\x00l\x00e\x00s\
\x00\x15\
\x0b\xe6`\xe3\
\x00m\
\x00a\x00i\x00n\x00_\x00w\x00i\x00n\x00d\x00o\x00w\x00_\x00s\x00t\x00y\x00l\x00e\
\x00.\x00q\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9b\x1e\xc9_\x5c\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
