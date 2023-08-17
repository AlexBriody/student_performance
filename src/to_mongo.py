# Import statements
from base import Base
from dotenv import load_dotenv
import pymongo
import os
import pandas as pd

# Class Declaration 
class ToMongo(Base):
   
    def __init__(self, filepath, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        # Initialize the instance of our inherited class:
        Base.__init__(self)
        
        # Call the clean_and_process_data method to initialize the df attribute
        self.clean_and_process_data(filepath)
        
        # Load the env variables:
        load_dotenv()
        self.user = user
        self.password = password
        self.mongo_url = os.getenv('MONGO_URL')
        
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        
        # Create a database
        self.db = self.client.db
        
        # Create a collection
        self.cards = self.db.cards
        
        # Set dataframe index to the id column:
        self.df.set_index('id', inplace=True)

    def upload_one_by_one(self):
        """
        Upload all our items to MongoDB, one-by-one.
        This method will take longer, but will ensure all our data is uploaded correctly!
        """
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

if __name__ == '__main__':
    filepath = '/Users/alexanderbriody/Desktop/Coding Temple/Data-Analytics-Projects/Week_6/student_performance/student_performance/student-mat.csv'
    c = ToMongo(filepath)
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all Card Info to')
