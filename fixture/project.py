from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:
    def __init__(self,app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@class='manage-menu-link']").click()
        wd.find_element_by_xpath("//span[text()='Zarządzanie projektami']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_css_selector('#project_name').send_keys(project)
        # wd.find_element_by_css_selector('#project_status').send_keys(project)
        # wd.find_element_by_css_selector('#project-view-state').send_keys(project)
        wd.find_element_by_css_selector('#project-description').send_keys(project)

    #
    # def select_project_by_index(self, index):
    #     wd = self.app.wd
    #     wd.find_element_by_xpath
    #     // h2[text()='Projekty']/following - sibling::table//tr/td
    #     // h2[text() = 'Projekty'] / following - sibling::table // tr / td[1]

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//fieldset//input[@value='Stwórz nowy projekt']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@type='submit'][@value = 'Dodaj projekt']").click()
        element = WebDriverWait(wd, 5).until(expected_conditions.visibility_of_element_located(By.XPATH, "//h2[text() = 'Projekty']"))

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_index[index]
        #submint deletion
        self.return_to_project_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))