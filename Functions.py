import os
import json
import Creds
import random
import gspread
import xml.dom
import wsgiref
import asyncio
import webbrowser
import http.cookies
import pyperclip as pc
from time import sleep
import distutils.version
import importlib.resources
import wsgiref.simple_server
from PySide2.QtWidgets import *
from multiprocessing import Queue
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from UserInterface import Ui_MainWindow as design
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from PySide2.QtCore import QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QPoint


class Package:
    @staticmethod
    def help():
        print("This will be available in the future")
        # webbrowser.open('https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python')
    @staticmethod
    def copy_email(program_path): # To change the json file every time the user click on copy email
        try:
            with open(f'{program_path}\Email.txt', mode="r+", encoding="utf-8") as file:
                email = file.read()
                if email == "Email1":
                    file.truncate(0)
                    file.seek(0)
                    file.write("Email2")
                    pc.copy(Creds.email_1)
                elif email == "Email2":
                    file.truncate(0)
                    file.seek(0)
                    file.write("Email3")
                    pc.copy(Creds.email_2)
                elif email == "Email3":
                    file.truncate(0)
                    file.seek(0)
                    file.write("Email4")
                    pc.copy(Creds.email_3)
                elif email == "Email4":
                    file.truncate(0)
                    file.seek(0)
                    file.write("Email1")
                    pc.copy(Creds.email_4)
                else:
                    file.truncate(0)
                    file.seek(0)
                    file.write("Email2")
                    pc.copy(Creds.email_1)

                file.close()

        except FileNotFoundError:
            with open(f'{program_path}\Email.txt', 'w+', encoding="utf-8") as file:
                pc.copy(Creds.email_1)
                file.writelines("Email2")
                file.close()

    @staticmethod
    def load_txt(user_interface, name):
        try:
            with open(f'{os.path.expanduser("~")}\AppData\Local\Youtube Auto Commenter\{name}.txt', 'r+',
                      encoding="utf-8") as file:
                try:
                    user_interface.setText(str(file.read()))
                except AttributeError:
                    user_interface.setPlainText(str(file.read()))
        except FileNotFoundError:
            pass

    @staticmethod
    def save_txt(name, value):
        with open(f'{os.path.expanduser("~")}\AppData\Local\Youtube Auto Commenter\{name}.txt', 'w+',
                  encoding="utf-8") as file:
            file.writelines(str(value))

    @staticmethod
    def access_google_spreadsheet(sheet, worksheet, creds):
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            f"{os.path.expanduser('~')}\AppData\Local\Youtube Auto Commenter\{creds}.json", scope)
        client = gspread.authorize(credentials)
        sheet_acess = client.open(sheet).worksheet(worksheet)
        return sheet_acess

    @staticmethod
    def create_json(credentials, name):
        # Creating Json File
        try:
            os.mkdir(f"{os.path.expanduser('~')}\AppData\Local\Youtube Auto Commenter")
        except FileExistsError:
            if not os.path.isfile(f"{os.path.expanduser('~')}\AppData\Local\Youtube Auto Commenter\{name}.json"):
                with open(f"{os.path.expanduser('~')}\AppData\Local\Youtube Auto Commenter\{name}.json", "w") as j:
                    j.write(json.dumps(credentials))

    def control_chrome(profile):
        chrome_path = f"{os.path.expanduser('~')}\AppData\Local\Google\Chrome"
        options = uc.ChromeOptions()
        options.user_data_dir = f"{chrome_path}\{profile}"
        chrome = uc.Chrome(options=options)
        chrome.get('https://accounts.google.com/v3/signin/identifier?dsh=S671521857%3A1675831651951465&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHfoAVlNGBvVIsAX-Ta_I5K6P5WPiU-RdwmsfSHaVVVDhE46RpCljdYHfzJRqfzjGjCht6y_sw')
        return chrome

    @staticmethod
    def comment(chrome, comment, sheet, start_from_row):
        # Skip ad
        try:
            WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '//*[@class="ytp-ad-skip-button-slot"]/span/button[@class="ytp-ad-skip-button ytp-button"]')))
            chrome.find_element(By.XPATH,
                                '//*[@class="ytp-ad-skip-button-slot"]/span/button[@class="ytp-ad-skip-button ytp-button"]').click()
        except TimeoutException:
            pass

        # Turn off autoplay
        try:
            chrome.find_element(By.XPATH,
                                '//*[@class="ytp-autonav-toggle-button" and @aria-checked="true"]').click()
        except NoSuchElementException:
            pass

        # Like Video
        try:
            like = chrome.find_element(By.XPATH,
                                       '(//button[@class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start "])[1]')
            if like.get_attribute('aria-pressed') == "false":
                like.click()
        except NoSuchElementException:
            pass

        # Comment
        try:
            chrome.execute_script(f"window.scrollBy(0,400)")
            WebDriverWait(chrome, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="simplebox-placeholder"]')))
            chrome.find_element(By.XPATH, '//*[@id="simplebox-placeholder"]').click()

            for letter in comment:
                chrome.find_element(By.XPATH, '//*[@id="contenteditable-root"]').send_keys(letter)
                sleep(random.randint(0, 75) / 1000)

            try:
                WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Comment"]')))
                chrome.find_element(By.XPATH, '//*[@aria-label="Comment"]').click()
            except TimeoutException:
                WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="تعليق"]')))
                chrome.find_element(By.XPATH, '//*[@aria-label="تعليق"]').click()

            sheet.update_cell(col=3, row=start_from_row, value="Commented Successfully")
            sleep(5)
        except TimeoutException or NoSuchElementException:
            sheet.update_cell(col=3, row=start_from_row, value="No Comment Section")
        except Exception as e:
            print(e)
            sheet.update_cell(col=3, row=start_from_row, value="Couldn't Comment on video")


class UserInterface(QMainWindow, design):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Auto Commenter")
        self.show()

    def transition(self, ui_element):
        self.anim_group = QParallelAnimationGroup()

        for element in ui_element:
            self.element = element
            x = self.element.x()
            y = self.element.y()
            element.move(x - 50, y)

        for element in ui_element:
            effect = QGraphicsOpacityEffect(element)
            self.element = element
            x = self.element.x()
            y = self.element.y()
            self.element.setGraphicsEffect(effect)
            self.anim_1 = QPropertyAnimation(effect, b"opacity")
            self.anim_1.setStartValue(0)
            self.anim_1.setEndValue(1)
            self.anim_1.setDuration(300)
            self.child = element
            self.anim = QPropertyAnimation(self.child, b"pos")
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setEndValue(QPoint(x + 50, y))
            self.anim.setDuration(300)
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim)

        self.anim_group.start()
