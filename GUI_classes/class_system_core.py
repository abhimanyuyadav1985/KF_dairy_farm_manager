from general_functions import *


class system_core(QtGui.QWidget):

    closed = QtCore.pyqtSignal()

    def __init__(self,parent):
        super(system_core,self).__init__()
        self.parent = parent

        self.grid = QtGui.QGridLayout()

        self.grid.addWidget(create_central_labels("System core settings"),0,0)

        self.pb_activity_groups = QtGui.QPushButton('Activity groups')
        self.pb_activity_groups.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_activity_groups,1,0)

        self.pb_activities = QtGui.QPushButton('Activities')
        self.pb_activities.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_activities,2,0)

        self.pb_association_types = QtGui.QPushButton('Association types')
        self.pb_association_types.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_association_types,3,0)

        self.pb_cattle_groups = QtGui.QPushButton('Cattle groups')
        self.pb_cattle_groups.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_cattle_groups,4,0)

        self.pb_measurement_units = QtGui.QPushButton("Measurement units")
        self.pb_measurement_units.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_measurement_units,5,0)

        self.pb_shifts = QtGui.QPushButton("Shifts")
        self.pb_shifts.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_shifts,6,0)

        self.pb_home = QtGui.QPushButton("Home")
        self.pb_home.clicked.connect(self.close)
        self.grid.addWidget(self.pb_home,7,0)

        for i in range(8,20):
            self.grid.addWidget(create_center_blank(""),i,0)

        self.setLayout(self.grid)

    def close(self):
        self.closed.emit()

    def no_use(self):
        print "This function will be available soon "