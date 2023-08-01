import sys
from _datetime import datetime
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QDesktopWidget, QLCDNumber
from PyQt5.QtWidgets import (QWidget)

eventx = []
eventy = []
vsevstrl = []
data = str(datetime.now().date())


class Line:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
    def draw(self, painter):
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)

class BrushPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, painter):
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.paint_or_no = False
        self.paint_or_noo = False
        self.paint_or_no1 = False
        self.initUI()
        self.x = 0
        self.y = 0
        self.n = 1
        self.right = False
        self.z = False
        self.setMouseTracking(True)
        self.objects = []

    def initUI(self):
        self.app = QApplication(sys.argv)
        self.q = QDesktopWidget().availableGeometry()
        self.w = self.q.width()
        self.h = self.q.height() - 30
        self.setGeometry(0, 0, self.w, self.h)
        self.setWindowTitle('SKATT тренажер')

        self.name_label = QLabel(self)
        self.name_label.setText('СТРЕЛКОВЫЙ ТРЕНАЖЕР "SKATT"')
        self.name_label.move(850, 310)
        self.name_label.resize(200, 30)

        self.name_input = QLineEdit(self)
        self.name_input.move(960, 380)
        self.name_input.resize(200, 30)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Введите количество выстрелов:")
        self.name_label1.move(730, 380)
        self.name_label1.resize(200, 30)

        self.btn = QPushButton('Пневматическая винтовка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.setStyleSheet('QPushButton {background-color: rgb(173, 102, 213); color: white;}')
        self.btn.move(740, 520)
        self.btn.resize(160, 50)
        self.btn.clicked.connect(self.startVint)

        self.btn1 = QPushButton('Пневматический пистолет', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.setStyleSheet('QPushButton {background-color: rgb(56, 178, 206); color: white;}')
        self.btn1.move(970, 520)
        self.btn1.resize(160, 50)
        self.btn1.clicked.connect(self.startPist)

        self.btn_s = QPushButton(self)
        self.btn_s.resize(self.btn_s.sizeHint())
        self.btn_s.setText('Винтовка. Показать результаты всех тренировок')
        self.btn_s.setStyleSheet('QPushButton {background-color: rgb(173, 102, 213); color: white;}')
        self.btn_s.move(1170, 720)
        self.btn_s.resize(300, 150)
        self.btn_s.hide()
        self.btn_s.clicked.connect(self.rez_v)

        self.btn_s1 = QPushButton(self)
        self.btn_s1.resize(self.btn_s.sizeHint())
        self.btn_s1.setText('Пистолет. Показать результаты всех тренировок')
        self.btn_s1.setStyleSheet('QPushButton {background-color: rgb(56, 178, 206); color: white;}')
        self.btn_s1.move(1520, 720)
        self.btn_s1.resize(300, 150)
        self.btn_s1.hide()
        self.btn_s1.clicked.connect(self.rez_p)

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.resize(200, 30)
        self.coords.move(100, 30)
        self.coords.hide()

        self.date = QLabel(self)
        self.date.setText(data)
        self.date.resize(200, 30)
        self.date.move(580, 70)
        self.date.hide()

        self.name_label51 = QLabel(self)
        self.name_label51.setText('1')
        self.name_label51.move(616, 126)
        self.name_label51.resize(30, 30)
        self.name_label51.hide()

        self.name_label52 = QLabel(self)
        self.name_label52.setText('2')
        self.name_label52.move(616, 166)
        self.name_label52.resize(30, 30)
        self.name_label52.hide()

        self.name_label53 = QLabel(self)
        self.name_label53.setText('3')
        self.name_label53.move(616, 206)
        self.name_label53.resize(30, 30)
        self.name_label53.hide()

        self.name_label54 = QLabel(self)
        self.name_label54.setText('4')
        self.name_label54.move(616, 246)
        self.name_label54.resize(30, 30)
        self.name_label54.hide()

        self.name_label55 = QLabel(self)
        self.name_label55.setText('5')
        self.name_label55.move(616, 286)
        self.name_label55.resize(30, 30)
        self.name_label55.hide()

        self.name_label56 = QLabel(self)
        self.name_label56.setText('6')
        self.name_label56.move(616, 326)
        self.name_label56.resize(30, 30)
        self.name_label56.hide()

        self.name_label57 = QLabel(self)
        self.name_label57.setText('7')
        self.name_label57.move(616, 366)
        self.name_label57.resize(30, 30)
        self.name_label57.hide()

        self.name_label58 = QLabel(self)
        self.name_label58.setText('8')
        self.name_label58.move(616, 406)
        self.name_label58.resize(30, 30)
        self.name_label58.hide()

        self.name_label59 = QLabel(self)
        self.name_label59.setText('9')
        self.name_label59.move(616, 446)
        self.name_label59.resize(30, 30)
        self.name_label59.hide()

        self.name_label50 = QLabel(self)
        self.name_label50.setText('10')
        self.name_label50.move(614, 486)
        self.name_label50.resize(30, 30)
        self.name_label50.hide()

        self.name_label550 = QLabel(self)
        self.name_label550.setText('10')
        self.name_label550.move(601, 486)
        self.name_label550.resize(30, 30)
        self.name_label550.hide()

        self.name_label560 = QLabel(self)
        self.name_label560.setText('10')
        self.name_label560.move(626, 486)
        self.name_label560.resize(30, 30)
        self.name_label560.hide()

        self.name_label570 = QLabel(self)
        self.name_label570.setText('10')
        self.name_label570.move(613, 498)
        self.name_label570.resize(30, 30)
        self.name_label570.hide()

        self.name_label580 = QLabel(self)
        self.name_label580.setText('10')
        self.name_label580.move(613, 472)
        self.name_label580.resize(30, 30)
        self.name_label580.hide()

        self.name_label61 = QLabel(self)
        self.name_label61.setText('1')
        self.name_label61.move(616, 846)
        self.name_label61.resize(30, 30)
        self.name_label61.hide()

        self.name_label62 = QLabel(self)
        self.name_label62.setText('2')
        self.name_label62.move(616, 806)
        self.name_label62.resize(30, 30)
        self.name_label62.hide()

        self.name_label63 = QLabel(self)
        self.name_label63.setText('3')
        self.name_label63.move(616, 766)
        self.name_label63.resize(30, 30)
        self.name_label63.hide()

        self.name_label64 = QLabel(self)
        self.name_label64.setText('4')
        self.name_label64.move(616, 726)
        self.name_label64.resize(30, 30)
        self.name_label64.hide()

        self.name_label65 = QLabel(self)
        self.name_label65.setText('5')
        self.name_label65.move(616, 686)
        self.name_label65.resize(30, 30)
        self.name_label65.hide()

        self.name_label66 = QLabel(self)
        self.name_label66.setText('6')
        self.name_label66.move(616, 646)
        self.name_label66.resize(30, 30)
        self.name_label66.hide()

        self.name_label67 = QLabel(self)
        self.name_label67.setText('7')
        self.name_label67.move(616, 606)
        self.name_label67.resize(30, 30)
        self.name_label67.hide()

        self.name_label68 = QLabel(self)
        self.name_label68.setText('8')
        self.name_label68.move(616, 566)
        self.name_label68.resize(30, 30)
        self.name_label68.hide()

        self.name_label69 = QLabel(self)
        self.name_label69.setText('9')
        self.name_label69.move(616, 526)
        self.name_label69.resize(30, 30)
        self.name_label69.hide()

        self.name_label71 = QLabel(self)
        self.name_label71.setText('1')
        self.name_label71.move(256, 486)
        self.name_label71.resize(30, 30)
        self.name_label71.hide()

        self.name_label72 = QLabel(self)
        self.name_label72.setText('2')
        self.name_label72.move(296, 486)
        self.name_label72.resize(30, 30)
        self.name_label72.hide()

        self.name_label73 = QLabel(self)
        self.name_label73.setText('3')
        self.name_label73.move(336, 486)
        self.name_label73.resize(30, 30)
        self.name_label73.hide()

        self.name_label74 = QLabel(self)
        self.name_label74.setText('4')
        self.name_label74.move(376, 486)
        self.name_label74.resize(30, 30)
        self.name_label74.hide()

        self.name_label75 = QLabel(self)
        self.name_label75.setText('5')
        self.name_label75.move(416, 486)
        self.name_label75.resize(30, 30)
        self.name_label75.hide()

        self.name_label76 = QLabel(self)
        self.name_label76.setText('6')
        self.name_label76.move(456, 486)
        self.name_label76.resize(30, 30)
        self.name_label76.hide()

        self.name_label77 = QLabel(self)
        self.name_label77.setText('7')
        self.name_label77.move(496, 486)
        self.name_label77.resize(30, 30)
        self.name_label77.hide()

        self.name_label78 = QLabel(self)
        self.name_label78.setText('8')
        self.name_label78.move(536, 486)
        self.name_label78.resize(30, 30)
        self.name_label78.hide()

        self.name_label79 = QLabel(self)
        self.name_label79.setText('9')
        self.name_label79.move(576, 486)
        self.name_label79.resize(30, 30)
        self.name_label79.hide()

        self.name_label81 = QLabel(self)
        self.name_label81.setText('1')
        self.name_label81.move(976, 486)
        self.name_label81.resize(30, 30)
        self.name_label81.hide()

        self.name_label82 = QLabel(self)
        self.name_label82.setText('2')
        self.name_label82.move(936, 486)
        self.name_label82.resize(30, 30)
        self.name_label82.hide()

        self.name_label83 = QLabel(self)
        self.name_label83.setText('3')
        self.name_label83.move(896, 486)
        self.name_label83.resize(30, 30)
        self.name_label83.hide()

        self.name_label84 = QLabel(self)
        self.name_label84.setText('4')
        self.name_label84.move(856, 486)
        self.name_label84.resize(30, 30)
        self.name_label84.hide()

        self.name_label85 = QLabel(self)
        self.name_label85.setText('5')
        self.name_label85.move(816, 486)
        self.name_label85.resize(30, 30)
        self.name_label85.hide()

        self.name_label86 = QLabel(self)
        self.name_label86.setText('6')
        self.name_label86.move(776, 486)
        self.name_label86.resize(30, 30)
        self.name_label86.hide()

        self.name_label87 = QLabel(self)
        self.name_label87.setText('7')
        self.name_label87.move(736, 486)
        self.name_label87.resize(30, 30)
        self.name_label87.hide()

        self.name_label88 = QLabel(self)
        self.name_label88.setText('8')
        self.name_label88.move(696, 486)
        self.name_label88.resize(30, 30)
        self.name_label88.hide()

        self.name_label89 = QLabel(self)
        self.name_label89.setText('9')
        self.name_label89.move(656, 486)
        self.name_label89.resize(30, 30)
        self.name_label89.hide()

        self.name_label100 = QLabel(self)
        self.name_label100.setText('Результат выстрела:')
        self.name_label100.move(1250, 130)
        self.name_label100.resize(300, 30)
        self.name_label100.hide()

        self.name_output = QLCDNumber(self)
        self.name_output.setEnabled(False)
        self.name_output.move(1250, 205)
        self.name_output.resize(150, 130)
        self.name_output.hide()

        self.btn5 = QPushButton('Конец тренировки', self)
        self.btn5.resize(self.btn.sizeHint())
        self.btn5.setStyleSheet('QPushButton {background-color: rgb(97, 216, 159); color: white;}')
        self.btn5.move(1250, 620)
        self.btn5.resize(300, 250)
        self.btn5.clicked.connect(self.finish)
        self.btn5.hide()

        self.btn6 = QPushButton('Конец тренировки', self)
        self.btn6.resize(self.btn.sizeHint())
        self.btn6.setStyleSheet('QPushButton {background-color: rgb(97, 216, 159); color: white;}')
        self.btn6.move(1250, 620)
        self.btn6.resize(300, 250)
        self.btn6.clicked.connect(self.finish1)
        self.btn6.hide()

        self.itog = QLabel(self)
        self.itog.setText('Итог тренировки:')
        self.itog.move(1350, 210)
        self.itog.resize(300, 30)
        self.itog.hide()

        self.itog1 = QLabel(self)
        self.itog1.setText('Количество выстрелов:')
        self.itog1.move(1250, 310)
        self.itog1.resize(300, 30)
        self.itog1.hide()

        self.num = QLCDNumber(self)
        self.num.setEnabled(False)
        self.num.move(1450, 305)
        self.num.resize(100, 50)
        self.num.hide()

        self.itog2 = QLabel(self)
        self.itog2.setText('Среднее значение выстрелов:')
        self.itog2.move(1250, 510)
        self.itog2.resize(300, 30)
        self.itog2.hide()

        self.num1 = QLCDNumber(self)
        self.num1.setEnabled(False)
        self.num1.move(1450, 505)
        self.num1.resize(100, 50)
        self.num1.hide()

        self.itog3 = QLabel(self)
        self.itog3.setText('Количество очков:')
        self.itog3.move(1250, 410)
        self.itog3.resize(300, 30)
        self.itog3.hide()

        self.num2 = QLCDNumber(self)
        self.num2.setEnabled(False)
        self.num2.move(1450, 405)
        self.num2.resize(100, 50)
        self.num2.hide()

        self.itog4 = QLabel(self)
        self.itog4.setText('Выстрел №:')
        self.itog4.move(1610, 130)
        self.itog4.resize(300, 30)
        self.itog4.hide()

        self.num3 = QLCDNumber(self)
        self.num3.setEnabled(False)
        self.num3.move(1600, 205)
        self.num3.resize(100, 50)
        self.num3.hide()

        self.predyp = QLabel(self)
        self.predyp.setText('Вы выполнили запланированную тренировку.')
        self.predyp.setStyleSheet('QLabel {background-color: red; color: white;}')
        self.predyp.move(1250, 450)
        self.predyp.resize(275, 30)
        self.predyp.hide()

        self.predyp1 = QLabel(self)
        self.predyp1.setText('*нажмите "Z" для обновления траектории.')
        self.predyp1.move(500, 50)
        self.predyp1.resize(300, 30)
        self.predyp1.hide()

    def startVint(self):
        self.name_output.show()
        self.predyp1.show()
        self.itog4.show()
        self.num3.show()
        self.btn.hide()
        self.btn1.hide()
        self.btn5.show()
        self.name_input.hide()
        self.name_label.hide()
        self.name_label1.hide()
        self.name_label100.show()
        self.paint_or_no = True
        self.coords.setVisible(True)
        self.name_label50.setVisible(True)
        self.name_label51.setVisible(True)
        self.name_label52.setVisible(True)
        self.name_label53.setVisible(True)
        self.name_label54.setVisible(True)
        self.name_label55.setVisible(True)
        self.name_label56.setVisible(True)
        self.name_label57.setVisible(True)
        self.name_label58.setVisible(True)
        self.name_label59.setVisible(True)
        self.name_label61.setVisible(True)
        self.name_label62.setVisible(True)
        self.name_label63.setVisible(True)
        self.name_label64.setVisible(True)
        self.name_label65.setVisible(True)
        self.name_label66.setVisible(True)
        self.name_label67.setVisible(True)
        self.name_label68.setVisible(True)
        self.name_label69.setVisible(True)
        self.name_label71.setVisible(True)
        self.name_label72.setVisible(True)
        self.name_label73.setVisible(True)
        self.name_label74.setVisible(True)
        self.name_label75.setVisible(True)
        self.name_label76.setVisible(True)
        self.name_label77.setVisible(True)
        self.name_label78.setVisible(True)
        self.name_label79.setVisible(True)
        self.name_label81.setVisible(True)
        self.name_label82.setVisible(True)
        self.name_label83.setVisible(True)
        self.name_label84.setVisible(True)
        self.name_label85.setVisible(True)
        self.name_label86.setVisible(True)
        self.name_label87.setVisible(True)
        self.name_label88.setVisible(True)
        self.name_label89.setVisible(True)
        self.update()

    def startPist(self):
        vistrel = self.name_input.text()
        self.btn.hide()
        self.predyp1.show()
        self.itog4.show()
        self.num3.show()
        self.btn1.hide()
        self.name_output.show()
        self.btn6.show()
        self.name_label100.show()
        self.name_input.hide()
        self.name_label.hide()
        self.name_label1.hide()
        self.paint_or_noo = True
        self.coords.setVisible(True)
        self.name_label550.setVisible(True)
        self.name_label560.setVisible(True)
        self.name_label570.setVisible(True)
        self.name_label580.setVisible(True)
        self.name_label51.setVisible(True)
        self.name_label52.setVisible(True)
        self.name_label53.setVisible(True)
        self.name_label54.setVisible(True)
        self.name_label55.setVisible(True)
        self.name_label56.setVisible(True)
        self.name_label57.setVisible(True)
        self.name_label58.setVisible(True)
        self.name_label59.setVisible(True)
        self.name_label61.setVisible(True)
        self.name_label62.setVisible(True)
        self.name_label63.setVisible(True)
        self.name_label64.setVisible(True)
        self.name_label65.setVisible(True)
        self.name_label66.setVisible(True)
        self.name_label67.setVisible(True)
        self.name_label68.setVisible(True)
        self.name_label69.setVisible(True)
        self.name_label71.setVisible(True)
        self.name_label72.setVisible(True)
        self.name_label73.setVisible(True)
        self.name_label74.setVisible(True)
        self.name_label75.setVisible(True)
        self.name_label76.setVisible(True)
        self.name_label77.setVisible(True)
        self.name_label78.setVisible(True)
        self.name_label79.setVisible(True)
        self.name_label81.setVisible(True)
        self.name_label82.setVisible(True)
        self.name_label83.setVisible(True)
        self.name_label84.setVisible(True)
        self.name_label85.setVisible(True)
        self.name_label86.setVisible(True)
        self.name_label87.setVisible(True)
        self.name_label88.setVisible(True)
        self.name_label89.setVisible(True)
        self.update()

    def mouseMoveEvent(self, event):
        self.objects.append(BrushPoint(event.x(), event.y()))
        self.update()

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        vistrel = self.name_input.text()
        self.coords.setText(f"Координаты: {event.x()}, {event.y()}")

        if (event.button() == Qt.RightButton):
            self.right = True
            self.num3.display(self.n)
            self.n += 1

        if (self.n - 1) == int(vistrel):
            self.predyp.show()

        self.repaint()
        eventx.append(event.x())
        eventy.append(event.y())

        if (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 40 ** 2:
            self.name_output.display('10')
            vsevstrl.append(10)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 80 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 > 40 ** 2:
            self.name_output.display('9')
            vsevstrl.append(9)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 120 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 20 ** 2:
            self.name_output.display('8')
            vsevstrl.append(8)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 160 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 60 ** 2:
            self.name_output.display('7')
            vsevstrl.append(7)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 200 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 100 ** 2:
            self.name_output.display('6')
            vsevstrl.append(6)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 240 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 140 ** 2:
            self.name_output.display('5')
            vsevstrl.append(5)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 280 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 180 ** 2:
            self.name_output.display('4')
            vsevstrl.append(4)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 320 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 220 ** 2:
            self.name_output.display('3')
            vsevstrl.append(3)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 360 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 260 ** 2:
            self.name_output.display('2')
            vsevstrl.append(2)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 <= 400 ** 2 and (event.x() - 620) ** 2 + (
                event.y() - 500) ** 2 >= 300 ** 2:
            self.name_output.display('1')
            vsevstrl.append(1)

        elif (event.x() - 620) ** 2 + (event.y() - 500) ** 2 > 400 ** 2:
            self.name_output.display('0')
            vsevstrl.append(0)

    def paintEvent(self, event):
        if self.paint_or_no:
            qp = QPainter()
            qp.begin(self)
            z = 0
            qp.setBrush(QColor(206, 206, 206))
            r = 370
            x = 620
            y = 500
            for i in range(10):
                qp.drawEllipse(x - r, y - r, r * 2, r * 2)
                r -= 40
                z += 20
            for obj in self.objects:
                obj.draw(qp)
            if self.z:
                self.objects.clear()
                self.z = False
            qp.setBrush(QColor(0, 0, 100))
            r = randint(30, 30)
            if self.right:
                qp.drawEllipse(self.x - r, self.y - r, r * 2, r * 2)
                self.right = False
            qp.end()
        if self.paint_or_noo:
            qp = QPainter()
            qp.begin(self)
            z = 0
            qp.setBrush(QColor(206, 206, 206))
            r = 370
            x = 620
            y = 500
            for i in range(9):
                qp.drawEllipse(x - r, y - r, r * 2, r * 2)
                r -= 40
                z += 20
            qp.drawEllipse(x - (r + 10), y - (r + 10), (r + 10) * 2, (r + 10) * 2)
            for obj in self.objects:
                obj.draw(qp)
            if self.z:
                self.objects.clear()
                self.z = False
            qp.setBrush(QColor(0, 0, 100))
            r = randint(30, 30)
            if self.right:
                qp.drawEllipse(self.x - r, self.y - r, r * 2, r * 2)
                self.right = False
            qp.end()
        if self.paint_or_no1:
            qp = QPainter()
            qp.begin(self)
            self.objects.clear()
            z = 0
            qp.setBrush(QColor(206, 206, 206))
            r = 370
            x = 620
            y = 500
            for i in range(10):
                qp.drawEllipse(x - r, y - r, r * 2, r * 2)
                r -= 40
                z += 20
            qp.setBrush(QColor(0, 0, 100))
            r = randint(30, 30)
            n = 0
            for i in range(len(eventx)):
                qp.drawEllipse(eventx[n] - r, eventy[n] - r, r * 2, r * 2)
                self.right = False
                n += 1
            qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z:
            self.z = True
            self.repaint()

    def finish(self):
        self.paint_or_no1 = True
        self.predyp1.hide()
        self.predyp.hide()
        self.num3.hide()
        self.itog4.hide()
        self.btn5.hide()
        self.name_output.hide()
        self.name_label100.hide()
        self.itog.show()
        self.itog1.show()
        self.itog2.show()
        self.itog3.show()
        self.btn_s.show()
        self.btn_s1.show()
        self.date.show()
        self.num.show()
        self.num1.show()
        self.num2.show()

        if len(vsevstrl) == 0:
            self.num2.display('0')
            self.num.display('0')
            self.num1.display('0')

        else:
            self.num2.display(sum(vsevstrl))
            self.num.display(len(vsevstrl))
            self.num1.display(sum(vsevstrl) / len(vsevstrl))

            stroka = str(datetime.now().date()) + ': ' + str(sum(vsevstrl)) + ' (' + str(len(vsevstrl)) + ') '
            f = open('винтовка.txt', 'a')
            f.write(stroka + '\n')
            print(stroka)

    def finish1(self):
        self.paint_or_no1 = True
        self.predyp1.hide()
        self.predyp.hide()
        self.num3.hide()
        self.itog4.hide()
        self.btn6.hide()
        self.name_output.hide()
        self.name_label100.hide()
        self.itog.show()
        self.itog1.show()
        self.itog2.show()
        self.itog3.show()
        self.btn_s.show()
        self.btn_s1.show()
        self.date.show()
        self.num.show()
        self.num1.show()
        self.num2.show()

        if len(vsevstrl) == 0:
            self.num2.display('0')
            self.num.display('0')
            self.num1.display('0')

        else:
            self.num2.display(sum(vsevstrl))
            self.num.display(len(vsevstrl))
            self.num1.display(sum(vsevstrl) / len(vsevstrl))

            strokaa = str(datetime.now().date()) + ': ' + str(sum(vsevstrl)) + ' (' + str(len(vsevstrl)) + ') '
            print(strokaa)
            f = open('пистолет.txt', 'a')
            л

    def rez_v(self):
        self.w2 = Window2()
        self.w2.show()

    def rez_p(self):
        self.w3 = Window3()
        self.w3.show()


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Винтовка. Все результаты')

        self.setGeometry(250, 150, 850, 850)
        f = open("винтовка.txt", 'r')
        self.name_label = QLabel(self)
        stroki = str(f.read())

        self.name_label.setText(stroki)
        self.name_label.move(30, -100)
        self.name_label.resize(800, 800)
        self.name_label.show()

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пистолет. Все результаты')

        self.setGeometry(250, 150, 850, 850)
        f = open("пистолет.txt", 'r')
        self.name_label = QLabel(self)
        stroki1 = str(f.read())

        self.name_label.setText(stroki1)
        self.name_label.move(30, -100)
        self.name_label.resize(800, 800)
        self.name_label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
