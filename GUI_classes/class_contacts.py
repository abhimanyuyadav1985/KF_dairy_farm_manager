from PyQt4 import QtGui, QtCore
from general_functions import *

class contacts_widget(QtGui.QWidget):
    closed = QtCore.pyqtSignal()

    def __init__(self,parent):

        super(contacts_widget, self).__init__()
        self.parent = parent
        self.grid = QtGui.QGridLayout()

        self.grid.addWidget(create_central_labels("Contacts"),0,0)

        self.pb_add = QtGui.QPushButton('Add')
        self.pb_add.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_add, 1, 0)

        self.pb_show = QtGui.QPushButton("Show")
        self.pb_show.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_show,2,0)

        self.pb_edit = QtGui.QPushButton('Edit')
        self.pb_edit.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_edit, 3, 0)

        self.pb_del = QtGui.QPushButton('Delete')
        self.pb_del.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_del, 4, 0)

        self.pb_home = QtGui.QPushButton('Home')
        self.pb_home.clicked.connect(self.parent.show_blank_screen)
        self.grid.addWidget(self.pb_home, 5, 0)

        for i in range(6,15):
            self.grid.addWidget(create_center_blank(""),i,0)

        self.setLayout(self.grid)


    def no_use(self):
        print "This function will be avaiable sonn "

    def close(self):
        self.closed.emit()