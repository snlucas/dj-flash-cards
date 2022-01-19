from django.test import TestCase


class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        '''Check if url status code is ok'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, 'Hompage status code is not properly working.')

    def test_home_page_uses_correct_template(self):
        '''Check if template file is ok'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'flash_card/home.html')
