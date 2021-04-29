from django.contrib.auth import authenticate
from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import *


class ViewTests(TestCase):
    @classmethod
    def setUp(self):
        Category.objects.create(name='cat1', slug='catslug1')
        Category.objects.create(name='cat2', slug='catslug2')
        Link.objects.create(title='title1', slug='slug1', content='http://content1.ua', stat=0, cat_id=1)
        Link.objects.create(title='title2', slug='slug2', content='http://content2.ua', stat=0, cat_id=1)
        client = Client()

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_logout_view_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_register_view_status_code(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_add_page_view_status_code(self):
        url = reverse('add_page')
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.save()
        user = authenticate(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(url)
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_delete_page_view_status_code(self):
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.save()
        user = authenticate(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('delete_page', args=('slug2',)))
        self.assertEqual(response.status_code, 200)

    def test_post_view_status_code(self):
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.save()
        user = authenticate(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('post', args=('slug1',)))
        self.assertEquals(response.status_code, 200)

    def test_category_view_status_code(self):
        response = self.client.get(reverse('category', args=('catslug1',)))
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, LinkListView)

    def test_login_url_resolves_view(self):
        view = resolve('/login/')
        self.assertEquals(view.func.view_class, LoginUser)

    def test_logout_url_resolves_view(self):
        view = resolve('/logout/')
        self.assertEquals(view.func, logout_user)

    def test_register_url_resolves_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func.view_class, RegisterUser)

    def test_post_url_resolves_view(self):
        view = resolve(reverse('post', args=('slug1',)))
        self.assertEquals(view.func.view_class, LinkDetailView)

    def test_category_url_resolves_view(self):
        view = resolve(reverse('category', args=('catslug1',)))
        self.assertEquals(view.func.view_class, CategoryListView)
