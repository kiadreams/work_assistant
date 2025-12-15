# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x02n\
Q\
MainWindow {\x0d\x0a  \
  background-col\
or: qlineargradi\
ent(spread:pad, \
x1:0, y1:0, x2:1\
, y2:1, stop:0 r\
gba(188, 81, 255\
, 247), stop:0.9\
59596 rgba(140, \
255, 255, 255));\
\x0d\x0a}\x0d\x0a\x0d\x0aQPushButt\
on {\x0d\x0a    font-s\
ize: 14px;\x0d\x0a    \
padding: 10px;\x0d\x0a\
    text-transfo\
rm: uppercase;\x0d\x0a\
    border-radiu\
s: 10px;\x0d\x0a    ba\
ckground-color: \
#f0f0f0;\x0d\x0a}\x0d\x0a\x0d\x0aQ\
PushButton:hover\
 {\x0d\x0a    backgrou\
nd-color: steelb\
lue;\x0d\x0a    border\
-color: darkblue\
;\x0d\x0a    color: wh\
ite;\x0d\x0a}\x0d\x0a\x0d\x0aQPush\
Button#psb_exit \
{\x0d\x0a    padding: \
5px;\x0d\x0a}\x0d\x0a\x0d\x0aQLabe\
l#lbl_app_title \
{\x0d\x0a    font-size\
: 22px;\x0d\x0a    fon\
t-weight: bold;\x0d\
\x0a    color: blue\
;\x0d\x0a    text-tran\
sform: uppercase\
;\x0d\x0a    text-alig\
n: center;\x0d\x0a}\
"

qt_resource_name = b"\
\x00\x06\
\x07\xac\x02\xc3\
\x00s\
\x00t\x00y\x00l\x00e\x00s\
\x00\x09\
\x00(\xad#\
\x00s\
\x00t\x00y\x00l\x00e\x00.\x00q\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9b (\xbaO\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
