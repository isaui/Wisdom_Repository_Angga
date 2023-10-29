from django.test import TestCase
from django.urls import reverse
from .models import Buku, Rating

class BukuViewsTestCase(TestCase):
    def setUp(self):
        self.rating = Rating.objects.create(
            rating=5
        )
        self.book = Buku.objects.create(
            isbn='1234567890',
            judul='Test Book',
            penulis='Test Author',
            tahun=2022,
            kategori='Test Category',
            gambar='test.jpg',
            deskripsi='Test description',
            rating=self.rating
        )

    def test_search_books_view(self):
        form_data = {'query': 'Test'}  
        response = self.client.post(reverse('daftar_buku:search'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Test Book')

    def test_sort_books_view(self):
        response = self.client.get(reverse('daftar_buku:sort', args=['judul']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_book_details_view(self):
        response = self.client.get(reverse('daftar_buku:book_details'), {'id': self.book.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['judul'], self.book.judul)

    def test_show_xml_view(self):
        response = self.client.get(reverse('daftar_buku:show_xml', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_show_main_view(self):
        response = self.client.get(reverse('daftar_buku:show_main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_get_books_json_view(self):
        response = self.client.get(reverse('daftar_buku:get_books_json'))
        self.assertEqual(response.status_code, 200)

    def test_get_user_view(self):
        response = self.client.get(reverse('daftar_buku:get_user'))
        self.assertEqual(response.status_code, 200)

    def test_get_buku_by_author_view(self):
        response = self.client.post(reverse('daftar_buku:get_buku_by_author'), {'query': 'Test Author'})
        self.assertEqual(response.status_code, 200)
