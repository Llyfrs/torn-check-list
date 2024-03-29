# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/setting_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(341, 637)
        Dialog.setMinimumSize(QtCore.QSize(181, 409))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 610, 131, 24))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-30, 20, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 500, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 520, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.busts_number = QtWidgets.QSpinBox(Dialog)
        self.busts_number.setGeometry(QtCore.QRect(220, 540, 43, 24))
        self.busts_number.setMinimum(1)
        self.busts_number.setProperty("value", 3)
        self.busts_number.setObjectName("busts_number")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 540, 211, 21))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 40, 321, 451))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drug = QtWidgets.QCheckBox(self.layoutWidget)
        self.drug.setChecked(True)
        self.drug.setObjectName("drug")
        self.verticalLayout.addWidget(self.drug)
        self.medical = QtWidgets.QCheckBox(self.layoutWidget)
        self.medical.setChecked(True)
        self.medical.setObjectName("medical")
        self.verticalLayout.addWidget(self.medical)
        self.booster = QtWidgets.QCheckBox(self.layoutWidget)
        self.booster.setChecked(True)
        self.booster.setObjectName("booster")
        self.verticalLayout.addWidget(self.booster)
        self.energy_refill = QtWidgets.QCheckBox(self.layoutWidget)
        self.energy_refill.setChecked(True)
        self.energy_refill.setObjectName("energy_refill")
        self.verticalLayout.addWidget(self.energy_refill)
        self.nerve_refill = QtWidgets.QCheckBox(self.layoutWidget)
        self.nerve_refill.setChecked(True)
        self.nerve_refill.setObjectName("nerve_refill")
        self.verticalLayout.addWidget(self.nerve_refill)
        self.casino_refill = QtWidgets.QCheckBox(self.layoutWidget)
        self.casino_refill.setChecked(True)
        self.casino_refill.setObjectName("casino_refill")
        self.verticalLayout.addWidget(self.casino_refill)
        self.energy = QtWidgets.QCheckBox(self.layoutWidget)
        self.energy.setChecked(True)
        self.energy.setObjectName("energy")
        self.verticalLayout.addWidget(self.energy)
        self.nerve = QtWidgets.QCheckBox(self.layoutWidget)
        self.nerve.setChecked(True)
        self.nerve.setObjectName("nerve")
        self.verticalLayout.addWidget(self.nerve)
        self.bills = QtWidgets.QCheckBox(self.layoutWidget)
        self.bills.setChecked(True)
        self.bills.setObjectName("bills")
        self.verticalLayout.addWidget(self.bills)
        self.race = QtWidgets.QCheckBox(self.layoutWidget)
        self.race.setChecked(True)
        self.race.setObjectName("race")
        self.verticalLayout.addWidget(self.race)
        self.rehab = QtWidgets.QCheckBox(self.layoutWidget)
        self.rehab.setChecked(True)
        self.rehab.setObjectName("rehab")
        self.verticalLayout.addWidget(self.rehab)
        self.missions = QtWidgets.QCheckBox(self.layoutWidget)
        self.missions.setChecked(True)
        self.missions.setObjectName("missions")
        self.verticalLayout.addWidget(self.missions)
        self.busts = QtWidgets.QCheckBox(self.layoutWidget)
        self.busts.setChecked(True)
        self.busts.setObjectName("busts")
        self.verticalLayout.addWidget(self.busts)
        self.wheels = QtWidgets.QCheckBox(self.layoutWidget)
        self.wheels.setChecked(True)
        self.wheels.setObjectName("wheels")
        self.verticalLayout.addWidget(self.wheels)
        self.npc = QtWidgets.QCheckBox(self.layoutWidget)
        self.npc.setChecked(True)
        self.npc.setObjectName("npc")
        self.verticalLayout.addWidget(self.npc)
        self.virus = QtWidgets.QCheckBox(self.layoutWidget)
        self.virus.setChecked(True)
        self.virus.setObjectName("virus")
        self.verticalLayout.addWidget(self.virus)
        self.addiction_amount = QtWidgets.QSpinBox(Dialog)
        self.addiction_amount.setGeometry(QtCore.QRect(220, 570, 43, 24))
        self.addiction_amount.setMinimum(1)
        self.addiction_amount.setProperty("value", 9)
        self.addiction_amount.setObjectName("addiction_amount")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 570, 211, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Displayed Tasks</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Advanced Options</p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Number of people to bust per day"))
        self.drug.setText(_translate("Dialog", "Task to take any drug when cooldown runs out"))
        self.medical.setText(_translate("Dialog", "Task to use up your medical cooldown"))
        self.booster.setText(_translate("Dialog", "Task to use up your booster cooldown"))
        self.energy_refill.setText(_translate("Dialog", "Task to use your energy refill"))
        self.nerve_refill.setText(_translate("Dialog", "Task to use your nerve refill"))
        self.casino_refill.setText(_translate("Dialog", "Task to use your casino tokens refill"))
        self.energy.setText(_translate("Dialog", "Task to use up your fill energy bar"))
        self.nerve.setText(_translate("Dialog", "Task to use up your full nerve bar"))
        self.bills.setText(_translate("Dialog", "Task to pay your bills "))
        self.race.setText(_translate("Dialog", "Task to join race "))
        self.rehab.setText(_translate("Dialog", "Task to go to rehab "))
        self.missions.setText(_translate("Dialog", "Taks to do your daily mission"))
        self.busts.setText(_translate("Dialog", "Taks to bust people from jail "))
        self.wheels.setText(_translate("Dialog", "Task to spin wheels of fortune"))
        self.npc.setText(_translate("Dialog", "Taks to buy stuff from NPC store "))
        self.virus.setText(_translate("Dialog", "Task to code virus"))
        self.label_4.setText(_translate("Dialog", "Amount of addiction to rehab"))
