from configuration import db_ip, db_name, db_port, db_user, db_pass
from sqlalchemy import create_engine,MetaData
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

class db_connection_obj(object):

    def __init__(self,parent):
        self.parent = parent
        self.initialize_db_engine()

    def initialize_db_engine(self):
        engine_definition = str('postgresql://'+ db_user + ":"+db_pass + "@" + db_ip + ":"+ db_port+ "/"+db_name)
        self.parent.logging.info("----------Database engine setup------------")
        self.parent.logging.info('Db engine definition: ' + engine_definition)
        try:
            print "Now setting up DB engine ..",
            self.db_engine =  create_engine(engine_definition, poolclass = QueuePool,echo = False)
            print "Done....."
            self.parent.logging.info("Connection to db engine successful")
            self.initialize_db_Session()
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_db_Session(self):
        try:
            print "Now setting up the Session ....",
            self.Session =  sessionmaker(self.db_engine)
            self.sess = self.Session()
            print "Done....."
            self.parent.logging.info("Db session setup successful")
            self.initialize_metadata()
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_metadata(self):
        try:
            self.metadata_public = MetaData(schema='public')
            self.parent.logging.info("Public metadata created ..")
            self.initialize_base()
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_base(self):
        try:
            self.Base_public = automap_base(metadata = self.metadata_public)
            self.Base_public.prepare(self.db_engine, reflect=True)
            self.parent.logging.info("Public base prepared.. ")
            self.initialize_all_dao()
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_all_dao(self):
        self.initialize_dao_activities()
        self.initialize_dao_activity_groups()
        self.initialize_dao_association_types()
        self.initialize_dao_cattle_association_membership()
        self.initialize_dao_cattle_groups()
        self.initialize_dao_cattle_to_collection_map()
        self.initialize_dao_cattles()
        self.initialize_dao_contacts()
        self.initialize_dao_feed_items()
        self.initialize_dao_health_log()
        self.initialize_dao_measurement_units()
        self.initialize_dao_shifts()
        self.initialize_dao_milk_yield()
        self.parent.logging.info("---------------ALL DAO initialized------------------")
        self.parent.db_connection_status = True


    def initialize_dao_activities(self):
        try:
            print "Now setting up DAO for activities....",
            self.activities = self.Base_public.classes.activities
            print "Done......."
            self.parent.logging.info("DAO for activities created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_activity_groups(self):
        try:
            print "Now setting up DAO for activity groups....",
            self.activity_groups = self.Base_public.classes.activity_groups
            print "Done......."
            self.parent.logging.info("DAO for activity groups created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_association_types(self):
        try:
            print "Now setting up DAO for association types....",
            self.association_types = self.Base_public.classes.association_types
            print "Done......."
            self.parent.logging.info("DAO for association types created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_cattle_association_membership(self):
        try:
            print "Now setting up DAO for cattle association membership....",
            self.cattle_association_membership = self.Base_public.classes.cattle_association_membership
            print "Done......."
            self.parent.logging.info("DAO for cattle association membership created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_cattle_groups(self):
        try:
            print "Now setting up DAO for activity groups....",
            self.cattle_groups = self.Base_public.classes.cattle_groups
            print "Done......."
            self.parent.logging.info("DAO for cattle groups created .. ")
        except Exception as e:
            self.parent.logging.error(e)


    def initialize_dao_cattle_to_collection_map(self):
        try:
            print "Now setting up DAO for cattle to colleciton map ....",
            self.cattle_to_colleciton_map = self.Base_public.classes.cattle_to_collection_map
            print "Done......."
            self.parent.logging.info("DAO for cattle to colleciton map created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_cattles(self):
        try:
            print "Now setting up DAO for activity groups....",
            self.cattles = self.Base_public.classes.cattles
            print "Done......."
            self.parent.logging.info("DAO for activity cattles created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_contacts(self):
        try:
            print "Now setting up DAO for activity groups....",
            self.contacts = self.Base_public.classes.contacts
            print "Done......."
            self.parent.logging.info("DAO for contacts created .. ")
        except Exception as e:
            self.parent.logging.error(e)


    def initialize_dao_feed_items(self):
        try:
            print "Now setting up DAO for feed items....",
            self.feed_items = self.Base_public.classes.feed_items
            print "Done......."
            self.parent.logging.info("DAO for feed items created .. ")
        except Exception as e:
            self.parent.logging.error(e)

    def initialize_dao_health_log(self):
        try:
            print "Now setting up DAO for health log....",
            self.health_log = self.Base_public.classes.health_log
            print "Done......."
            self.parent.logging.info("DAO for health log  created .. ")
        except Exception as e:
            self.parent.logging.error(e)


    def initialize_dao_measurement_units(self):
        try:
            print "Now setting up DAO for measurement units....",
            self.measurement_units = self.Base_public.classes.measurement_units
            print "Done......."
            self.parent.logging.info("DAO for measurement units created .. ")
        except Exception as e:
            self.parent.logging.error(e)


    def initialize_dao_milk_yield(self):
        try:
            print "Now setting up DAO for milk yield....",
            self.milk_yield = self.Base_public.classes.milk_yield
            print "Done......."
            self.parent.logging.info("DAO for milk yield created .. ")
        except Exception as e:
            self.parent.logging.error(e)


    def initialize_dao_shifts(self):
        try:
            print "Now setting up DAO for shifts....",
            self.shifts = self.Base_public.classes.shifts
            print "Done......."
            self.parent.logging.info("DAO for shifts created .. ")
        except Exception as e:
            self.parent.logging.error(e)




