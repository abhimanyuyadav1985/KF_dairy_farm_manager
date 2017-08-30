import logging
from configuration import version, media_path
import os
from general_functions import *
import sys
from class_connection import connection_dock
from class_system_core import system_core
from class_cattle import cattle_widget
from class_health_log import health_log_widget
from class_contacts import contacts_widget

####################################################################################################################################
###Main window
####################################################################################################################################


class Top_Window(QtGui.QMainWindow):

    """

    Top_window is the main window for the application

    """

    closed = QtCore.pyqtSignal()


    def __init__(self,log_file_path):

        """
        Initialization protocol =>


        :param log_file_path:
        """

        super(Top_Window, self).__init__()
        # Create the logging services 1st so that all the executions can be logged
        self.db_connection_status = False
        self.add_logger(log_path=log_file_path)
        self.layout = QtGui.QGridLayout()
        self.default_central_widget = QtGui.QWidget(self)
        self.default_central_widget.setLayout(self.layout)
        self.setCentralWidget(self.default_central_widget)
        self.statusBar()

        #------creating the top window------------

        self.set_window_title_and_icon()
        self.set_dummy_central_widget()
        self.set_logo_and_title()
        self.add_connection_dock()
        self.show_blank_screen()

        #-----------------------------------------

        self.show()

#-----------------------------------------------------------------------------+
    # Functions for Top window GUI
#------------------------------------------------------------------------------+

    def add_logger(self,log_path):
        """
        Start application loggin service using the path specified
        :param log_path: path to the log file for current execution
        :return: None
        """

        self.logging = logging
        self.logging.basicConfig(level=logging.DEBUG,
                                 format='%(asctime)s %(levelname)-8s %(message)s',
                                 datefmt='%a, %d %b %Y %H:%M:%S',
                                 filename=log_path,
                                 file_mode='w')
        self.logging.info('Logging services setup done ....')





    def set_window_title_and_icon(self):
        """
        Add application version from configuration.__init__()

        Add polarcus logo from images in media

        :return: none
        """
        title = "Krishna Farms Dairy Manager" + version
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(),media_path,'LOGO.png')))# change this in the future

        self.logging.info("Application Title and Polarcus Logo set")



    def set_dummy_central_widget(self):
        """
        Sets a dummy empty widget

        :return: none
        """
        self.working_widget = QtGui.QWidget()
        self.layout.addWidget(self.working_widget, 1, 1)

        self.logging.info("Dummy central widget set")

    def set_logo_and_title(self):
        """
        Add various widget titles and Polarcus logo to the application

        :return: none
        """
        logo = QtGui.QLabel()
        myPixmap = QtGui.QPixmap(os.path.join(os.getcwd(),media_path,'LOGO.png'))
        pixmap_resized = myPixmap.scaled(200, 50, QtCore.Qt.KeepAspectRatio)
        logo.setPixmap(pixmap_resized)
        logo.setFixedSize(200,50)
        self.layout.addWidget(logo,0,0)
        #Addition of window title
        ca_title = create_central_labels('KF Dairy Farm manager')
        ca_title.setStyleSheet('background-color: rgb(140,198,63);color: black')
        ca_title.setFont(QtGui.QFont('SansSerif', 20))
        self.layout.addWidget(ca_title,0,1)
        ############ ading label for status info
        self.logging.info("Application layout title elements set")

    def add_connection_dock(self):
        self.connection_dock = connection_dock(self)
        self.layout.addWidget(self.connection_dock,1,0)
        self.connection_dock.setMaximumHeight(300)

    def show_blank_screen(self):
        self.layout.itemAtPosition(1, 1).widget().deleteLater()
        blank_screen = QtGui.QLabel()
        myPixmap = QtGui.QPixmap(os.path.join(os.getcwd(), media_path, 'blank.jpg'))
        pixmap_resized = myPixmap.scaled(800, 550, QtCore.Qt.KeepAspectRatio)
        blank_screen.setPixmap(pixmap_resized)
        self.layout.addWidget(blank_screen, 1, 1)


    def show_system_core(self):
        # if self.db_connection_status == False:
        #     print " You are not connected to the database , please connect to the database first !!"
        # else:
        self.layout.itemAtPosition(1, 1).widget().deleteLater()
        self.working_widget = system_core(self)
        self.layout.addWidget(self.working_widget, 1, 1)
        self.layout.update()
        self.setFixedSize(self.minimumSizeHint())
        self.working_widget.closed.connect(self.show_blank_screen)


    def show_cattle_widget(self):
        # if self.db_connection_status == False:
        #     print " You are not connected to the database , please connect to the database first !!"
        # else:
        self.layout.itemAtPosition(1, 1).widget().deleteLater()
        self.working_widget = cattle_widget(self)
        self.layout.addWidget(self.working_widget, 1, 1)
        self.layout.update()
        self.setFixedSize(self.minimumSizeHint())
        self.working_widget.closed.connect(self.show_blank_screen)

    def show_health_log_widget(self):
        # if self.db_connection_status == False:
        #     print " You are not connected to the database , please connect to the database first !!"
        # else:
        self.layout.itemAtPosition(1, 1).widget().deleteLater()
        self.working_widget = health_log_widget(self)
        self.layout.addWidget(self.working_widget, 1, 1)
        self.layout.update()
        self.setFixedSize(self.minimumSizeHint())
        self.working_widget.closed.connect(self.show_blank_screen)


    def show_contacts_widget(self):
        # if self.db_connection_status == False:
        #     print " You are not connected to the database , please connect to the database first !!"
        # else:
        self.layout.itemAtPosition(1, 1).widget().deleteLater()
        self.working_widget = contacts_widget(self)
        self.layout.addWidget(self.working_widget, 1, 1)
        self.layout.update()
        self.setFixedSize(self.minimumSizeHint())
        self.working_widget.closed.connect(self.show_blank_screen)

    def closeEvent(self,event):
        self.closed.emit()
        #self.db_engine.dispose()
        try:
            self.db_connection_obj.db_engine.dispose()
            sys.exit()
        except:
            sys.exit()