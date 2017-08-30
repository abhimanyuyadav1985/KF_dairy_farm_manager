from PyQt4 import QtGui, QtCore
from general_functions import *

class add_new_cattle_widget(QtGui.QWidget):

    closed = QtCore.pyqtSignal()

    def __init__(self,parent):
        super(add_new_cattle_widget,self).__init__()
        self.parent = parent
        self.db_connection_obj = self.parent.db_connection_obj
        self.grid = QtGui.QGridLayout

        status_options = ['True','False']

        self.dict = {
            'id' : [create_center_data('Automatic'),1],
            'name': [QtGui.QLineEdit(),2],
            'age_at_purchase_months' : [QtGui.QLineEdit(),3],
            'status' : [QtGui.QComboBox(),4],
            'group' : [QtGui.QComboBox(),5],
            'purchased_from' : [QtGui.QComboBox(),6],
            'purchase_price' : [QtGui.QLineEdit(),7],
            'sold_to' : [QtGui.QComboBox(),8],
            'selling_price' : [QtGui.QLineEdit(),9]
        } # {label : [widget, row_number]

        self.add_combo_items_to_dict()
        self.add_dict_to_grid()

        self.show

    def add_dict_to_grid(self):

        self.grid.addWidget(create_central_labels("New Cattle form"),0,0,1,2)

        pass

    def add_combo_items_to_dict(self):
        # search contacts and create the contact list + append the combo items
        contact_list = []
        contact_results = self.db_connection_obj.sess.query(self.db_connection_obj.contacts).order_by(self.db_connection_obj.contacts.nick_name).all()
        if contact_results is not None:
            for a_contact in contact_results:
                a_contact_dict = a_contact.__dict__
                contact_list.append(a_contact_dict['nick_name'])
            # Now add to the combo items
            self.dict['purchased_from'][0].addItems(contact_list)
            self.dict['sold_to'][0].addItems(contact_list)
        # search cattle groups and add to combo box
        cattle_group_list = []
        cattle_groups = self.db_connection_obj.sess.query(self.db_connection_obj.cattle_groups).all()
        if cattle_groups is not None:
            for a_cattle_group in cattle_groups:
                a_cattle_group_dict = a_cattle_group.__dict__
                cattle_group_list.append(a_cattle_group_dict['group'])
            # Now add items to the combo box
            self.dict['group'][0].addItems(cattle_group_list)


    def save(self):
        print "This function will be available soon "


    def cancel(self):
        print "This function will be available soon "

    def no_use(self):
        print "This function will be available soon .. "


    def close(self):
        self.closed.emit()