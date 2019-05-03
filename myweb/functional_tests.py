from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000/m/5')

        self.assertIn('Title', self.browser.title)
        number_text = self.browser.find_element_by_tag_name('h2')
        count = 0
        for row in number_text:
            count +=1

        self.assertEqual(count,12)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('5 5 5', header_text)

        self.fail('Finish the test!')



if __name__ == '__main__':
    unittest.main(warnings='ignore')