from selenium import webdriver
from PageObjects.InitialPage import InitialPage
from PageObjects.ArraysChallengePage import ArraysChallenge
import platform

AUTHOR_NAME = "Hanish Shetty"


class Test_Solution:

    def test_submit_test(self, setup):
        self.driver = setup
        self.ip = InitialPage(self.driver)
        self.ip.click_render_challenge()
        challenge1 = ArraysChallenge(self.driver)
        no_of_tests = challenge1.get_table_row_count()
        for i in range(1, no_of_tests+1):
            challenge1.fill_value_input(i, challenge1.get_the_answers(i))
        challenge1.fill_value_input(no_of_tests + 1, AUTHOR_NAME)
        challenge1.submit_answer()
        self.driver.quit()
