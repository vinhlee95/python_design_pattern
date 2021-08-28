class Database:
    """
    Singleton Database class
    The goal is to store and hold only 1 instance of the database.
    """
    def __init__(self):
        """
        ⚠️⚠️⚠️⚠️⚠️⚠️
        This is the main problem with this singleton class.
        This initializer gets called RIGHT AFTER __new__ so even though we eventually return only 1 instance of the DB,
        the initializer is still called twice or more.
        """
        print("Loading DB...")
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


db_instance_1 = Database()
db_instance_2 = Database()
print(db_instance_1 == db_instance_2)
