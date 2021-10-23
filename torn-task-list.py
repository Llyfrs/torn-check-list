#!/usr/bin/env python
import sys
import random
import requests
import time
import datetime
import os
import json
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap

from setting_window import Ui_Dialog
from window import Ui_MainWindow

API_key = None
#Forcing setting file back in to the application folder.
#This will make sure that I don't leave any junk files over peoples computers. Since there is no unistall button. 
settings = QtCore.QSettings("setting.ini",QtCore.QSettings.IniFormat) 


#Setting window contains setting for the program
#Here you can chose what tasks will be shown and more. 
class SettingWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.save)

        #Quick fix so None variables don't load, not yet sure how to implement better. 
        #This leads to a bug where when you delete one line from your settin it will reset it.
        #Hope user wont really do that but I would still like it to be working better. 
        if len(settings.allKeys()) == 15: 
            #Displayed Tasks setting 
            self.bills.setChecked(bool(settings.value("bills")))
            self.booster.setChecked(bool(settings.value("booster")))
            self.busts.setChecked(bool(settings.value("busts")))
            self.drug.setChecked(bool(settings.value("drug")))
            self.energy.setChecked(bool(settings.value("energy")))
            self.energy_refill.setChecked(bool(settings.value("energy_refill")))
            self.medical.setChecked(bool(settings.value("medical")))
            self.missions.setChecked(bool(settings.value("missions")))
            self.nerve.setChecked(bool(settings.value("nerve")))
            self.npc.setChecked(bool(settings.value("npc")))
            self.race.setChecked(bool(settings.value("race")))
            self.rehab.setChecked(bool(settings.value("rehab")))
            self.wheels.setChecked(bool(settings.value("wheels")))
            
            #Advanced Options

            self.busts_number.setValue(int(settings.value("busts_number")))
        
        

    def save(self): #Saves check box states in to a setting.ini 
        #Displayed Tasks setting 
        settings.setValue("bills", int(self.bills.isChecked()))
        settings.setValue("booster", int(self.booster.isChecked()))
        settings.setValue("busts", int(self.busts.isChecked()))
        settings.setValue("drug", int(self.drug.isChecked()))
        settings.setValue("energy", int(self.energy.isChecked()))
        settings.setValue("energy_refill", int(self.energy_refill.isChecked()))
        settings.setValue("medical", int(self.medical.isChecked()))
        settings.setValue("missions", int(self.missions.isChecked()))
        settings.setValue("nerve", int(self.nerve.isChecked()))
        settings.setValue("npc", int(self.npc.isChecked()))
        settings.setValue("race", int(self.race.isChecked()))
        settings.setValue("rehab", int(self.rehab.isChecked()))
        settings.setValue("wheels", int(self.wheels.isChecked()))
        #Advanced Options
        settings.setValue("busts_number", self.busts_number.value())
        

        update_tasks()
        


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        

        self.pushButton.clicked.connect(the_button_was_clicked)
        self.actionSetting.triggered.connect(self.open_setting)
        self.timer= QtCore.QTimer()
        self.timer.timeout.connect(update_tasks)
        self.frame.hide()
        self.error.hide()

    def open_setting(self):
        self.dialog = SettingWindow(self)
        self.dialog.open()


class Task():
    
    priority = 0
    ID = 0

    def __init__(self, task_name,priority = 0, link="link", image="icons/missing_icon.png", ID=0):
        self.newframe = QtWidgets.QFrame(window.centralwidget)
        self.newframe.setGeometry(window.frame.geometry())
        self.newframe.setPalette(window.frame.palette())
        self.newframe.setFrameShape(QtWidgets.QFrame.Box)
        self.newframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newframe.setAutoFillBackground(True)
        self.task_name = QtWidgets.QLabel(self.newframe)
        self.task_name.setGeometry(window.label_3.geometry())
        self.task_name.setText(task_name)
        self.icon = QtWidgets.QLabel(self.newframe)
        self.icon.setGeometry(window.label_4.geometry())
        self.icon.setPixmap(QPixmap(image).scaled(self.icon.size()))
        self.link = QtWidgets.QLabel(self.newframe)
        self.link.setGeometry(window.label_5.geometry())
        self.link.setText(link)
        self.link.setOpenExternalLinks(True)
        self.newframe.show()
        self.ID = ID
        self.priority = priority
    
    def __del__(self):
        self.newframe.deleteLater()
    
    def move(self,position):
        self.newframe.move(self.newframe.x(),window.frame.y()+position*window.frame.height())
        
def the_button_was_clicked(): 
    global API_key 
    API_key = window.textEdit.toPlainText()

    code = get_request("https://api.torn.com/user/?selections=timestamp&key={}".format(API_key))

    if code == 2: # Checks if the API_key is valid, shows error message if it isn't. 
        window.error.show()
        return False

    if settings.value("API_key") != API_key: # if the keys different and the new key is valid save key to file. 
        settings.setValue("API_key", API_key)


    window.timer.start(30500) #every 30 second update (new data is shown every 30 seconds so no need to update sooner)
    window.error.hide()
    update_tasks()


tasks = list()


def reorder_task(): # first actually working pice of code :D Sorts Task based on priority. Should be call every time new task is added. 
    offset = 0
    for i in range(10):
        for task in tasks:
            if task.priority == i:
                task.move(offset)
                offset += 1

