import sys
from PyQt4 import QtGui
from general_functions import *

class cattle_widget(QtGui.QWidget):

    closed = QtCore.pyqtSignal()

    def __init__(self,parent):
        super(cattle_widget,self).__init__()

        self.parent = parent
        self.grid = QtGui.QGridLayout()

        self.cattle_buttons = cattle_buttons(self.parent)
        self.grid.addWidget(self.cattle_buttons,2,0)

        self.grid.addWidget(create_central_labels('Cattle Widget'),0,0)

        self.cattle_table = cattle_table(self.parent)
        self.grid.addWidget(self.cattle_table,1,0)

        self.setLayout(self.grid)


    def close(self):
        self.closed.emit()


class cattle_table(QtGui.QScrollArea):
    def __init__(self,data):
        super(cattle_table,self).__init__()
        self.data = data
        pass


class cattle_buttons(QtGui.QWidget):
    def __init__(self,parent):
        super(cattle_buttons,self).__init__()
        self.parent = parent
        self.grid = QtGui.QGridLayout()

        self.pb_add = QtGui.QPushButton('Add')
        self.pb_add.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_add,0,0)

        self.pb_show = QtGui.QPushButton("Show")
        self.pb_show.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_show,0,1)

        self.pb_edit = QtGui.QPushButton('Edit')
        self.pb_edit.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_edit,0,2)

        self.pb_del = QtGui.QPushButton('Delete')
        self.pb_del.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_del,0,3)

        self.pb_home = QtGui.QPushButton('Home')
        self.pb_home.clicked.connect(self.parent.show_blank_screen)
        self.grid.addWidget(self.pb_home,0,4)

        self.setLayout(self.grid)


    def no_use(self):
        print "This function will be available soon .."