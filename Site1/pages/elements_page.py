from datetime import time
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.elements_page_locators import *
from generator.generator import *
import allure
import requests
import base64
import os
import random
import time


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.feature("fill all field")
    def fill_all_field(self):
        info = next(get_person())
        full_name = info.full_name
        email = info.email
        current_address = info.current_address
        permanent_address = info.permanent_address
        with allure.step("Filled all field"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            #self.driver.execute_script("window.scrollBy(0, 200);")
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.title("check filled list")
    def check_filled_field(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    @allure.title("open full list")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    @allure.title("click random checkbox")
    def click_random(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 5
        while count !=0:
            item = item_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.title("get checked box")
    def get_checked_box(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        lst = []
        for i in checked_list:
            item = i.find_element("xpath", self.locators.TITLE_ITEM)
            lst.append(item.text)
        return str(lst).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.title("get output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT)
        lst = []
        for i in result_list:
            lst.append(i.text)
        return str(lst).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.title("check click on the radiobutton")
    def click_on_the_radiobutton(self, choice):
        choices = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no' : self.locators.NO_BUTTON
        }
        click_button = self.element_is_visible(choices[choice]).click()

    @allure.title("check get output result")
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.title("add new person")
    def add_new_person(self, count=1):
        while count !=0:
            info = next(get_person())
            first_name = info.first_name
            last_name = info.last_name
            email = info.email
            age = info.age
            salary = info.salary
            department = info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]


    @allure.title("check new added person")
    def check_new_added_person(self):
        people = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for i in people:
            data.append(i.text.splitlines())
        return data

    @allure.title("search people")
    def search_people(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.title("check found person")
    def check_people(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return  row.text.splitlines()

    @allure.title("update person info")
    def update_person_info(self):
        info = next(get_person())
        age = info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.title("delete person")
    def delete_person(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    @allure.title("check deleted person")
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.title("select up to rows")
    def select_up_to_rows(self):
        self.remove_footer()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(By.CSS_SELECTOR, f"""option[value="{i}"]""").click()
            data.append(self.check_count_row())
        return data

    @allure.title("check count rows")
    def check_count_row(self):
        list_row = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_row)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators

    @allure.step('click on different  buttons')
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)


    @allure.step('check clicked button')
    def check_clicked_on_the_button(self, elem):
        return  self.element_is_present(elem).text


class LinksPage(BasePage):
    locators = LinksPageLocators

    def click_on_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        response = requests.get(link_href)
        if response.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return response.status_code


    def click_on_the_broken_link(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return response.status_code


    def click_on_Not_found_link(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return response.status_code


class DownloadPage(BasePage):
    locators = DownLoadPageLocators

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf"D:\Zagruzki\AUTO_DOWNLOAD\{random.randint(0, 999)}.jpg"
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


class UploadPage(BasePage):
    locators = UploadPageLocators

    @allure.step('Upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE).text
        return file_name.split("\\")[-1], text.split("\\")[-1]


class DynamicPage(BasePage):
    locators = DynamicPropertiesPageLocators

    @allure.step("check enable button")
    def check_enable_button(self):
        try:
            enable_button = self.element_is_clicable(self.locators.ENABLE_AFTER_FIVE_SECOND, 5)
        except TimeoutException:
            return "Timeout"
        return True

    @allure.step("check changed of color")
    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(6)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after

    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SECOND)
        except TimeoutException:
            return "Timeout"
        return True









