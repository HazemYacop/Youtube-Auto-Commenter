import os
import Creds
import random
import threading
from time import sleep
from PySide2.QtWidgets import QApplication
from Functions import Package, UserInterface


class Main:
    def __init__(self):
        super().__init__()

        # Start-Up
        self.program_path = f'{os.path.expanduser("~")}\AppData\Local\Youtube Auto Commenter'

        # Creating 4 Json files to proceed with (So there won't be overload on a specific spreadsheet api)
        Package.create_json(Creds.json_content_1, "Creds1")
        Package.create_json(Creds.json_content_2, "Creds2")
        Package.create_json(Creds.json_content_3, "Creds3")
        Package.create_json(Creds.json_content_4, "Creds4")

        # Re-translating UI
        self.UserInterface = UserInterface()
        self.UserInterface.stackedWidget.setCurrentIndex(0)

        # Load Information
        Package.load_txt(self.UserInterface.Sheet, "Sheet")
        Package.load_txt(self.UserInterface.Worksheet, "Worksheet")
        Package.load_txt(self.UserInterface.StartFromRow, "StartFromRow")
        Package.load_txt(self.UserInterface.ChromeProfile, "ChromeProfile")

        # Button(s) Fun(s)
        self.UserInterface.StartButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(3), self.UserInterface.transition([self.UserInterface.stackedWidget]), self.required_data(), threading.Thread(target=self.main).start(), self.UserInterface.BackButton.setDisabled(True)])
        self.UserInterface.NextToChromeProfilesPageButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(1), self.UserInterface.transition([self.UserInterface.stackedWidget])])
        self.UserInterface.BackToMainPageButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(0), self.UserInterface.transition([self.UserInterface.stackedWidget])])
        self.UserInterface.NextToSharePageButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(2), self.UserInterface.transition([self.UserInterface.stackedWidget]), self.UserInterface.EmailCopiedSuccessfullyLabel.setText("")])
        self.UserInterface.OpenChromeProfileButton.clicked.connect(lambda: Package.control_chrome(self.UserInterface.ChromeProfile.text()))
        self.UserInterface.CopyEmailButton.clicked.connect(lambda: [Package.copy_email(self.program_path), self.UserInterface.EmailCopiedSuccessfullyLabel.setText("Email Copied Successfully")])
        self.UserInterface.BackToMesaagePageButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(1), self.UserInterface.transition([self.UserInterface.stackedWidget])])

    def main(self):
        try:
            # Save Information
            Package.save_txt("Sheet", self.sheet)
            Package.save_txt("Worksheet", self.worksheet)
            Package.save_txt("StartFromRow", self.start_from_row)
            Package.save_txt("ChromeProfile", self.chrome_profile)

            # Re-translating UI
            self.UserInterface.SheetStatusLabel.setText(f"Sheet : {self.sheet}")
            self.UserInterface.WorksheetStatusLabel.setText(f"Worksheet : {self.worksheet}")
            self.UserInterface.StartFromRowStatusLabel.setText(f"Start From Row : {self.start_from_row}")
            videos_done = 0
            self.UserInterface.VideosFinishedStatusLabel.setText(f"Videos Finished : {videos_done}")

            # Chrome open Function
            chrome = Package.control_chrome(self.chrome_profile)

            # Defining videos list
            videos = self.videos[self.start_from_row - 1:]

            for video in videos:
                comment = self.comments[random.randint(0, len(self.comments) - 1)]
                chrome.get(video)
                sleep(5)
                Package.comment(chrome, comment, self.sheet_control, self.start_from_row)

                # Adding 1 to Variables
                videos_done += 1
                self.start_from_row += 1

                # Re-translating UI
                self.UserInterface.VideosFinishedStatusLabel.setText(f"Videos Finished : {videos_done}")

            self.UserInterface.BackButton.setDisabled(False)

        except Exception as e:
            print(e)
            # Re-translating UI
            self.UserInterface.WorkingLabel.setText("Error Occurred, Take a screenshot of the CMD (Black Screen) and Contact : +201150169348")
            self.UserInterface.SheetStatusLabel.setText("")
            self.UserInterface.WorksheetStatusLabel.setText("")
            self.UserInterface.StartFromRowStatusLabel.setText("")
            self.UserInterface.BackButton.setDisabled(False)



    def required_data(self):
        self.sheet = self.UserInterface.Sheet.text()
        self.worksheet = self.UserInterface.Worksheet.text()
        self.start_from_row = int(self.UserInterface.StartFromRow.text())
        self.chrome_profile = self.UserInterface.ChromeProfile.text()

        with open(f'{self.program_path}\Email.txt', 'r+', encoding="utf-8") as file:
            if file.read() == "Email1":
                file.close()
                self.sheet_control = Package.access_google_spreadsheet(self.sheet, self.worksheet, "Creds1")

            elif file.read() == "Email2":
                file.close()
                self.sheet_control = Package.access_google_spreadsheet(self.sheet, self.worksheet, "Creds2")

            elif file.read() == "Email3":
                file.close()
                self.sheet_control = Package.access_google_spreadsheet(self.sheet, self.worksheet, "Creds3")
            else:
                file.close()
                self.sheet_control = Package.access_google_spreadsheet(self.sheet, self.worksheet, "Creds4")

        self.videos = self.sheet_control.col_values(1)
        self.comments = list(filter(lambda x: x != "", self.sheet_control.col_values(2)))


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