def get_request(url): #Code that waits and retryes request when error occurs (most comonly running out off AP calls) 
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


    #This is when asking for logs to only ask for the one that are from current day. 
    time = datetime.datetime.utcnow().time()
    timestamp = datetime.datetime.now().timestamp()
    time_from_midnight = time.second + time.minute * 60 + time.hour * 3600
    time_day_start = int(timestamp - time_from_midnight)


    info = get_request(f'https://api.torn.com/user/?selections=cooldowns,profile,refills,networth,bars,icons&key={API_key}')
    count_logs = str(get_request(f'https://api.torn.com/user/?selections=log&log=4200,5360,7815,7810,7805,8370&from={time_day_start}&key={API_key}'))
    NPC_shop = get_request(f'https://api.torn.com/user/?selections=log&log=4200&from={time_day_start}&key={API_key}')


    #Drug cooldown task
    if int(info.get("cooldowns").get("drug")) < 60 and bool(settings.value("drug")):
        tasks.append(Task("Take a drug!",1,ID=1,image=("icons/drugs.png"))) 

    #Medical cooldown task
    medical = int(info.get("cooldowns").get("medical"))
    life = (float(info.get("life").get("current"))/float(info.get("life").get("maximum")))*100
    if medical < 14400 and life > 90 and bool(settings.value("medical")): #set up that you get task only if you can fill 3 blood packs
        tasks.append(Task("Fill a Blood Bag",5,ID=1,image=str("icons/medical.png")))

    #Bosster cooldown task
    booster = int(info.get("cooldowns").get("booster"))
    if booster < 28800 and bool(settings.value("booster")):
        tasks.append(Task("Go Drink some Beer",4,ID=1,image="icons/booster.png"))
    
    #Energy refill task
    refills = info.get("refills")
    if not bool(refills.get("energy_refill_used")) and bool(settings.value("energy_refill")):
        tasks.append(Task("Use Your Energy Refill",4,link=link("https://www.torn.com/crimes.php"),ID=2,image="icons/e_refill.png"))

    #Energy task
    energy = info.get("energy")
    if int(energy.get("current"))==int(energy.get("maximum")) and bool(settings.value("energy")):
        tasks.append(Task("Spend your Energy on something",2,ID=3,image="icons/energy.png"))

    #Crime task
    nerve = info.get("nerve")
    if int(nerve.get("current")) >= int(nerve.get("maximum")) and bool(settings.value("nerve")):
        tasks.append(Task("Go Commit some Crimes",2,link=link("https://www.torn.com/crimes.php"),ID=3,image="icons/crimes.png"))

    #Unpaidfees task
    unpaidfees = int(info.get("networth").get("unpaidfees"))
    if unpaidfees != 0 and bool(settings.value("bills")):
        tasks.append(Task("You have -${:,} unpaidfees".format(-1*unpaidfees),6,link("https://www.torn.com/loan.php"),ID=5,image="icons/fees.png"))

    #Racing task 
    race = info.get("icons").get("icon17")
    if race == None and bool(settings.value("race")):
        tasks.append(Task("You should enter race",5,link=link("https://www.torn.com/loader.php?sid=racing"),ID=8,image="icons/race.png"))

    #Rehab task
    addiction = info.get("icons").get("icon57")
    if addiction != None and bool(settings.value("rehab")):
        addiction = str(addiction)[(addiction.find("(")+1):addiction.find(")")].strip("-%")
        if int(addiction) >= 3:
            tasks.append(Task("Go to rehab",6,ID=11))


    #Daily mission task
    missions = count_logs.count("g\': 7815") + count_logs.count("g\': 7810") + count_logs.count("g\': 7805")
    if missions == 0 and bool(settings.value("missions")):
        tasks.append(Task("Complete your daily mission",9,ID=6,image="icons/mission.png"))
    
    #Bust people task
    busts = count_logs.count("g\': 5360") 
    busts_number = int(settings.value("busts_number"))
    if   busts < busts_number  and bool(settings.value("busts")):
        tasks.append(Task("Do {} more busts".format(busts_number-busts),7,link=link("https://www.torn.com/jailview.php"),ID=7,image="icons/busts.png"))
        pass
    
    
    #Wheel of Fortune
    spins = count_logs.count("g\': 8370")
    if spins != 3 and bool(settings.value("wheels")):
        tasks.append(Task("You have {} wheels to be spun".format(3-spins),8,link=link("https://www.torn.com/loader.php?sid=spinTheWheel"),ID=10,image="icons/wheel.png"))

    #Buy stuff at NPC shop task
    NPC_shop = NPC_shop.get("log")
    brought = 0
    if NPC_shop != None:
        for log in NPC_shop:
            brought += int(NPC_shop.get(log).get("data").get("quantity"))
    if brought < 100 and bool(settings.value("npc")):
        tasks.append(Task("Buy {} items at NPC shop".format(100-brought),9,link=link("https://www.torn.com/shops.php?step=bitsnbobs"),ID=8,image="icons/bits_bobs.png"))


    reorder_task()
    


app = QtWidgets.QApplication(sys.argv) # not sure what it does 
window = MainWindow() #initializing window.py basically 
window.show() 


if settings.value("API_key") != None : # inserst key in to field if it exists. 
    window.textEdit.setText(settings.value("API_key"))


app.exec()





