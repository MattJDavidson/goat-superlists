from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # edith has heard abouyt a cool new online to-do app She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # she is invited to enter a to-do item straight away

        # she types "Buy peacock feathers" into a text box 

        # when she hits enter, the page updates, and now the page lists
        # "Buy peacock feathers" into a text box" as an item in a to-do list

        # There is still a text box invited her to add another item. She 
        # enters "Use peacock feathers to make a fly"

        # the page updates again and now shoes both items on her list

        # edith wonders whether the site will remember he r list. The she sees
        # that the site has generated a unique URL for her -- there is some 
        # explanatory text to that effect

        # she visits that URL - her to-do list is still there.

        # satisied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
