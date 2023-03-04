#!/usr/bin/env python3
import sys
import requests
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

from gui.py.setting_window import Ui_Dialog
from gui.py.window import Ui_MainWindow
from gui.py.task_box import Ui_frame

API_key = None
# Forcing setting file back in to the application folder.
# This will make sure that I don't leave any junk files on peoples computers. Since there is no uninstall button.
settings = QtCore.QSettings("setting.ini", QtCore.QSettings.IniFormat)


# Setting window contains setting for the program
# Here you can choose what tasks will be shown and more.
class SettingWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.save)

        # Displayed Tasks setting

        # Sets all checkboxes, needs to be parsed to int because it returns string and bool parser always give true
        for child in self.findChildren(QtWidgets.QCheckBox):  # type: QtWidgets.QCheckBox
            # assert isinstance(child, QtWidgets.QCheckBox)
            child.setChecked(int(settings.value(child.objectName())))

        # Advanced Options
        self.busts_number.setValue(int(settings.value("busts_number")))
        self.addiction_amount.setValue(int(settings.value("addiction_amount")))

    def save(self):  # Saves check box states in to a setting.ini

        for child in self.findChildren(QtWidgets.QCheckBox):  # type: QtWidgets.QCheckBox
            # assert isinstance(child, QtWidgets.QCheckBox)
            settings.setValue(child.objectName(), int(child.isChecked()))

        # Advanced Options
        settings.setValue("busts_number", self.busts_number.value())
        settings.setValue("addiction_amount", self.addiction_amount.value())

        the_button_was_clicked()  # Force Updates the list so the new setting is applied


