from configuration import db_ip
import os
from general_functions import *
from db_engine import db_connection_obj

class connection_dock(QtGui.QWidget):

    def __init__(self,parent):
        super(connection_dock,self).__init__()
        self.parent = parent
        self.check_ping()
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(create_central_labels('Ping status'),0,0)
        self.grid.addWidget(decide_and_create_label(self.ping),1,0)
        self.pb_db_conenct = QtGui.QPushButton("Connect to Db")
        self.pb_db_conenct.clicked.connect(self.create_db_connection)
        self.grid.addWidget(self.pb_db_conenct,2,0)

        self.grid.addWidget(create_central_labels("Main Menu"),3,0)

        self.pb_system_core = QtGui.QPushButton("System core")
        self.pb_system_core.clicked.connect(self.parent.show_system_core)
        self.grid.addWidget(self.pb_system_core, 4, 0)

        self.pb_cattles = QtGui.QPushButton("Cattles")
        self.pb_cattles.clicked.connect(self.parent.show_cattle_widget)
        self.grid.addWidget(self.pb_cattles, 5, 0)

        self.pb_health_log = QtGui.QPushButton("Health log")
        self.pb_health_log.clicked.connect(self.parent.show_health_log_widget)
        self.grid.addWidget(self.pb_health_log, 6, 0)

        self.pb_milk_yield = QtGui.QPushButton("Upload Milk Yield")
        self.pb_milk_yield.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_milk_yield, 7, 0)

        self.pb_contacts = QtGui.QPushButton("Contacts")
        self.pb_contacts.clicked.connect(self.parent.show_contacts_widget)
        self.grid.addWidget(self.pb_contacts, 8, 0)

        self.pb_reports = QtGui.QPushButton("Reports")
        self.pb_reports.clicked.connect(self.no_use)
        self.grid.addWidget(self.pb_reports,9, 0)

        self.setLayout(self.grid)



    def check_ping(self):
        hostname = db_ip
        response = os.system("ping -n 1 " + hostname)
        # and then check the response...
        if response == 0:
            self.pingstatus = "Network Active"
            self.ping = True
        else:
            self.pingstatus = "Network Error"
            self.ping = False


    def create_db_connection(self):
        if self.ping:
            self.parent.db_connection_obj = db_connection_obj(self.parent)
        else:
            print "You are not able to ping the database"


    def no_use(self):
        print "This function will be available shortly"