from django.test import TestCase
from .models import *


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='cat1', slug='catslug1')
        Category.objects.create(name='cat2', slug='catslug2')
        Link.objects.create(title='title1', slug='slug1', content='http://content1.ua', stat=0, cat_id=1)

        Statistic.objects.create(lk=Link.objects.create(title='title2', slug='slug2', content='http://content2.ua', stat=0, cat_id=1))

    def test_title_label(self):
        link = Link.objects.get(id=1)
        label = link._meta.get_field('title').verbose_name
        self.assertEquals(label, 'Заголовок')

    def test_title_max_length(self):
        link = Link.objects.get(id=1)
        max_length = link._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_slug_label(self):
        link = Link.objects.get(id=1)
        label = link._meta.get_field('slug').verbose_name
        self.assertEquals(label, 'Слаг')

    def test_slug_max_length(self):
        link = Link.objects.get(id=1)
        max_length = link._meta.get_field('slug').max_length
        self.assertEquals(max_length, 255)

    def test_content_label(self):
        link = Link.objects.get(id=1)
        field_label = link._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Контент')

    def test_content_blank(self):
        link = Link.objects.get(id=1)
        blank = link._meta.get_field('content').blank
        self.assertEquals(blank, True)

    def test_link_get_absolute_url(self):
        link = Link.objects.get(id=1)
        self.assertEquals(link.get_absolute_url(), '/post/slug1/')

    def test_category_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Категория')

    def test_category_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_category_slug_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'URL')

    def test_category_slug_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('slug').max_length
        self.assertEquals(max_length, 255)

    def test_category_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/category/catslug1/')

    def test_statistic_lk_label(self):
        stat = Statistic.objects.get(id=1)
        field_label = stat._meta.get_field('lk').verbose_name
        self.assertEquals(field_label, 'Ссылка')

    def test_statistic_time_label(self):
        stat = Statistic.objects.get(id=1)
        field_label = stat._meta.get_field('time').verbose_name
        self.assertEquals(field_label, 'Время перехода')

    def test_statistic_usr_label(self):
        stat = Statistic.objects.get(id=1)
        field_label = stat._meta.get_field('usr').verbose_name
        self.assertEquals(field_label, 'Пользователь')