class TaskBox(QtWidgets.QFrame, Ui_frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(the_button_was_clicked)
        self.actionSetting.triggered.connect(self.open_setting)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(update_tasks)
        self.frame.hide()
        self.error.hide()

    def open_setting(self):
        dialog = SettingWindow(self)
        dialog.open()

    def generate_save_file(self):
        dialog = SettingWindow(self)
        dialog.save()


class Task():
    priority = 0
    ID = 0

    def __init__(self, task_name, priority=0, link="link", image="icons/missing_icon.png", ID=0):
        self.frame = TaskBox(window)

        self.frame.task_name.setText(task_name)
        self.frame.icon.setAutoFillBackground(False)
        self.frame.icon.setGeometry(window.label_4.geometry())
        self.frame.icon.setPixmap(QPixmap(image).scaled(self.frame.icon.size()))

        self.frame.link.setText(link)
        self.frame.link.setOpenExternalLinks(True)

        self.frame.show()
        self.ID = ID
        self.priority = priority

    def __del__(self):
        self.frame.deleteLater()

    def move(self, position):
        self.frame.move(10, 60 + position * self.frame.height())


def the_button_was_clicked():
    global API_key
    API_key = window.textEdit.toPlainText()

    code = get_request("https://api.torn.com/user/?selections=timestamp&key={}".format(API_key))

    if code == 2:  # Checks if the API_key is valid, shows error message if it isn't.
        window.error.show()
        return False

    if settings.value("API_key") != API_key:  # if the keys different and the new key is valid save key to file.
        settings.setValue("API_key", API_key)

    window.timer.start(30500)  # every 30-second update (new data is shown every 30 seconds so no need to update sooner)
    window.error.hide()
    update_tasks()


tasks = list()


def reorder_task():  # first actually working pice of code :D Sorts Task based on priority. Should be call every time new task is added.
    offset = 0
    for i in range(10):
        for task in tasks:
            if task.priority == i:
                task.move(offset)
                offset += 1


def get_request(url):  # Code that waits and retryes request when error occurs (most comonly running out off API calls)
    json_info = requests.get(url).json()

    while True:
        if json_info.get("error") == None:
            break
        elif json_info.get("error").get("code") != "5":
            return json_info.get("error").get("code")

        json_info = requests.get(url).json()
    return json_info


def link(url):
    return "<a href=\"{0}\"><span style=\" text-decoration: underline; color:#0000ff;\">Visit</span></a>".format(url)


# def delete_task(ID):
#     i = 0
#     while i < len(tasks):
#         if tasks[i].ID ==ID:
#             tasks.pop(i)
#             i = 0
#             continue
#         i += 1


def update_tasks():
    tasks.clear()
    print("Updating")

    # This is when asking for logs to only ask for the one that are from current day.
    time = datetime.datetime.utcnow().time()
    timestamp = datetime.datetime.now().timestamp()
    time_from_midnight = time.second + time.minute * 60 + time.hour * 3600
    time_day_start = int(timestamp - time_from_midnight)

    print(time_day_start)

    info = get_request(
        f'https://api.torn.com/user/?selections=cooldowns,profile,refills,networth,bars,icons&key={API_key}')
    count_logs = str(get_request(
        f'https://api.torn.com/user/?selections=log&log=5360,7815,7810,7805,8370,8371,6005&from={time_day_start}&key={API_key}'))
    ## Used log IDs 
    # 5360 - Bust success
    # 7815 - Missions complete
    # 7810 - Missions fail
    # 7805 - Missions decline
    # 8370 - Casino spin the wheel start
    # 8371 - Casino spin the wheel free spin
    # 6005 - Rehab 

    ## Notes 
    ## NPC_shop should be skipped automatically when is completed. 

    # count_newsletter = str(get_request(f'https://api.torn.com/user/?selections=log&log=400,401&key={API_key}'))

    # Drug cooldown task
    drugs = int(info.get("cooldowns").get("drug"))
    if drugs < 60 and int(settings.value("drug")):
        tasks.append(Task("Take a drug!", 1, ID=1, image=("icons/drugs.png")))

        # Medical cooldown task
    medical = int(info.get("cooldowns").get("medical"))
    life = (float(info.get("life").get("current")) / float(info.get("life").get("maximum"))) * 100
    if medical < 14400 and life > 90 and int(
            settings.value("medical")):  # set up that you get task only if you can fill 3 blood packs
        tasks.append(Task("Fill a Blood Bag", 5, ID=1, image=str("icons/medical.png")))

    # Bosster cooldown task
    booster = int(info.get("cooldowns").get("booster"))
    if booster < 28800 and int(settings.value("booster")):
        tasks.append(Task("Go Drink some Beer", 4, ID=1, image="icons/booster.png"))

    # Energy refill task
    refills = info.get("refills")
    if not bool(refills.get("energy_refill_used")) and int(settings.value("energy_refill")):
        tasks.append(Task("Use Your Energy Refill", 4, link=link("https://www.torn.com/points.php"), ID=2,
                          image="icons/e_refill.png"))

    # Nerve refill task
    if not bool(refills.get("nerve_refill_used")) and int(settings.value("nerve_refill")):
        tasks.append(Task("Use Your Nerve Refill", 5, link=link("https://www.torn.com/points.php"), ID=2))

    # Casino refill task
    if not bool(refills.get("token_refill_used")) and int(settings.value("casino_refill")):
        tasks.append(Task("Use Your Casino Tokens Refill", 5, link=link("https://www.torn.com/points.php"), ID=2,
                          image="icons/casino.png"))

    # Energy task
    energy = info.get("energy")
    if int(energy.get("current")) == int(energy.get("maximum")) and int(settings.value("energy")):
        tasks.append(Task("Spend your Energy on something", 2, ID=3, image="icons/energy.png"))

    # Crime task
    nerve = info.get("nerve")
    if int(nerve.get("current")) >= int(nerve.get("maximum")) and int(settings.value("nerve")):
        tasks.append(Task("Go Commit some Crimes", 2, link=link("https://www.torn.com/crimes.php"), ID=3,
                          image="icons/crimes.png"))

    # Unpaidfees task
    unpaidfees = int(info.get("networth").get("unpaidfees"))
    if unpaidfees != 0 and int(settings.value("bills")):
        tasks.append(
            Task("You have -${:,} unpaidfees".format(-1 * unpaidfees), 6, link("https://www.torn.com/loan.php"), ID=5,
                 image="icons/fees.png"))

    # Racing task
    race = info.get("icons").get("icon17")
    if race == None and int(settings.value("race")):
        tasks.append(Task("You should enter a race", 5, link=link("https://www.torn.com/loader.php?sid=racing"), ID=8,
                          image="icons/race.png"))

    # Rehab task
    addiction = info.get("icons").get("icon57")
    if addiction != None and int(settings.value("rehab")):
        addiction = str(addiction)[(addiction.find("(") + 1):addiction.find(")")].strip("-%")
        if int(addiction) >= 3:
            tasks.append(Task("Go to rehab", 6, ID=11, image="icons/rehab.png"))

    # Employee effectiveness
    rehab = count_logs.count("g\': 6005")
    if not rehab and int(settings.value("rehab")):
        company = get_request(f'https://api.torn.com/company/?selections=employees&key={API_key}')
        addiction = company.get("company_employees").get(str(info.get("player_id"))).get("effectiveness").get(
            "addiction")
        if addiction <= int(settings.value("addiction_amount")) * -1 and not rehab:
            tasks.append(Task("Go to rehab your addiction is {}".format(addiction), 6, ID=11))

    # #Use newsletter bonus 
    # newsletters_unused = count_newsletter.count("g\': 400") - count_newsletter.count("g\': 401") 
    # if newsletters_unused > 0 :
    #     tasks.append(Task("You have {} unused newsletter bonuses".format(newsletters_unused),10,ID=15))

    # Daily mission task
    missions = count_logs.count("g\': 7815") + count_logs.count("g\': 7810") + count_logs.count("g\': 7805")
    if missions == 0 and int(settings.value("missions")):
        tasks.append(Task("Complete your daily mission", 9, ID=6, image="icons/mission.png"))

    # Bust people task
    if settings.value("busts_number") != None:  # Just in case value doesn't exists in setting.
        busts = count_logs.count("g\': 5360")
        busts_number = int(settings.value("busts_number"))
        if busts < busts_number and int(settings.value("busts")):
            tasks.append(
                Task("Do {} more busts".format(busts_number - busts), 7, link=link("https://www.torn.com/jailview.php"),
                     ID=7, image="icons/busts.png"))
            pass

    # Wheel of Fortune
    spins = count_logs.count("g\': 8370") - count_logs.count("g\': 8371")
    if spins < 3 and int(settings.value("wheels")):
        tasks.append(Task("You have {} wheels to be spun".format(3 - spins), 8,
                          link=link("https://www.torn.com/loader.php?sid=spinTheWheel"), ID=10,
                          image="icons/wheel.png"))

    # Buy stuff at NPC shop task
    if int(settings.value("npc")):
        NPC_shop = get_request(
            f'https://api.torn.com/user/?selections=log&log=4200&from={time_day_start}&key={API_key}')
        NPC_shop = NPC_shop.get("log")
        brought = 0
        if NPC_shop != None:
            for log in NPC_shop:
                brought += int(NPC_shop.get(log).get("data").get("quantity"))
        if brought < 100 and int(settings.value("npc")):
            tasks.append(Task("Buy {} items at NPC shop".format(100 - brought), 9,
                              link=link("https://www.torn.com/shops.php?step=bitsnbobs"), ID=8,
                              image="icons/bits_bobs.png"))

    if int(settings.value("virus")):
        virus = get_request(f'https://api.torn.com/user/?selections=log&log=5800,5801,5802&key={API_key}')
        virus = virus.get("log")
        if virus[next(iter(virus))].get("log") != 5800:
            tasks.append(Task("Start programming virus", 9, ID=10, image="icons/virus.png"))

    reorder_task()


app = QtWidgets.QApplication(sys.argv)  # not sure what it does
window = MainWindow()  # initializing window.py basically
window.show()

if len(settings.allKeys()) != 19:  # Checks if setting file exists if no forces window to generate new one.
    window.generate_save_file()

if settings.value("API_key") != None:  # inserst key in to field if it exists.
    window.textEdit.setText(settings.value("API_key"))

app.exec()
