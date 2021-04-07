from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class ArraysChallenge:

    def __init__(self, driver):
        self.driver = driver

    def get_table_row_count(self):
        list_elements = self.driver.find_elements_by_css_selector("tr")
        return len(list_elements)

    def fill_value_input(self, array_num, answer):
        text_input = self.driver.find_element_by_css_selector("input[data-test-id^='submit-" + str(array_num) + "']")
        text_input.clear()
        text_input.send_keys(answer)

    def get_the_answers(self, array_num):
        list_elements = self.driver.find_elements_by_css_selector("tr:nth-child(" + str(array_num) + ") td")
        list_numbers = []
        for i in list_elements:
            list_numbers.append(int(i.text))
        return str(self.get_equal_weighed_lists(list_numbers))

    def submit_answer(self):
        self.driver.find_element_by_xpath("//button[.='Submit Answers']").click()
        assert Wait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(.,'✅')]")))
        self.driver.find_element_by_xpath("//button[.='Close']").click()
        return

    @staticmethod
    def get_equal_weighed_lists(list_numbers):
        for i in range(1, len(list_numbers) - 1):
            if sum(list_numbers[:i]) == sum(list_numbers[i + 1:]):
                return i
        return "null"
