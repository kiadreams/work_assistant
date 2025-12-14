# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01D\
Q\
MainWindow {\x0d\x0a  \
  background-col\
or: rgb(55, 55, \
55);\x0d\x0a}\x0d\x0a\x0d\x0aQPush\
Button {\x0d\x0a    fo\
nt-size: 14px;\x0d\x0a\
    padding: 10p\
x;\x0d\x0a    text-tra\
nsform: uppercas\
e;\x0d\x0a}\x0d\x0a\x0d\x0aQPushBu\
tton#psb_exit {\x0d\
\x0a    padding: 5p\
x;\x0d\x0a}\x0d\x0a\x0d\x0aQLabel#\
lbl_app_title {\x0d\
\x0a    font-size: \
22px;\x0d\x0a    color\
: blue;\x0d\x0a    tex\
t-transform: upp\
ercase;\x0d\x0a    tex\
t-align: center;\
\x0d\x0a}\
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
\x00\x00\x01\x9b\x1d\xc1\xccN\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
