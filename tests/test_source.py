import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('ars-technica','Ars Technica.','http://arstechnica.com','The PC enthusiasts resource. Power users and the tools they love, without computing religion.')

    def test_instance(self):
        '''
        Test to check new source instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))