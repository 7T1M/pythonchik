# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 40, 60, 16))
        self.label.setObjectName("label")
        self.input_str = QtWidgets.QTextEdit(self.centralwidget)
        self.input_str.setGeometry(QtCore.QRect(70, 40, 281, 20))
        self.input_str.setObjectName("input_str")
        self.word_len_check = QtWidgets.QCheckBox(self.centralwidget)
        self.word_len_check.setGeometry(QtCore.QRect(80, 100, 241, 20))
        self.word_len_check.setObjectName("word_len_check")
        self.replace_num_check = QtWidgets.QCheckBox(self.centralwidget)
        self.replace_num_check.setGeometry(QtCore.QRect(80, 130, 291, 20))
        self.replace_num_check.setObjectName("replace_num_check")
        self.space_between_check = QtWidgets.QCheckBox(self.centralwidget)
        self.space_between_check.setGeometry(QtCore.QRect(80, 160, 281, 20))
        self.space_between_check.setObjectName("space_between_check")
        self.sort_check = QtWidgets.QCheckBox(self.centralwidget)
        self.sort_check.setGeometry(QtCore.QRect(80, 190, 341, 20))
        self.sort_check.setObjectName("sort_check")
        self.sort_for_len_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.sort_for_len_btn.setGeometry(QtCore.QRect(100, 220, 100, 20))
        self.sort_for_len_btn.setObjectName("sort_for_len_btn")
        self.sort_for_lexic_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.sort_for_lexic_btn.setGeometry(QtCore.QRect(100, 250, 191, 20))
        self.sort_for_lexic_btn.setObjectName("sort_for_lexic_btn")
        self.format_btn = QtWidgets.QPushButton(self.centralwidget)
        self.format_btn.setGeometry(QtCore.QRect(60, 330, 491, 51))
        self.format_btn.setObjectName("format_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(10, 420, 81, 16))
        self.label_2.setObjectName("label_2")
        self.result_str = QtWidgets.QTextEdit(self.centralwidget)
        self.result_str.setGeometry(QtCore.QRect(100, 420, 281, 20))
        self.result_str.setObjectName("result_str")
        self.word_len_box = QtWidgets.QSpinBox(self.centralwidget)
        self.word_len_box.setGeometry(QtCore.QRect(320, 100, 71, 24))
        self.word_len_box.setObjectName("word_len_box")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 100, 60, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "String Formatter Demo"))
        self.label.setText(_translate("MainWindow", "Строка:"))
        self.word_len_check.setText(_translate(
            "MainWindow", "Удалить слова размером  меньше:"))
        self.replace_num_check.setText(_translate(
            "MainWindow", "Заменить все цифры на *"))
        self.space_between_check.setText(_translate(
            "MainWindow", "Вставить по пробелу между символами"))
        self.sort_check.setText(_translate(
            "MainWindow", "Сортировать слова в строке"))
        self.sort_for_len_btn.setText(_translate("MainWindow", "По размеру"))
        self.sort_for_lexic_btn.setText(
            _translate("MainWindow", "Лексикографически"))
        self.format_btn.setText(_translate("MainWindow", "Форматировать"))
        self.label_2.setText(_translate("MainWindow", "Результат:"))
        self.label_3.setText(_translate("MainWindow", "букв"))
