import time
import pytest
import allure
from pages.elements_page import *
import locators

@allure.suite("Main test")
class TestElements:
    @allure.feature("Test Text Box")
    class TestTextBox:
        @allure.title("Test text box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
            time.sleep(5)
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_field()
            time.sleep(5)
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address


    @allure.feature("Test Check Box")
    class TestCheckBox:
        @allure.title("Test check box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random()
            input_checkbox = check_box_page.get_checked_box()
            output_checkbox = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox


    @allure.feature("Test Radio Button")
    class TestRadioButton:

        @allure.title("Check radio button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            #radio_button_list = ['yes', 'impressive', 'no']
            #i = random.choice(random_button_list)
            with allure.step("check click on the buttons"):
                #radio_buttons_list = ["yes", "impressive", "no"]
                radio_button_page.click_on_the_radiobutton('yes')
                output_yes = radio_button_page.get_output_result()
                time.sleep(5)
                radio_button_page.click_on_the_radiobutton('impressive')
                output_impressive = radio_button_page.get_output_result()
                time.sleep(5)
                radio_button_page.click_on_the_radiobutton('no')
                output_no = radio_button_page.get_output_result()
                time.sleep(5)
            print("!!!!!", output_yes, output_no, output_impressive)
            assert output_yes == "Yes" , "Yes radiobutton is not clickable"
            assert output_impressive == "Impressive", "Impressive radiobutton is not clickable"
            assert output_no == "No", "No radiobutton is not clickable"


    @allure.feature("Check webtable")
    class TestWebTable:
        @allure.title("add new person table")
        def test_add_person_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = random.randint(1, 5)
            new_person = web_table_page.add_new_person(count)
            result = web_table_page.check_new_added_person()
            assert  new_person in result, 'a new person is not in the table'

        @allure.title("check people in the table")
        def test_check_people_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_people(key_word)
            table_result = web_table_page.check_people()
            time.sleep(10)
            assert  key_word in table_result, 'The person is not in the table'


        @allure.title("Cheking update the person info")
        def test_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_people(lastname)
            time.sleep(2)
            age = web_table_page.update_person_info()
            time.sleep(2)
            row = web_table_page.check_people()
            time.sleep(2)
            assert age in row, 'The person card has not been changed'


        @allure.title('Delete person from the table')
        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            time.sleep(5)
            web_table_page.search_people(email)
            time.sleep(5)
            web_table_page.delete_person()
            time.sleep(5)
            text = web_table_page.check_deleted()
            assert  text == 'No rows found', "The person card has not been deleted"

        # @allure.title('Check the change in the number of rows in the table')
        # def test_change_rows(self, driver):
        #     web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        #     web_table_page.open()
        #     count = web_table_page.select_up_to_rows()
        #     assert count in [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or '

    @allure.feature("Test Buttons page")
    class TestButtonsPage:
        button = ["double", "right", "click"]

        @pytest.mark.parametrize("item", button)
        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_button(self, driver, item):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button = button_page.click_on_different_button(item)
            assert button in ["You have done a double click", "You have done a right click",
                              "You have done a dynamic click"], f"The button was not pressed"

        @allure.title('Checking clicks of different types version 2')
        def test_different_click_on_the_button_v2(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"


    @allure.feature("Links Page")
    class TestLinkPage:

        @allure.title("Check simple link")
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link()

            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check the broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_the_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or status code is not 400"

        @allure.title("Check the 'Not found' link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_the_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or status code is not 400"

    @allure.feature("Download/Upload files")
    class TestDownloadAndUploadPage:
        @allure.title("Download file")
        def test_download_file(self, driver):
            download_page = DownloadPage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            check = download_page.download_file()
            assert check is True

        @allure.title("Upload file")
        def test_upload_file(self, driver):
            upload_file = UploadPage(driver, "https://demoqa.com/upload-download")
            upload_file.open()
            file_name, result = upload_file.upload_file()
            assert file_name == result, "There is not been upload"

    @allure.feature("check dynamic buttons")
    class TestDynamicButtons:
        @allure.title("check enable button")
        def test_enable_button(self, driver):
            enable_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
            enable_button.open()
            clickable_button = enable_button.check_enable_button()
            assert clickable_button is True, "The button is not enable"

        @allure.title("check changed color")
        def test_check_changed_color(self, driver):
            color_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
            color_button.open()
            color_before, color_after = color_button.check_changed_of_color()
            assert color_after != color_before, "The color is not changed"

        @allure.title("check appear button")
        def test_appear_button(self, driver):
            appear_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
            appear_button.open()
            button = appear_button.check_appear_button()
            assert button is True, "The button don't appear"






