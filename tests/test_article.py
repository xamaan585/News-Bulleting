import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article("https://as01.epimg.net/futbol/imagenes/2021/10/31/primera/1635694624_171624_1635694850_noticia_normal.jpg",
                                   "Getafe - Espanyol en directo: LaLiga Santander, hoy, en vivo - AS ","Sergio López de Vicente",
                                   "Sigue el Getafe vs Espanyol en vivo y en directo, jornada 12 de LaLiga Santander que se disputa hoy, 31 de octubre, a las 18:30h, en el Coliseum.",
                                   "2021-10-31T16:31:07Z","https://as.com/futbol/2021/10/31/primera/1635694624_171624.html")

    def test_instance(self):
        '''
        Test to check creation of article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))