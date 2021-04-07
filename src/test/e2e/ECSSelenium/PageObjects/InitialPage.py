class InitialPage:
    button_render_challenge_css = "button[data-test-id='render-challenge']"

    def __init__(self, driver):
        self.driver = driver

    def click_render_challenge(self):
        self.driver.find_element_by_css_selector(self.button_render_challenge_css).click()
