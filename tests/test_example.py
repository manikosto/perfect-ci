import os
import allure
import pytest
from dotenv import load_dotenv

load_dotenv()

@allure.epic("Example")
@allure.feature("Feature")
class TestExample:

    @pytest.mark.smoke
    @allure.title("Test Example")
    def test_example(self):
        with allure.step("Open page"):
            self.driver.get(os.getenv("STAGE"))
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    @pytest.mark.regression
    @allure.title("Test Example 2")
    def test_example_2(self):
        with allure.step("Open page"):
            self.driver.get(os.getenv("STAGE"))
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )