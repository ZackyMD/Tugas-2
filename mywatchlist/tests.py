from django.test import TestCase, Client
from urllib import response
from django.urls import resolve

# Create your tests here.
class TestPy(TestCase):
    def testHtml(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def testJson(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def testXml(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)



