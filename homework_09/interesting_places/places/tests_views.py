from django.test import TestCase


class TestViews(TestCase):

    def test_get_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_create_page(self):
        response = self.client.get('/place/create')
        self.assertEqual(response.status_code, 301)

    def test_context_object_list_is_exist(self):
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)

    def test_context_object_list_is_empty(self):
        response = self.client.get('/')
        self.assertCountEqual(response.context['object_list'], [])

    def test_content_main_title_is_exist(self):
        response = self.client.get('/')
        self.assertIn(b'Welcome to Interesting places!!!', response.content)

    def test_content_contacts_title_is_exist(self):
        response = self.client.get('/')
        self.assertIn(b'Contacts', response.content)

    def test_content_home_title_is_exist(self):
        response = self.client.get('/')
        self.assertIn(b'Home', response.content)


