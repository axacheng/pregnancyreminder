""" Implements the datastore instances.
"""

from google.appengine.ext import db

class PregnancyGadget(db.Model):
    """ The Main table for all the words. """
    
    weekday = db.IntegerProperty(required=True, default=0)
    description = db.TextProperty(required=True)
    #description = db.TextProperty(required=True, default=db.Text('', encoding='utf_8'))
    
    

