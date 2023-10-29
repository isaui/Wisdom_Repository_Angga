from django.test import TestCase, Client
from authentication_bookmark.models import CustomUser

# Create your tests here.
class mainTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testmember", member="regular", password="testpassword")
        self.client = Client()
        self.client.login(username="testmember", password="testpassword")
    
    def test_pinjam_url_is_exist(self):
        response = self.client.get('/borrow/details/12/')
        self.assertEqual(response.status_code, 200)

    def test_pinjam_using_template(self):
        response = self.client.get('/borrow/details/12/')
        self.assertTemplateUsed(response, 'pinjambuku.html')
    
    def test_returnbook_is_exist(self):
        response = self.client.get('/borrow/returned/')
        self.assertEqual(response.status_code, 200)
        
    def test_returnbook_using_template(self):
        response = self.client.get('/borrow/returned/')
        self.assertTemplateUsed(response, 'listbukureturn.html')
        
    def test_borrowedbook_is_exist(self):
        response = self.client.get('/borrow/borrowed/')
        self.assertEqual(response.status_code, 200)
        
    def test_borrowedbook_using_template(self):
        response = self.client.get('/borrow/borrowed/')
        self.assertTemplateUsed(response, 'listbukudipinjam.html')