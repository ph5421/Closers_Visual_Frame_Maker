# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
import makeGIF

class Ui_Dialog(object):
    ex_image = Image.open("P_VISUAL_FRAME/P_VISUAL_FRAME_01.png")
    mframes = []
    loadDir = []
    disable = []
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 400)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.R_Slider = QtWidgets.QSlider(Dialog)
        self.R_Slider.setGeometry(QtCore.QRect(135, 230, 200, 20))
        self.R_Slider.setMaximum(500)
        self.R_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_Slider.setObjectName("R_Slider")
        self.R_Slider.valueChanged.connect(self.R_Slider_Changed)
        self.G_Slider = QtWidgets.QSlider(Dialog)
        self.G_Slider.setGeometry(QtCore.QRect(135, 260, 200, 20))
        self.G_Slider.setMaximum(500)
        self.G_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.G_Slider.setObjectName("G_Slider")
        self.G_Slider.valueChanged.connect(self.G_Slider_Changed)
        self.B_Slider = QtWidgets.QSlider(Dialog)
        self.B_Slider.setGeometry(QtCore.QRect(135, 290, 200, 20))
        self.B_Slider.setMaximum(500)
        self.B_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.B_Slider.setObjectName("B_Slider")
        self.B_Slider.valueChanged.connect(self.B_Slider_Changed)
        self.R_Lable = QtWidgets.QLineEdit(Dialog)
        self.R_Lable.setGeometry(QtCore.QRect(365, 230, 50, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.R_Lable.setFont(font)
        self.R_Lable.setObjectName("R_Lable")
        self.R_Lable.setValidator(QtGui.QIntValidator())
        self.R_Lable.textChanged.connect(self.R_Value_Changed)
        self.R_Lable.setText("0")
        self.R_Lable.setMaxLength(3)
        self.G_Lable = QtWidgets.QLineEdit(Dialog)
        self.G_Lable.setGeometry(QtCore.QRect(365, 260, 50, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.G_Lable.setFont(font)
        self.G_Lable.setObjectName("G_Lable")
        self.G_Lable.setValidator(QtGui.QIntValidator(0,900))
        self.G_Lable.textChanged.connect(self.G_Value_Changed)
        self.G_Lable.setText("0")
        self.G_Lable.setMaxLength(3)
        self.B_Lable = QtWidgets.QLineEdit(Dialog)
        self.B_Lable.setGeometry(QtCore.QRect(365, 290, 50, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.B_Lable.setFont(font)
        self.B_Lable.setObjectName("B_Lable")
        self.B_Lable.setValidator(QtGui.QIntValidator(0,900))
        self.B_Lable.textChanged.connect(self.B_Value_Changed)
        self.B_Lable.setText("0")
        self.B_Lable.setMaxLength(3)
        self.R_Text = QtWidgets.QLabel(Dialog)
        self.R_Text.setGeometry(QtCore.QRect(100, 230, 20, 15))
        self.R_Text.setObjectName("R_Text")
        self.G_Text = QtWidgets.QLabel(Dialog)
        self.G_Text.setGeometry(QtCore.QRect(100, 260, 20, 15))
        self.G_Text.setObjectName("G_Text")
        self.B_Text = QtWidgets.QLabel(Dialog)
        self.B_Text.setGeometry(QtCore.QRect(100, 290, 20, 15))
        self.B_Text.setObjectName("B_Text")
        self.Save = QtWidgets.QPushButton(Dialog)
        self.Save.setGeometry(QtCore.QRect(290, 350, 75, 25))
        self.Save.clicked.connect(self.save_image)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.Load = QtWidgets.QPushButton(Dialog)
        self.Load.setGeometry(QtCore.QRect(150, 350, 75, 25))
        self.Load.clicked.connect(self.load_image)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Load.setFont(font)
        self.Load.setObjectName("Load")
        self.exImage = QtWidgets.QLabel(Dialog)
        self.exImage.setGeometry(QtCore.QRect(4, 4, 1024, 173))
        self.exImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.exImage.setText("")
        self.exImage.setObjectName("Image")
        self.disable.extend([self.R_Slider,self.G_Slider,self.B_Slider,self.R_Lable,self.G_Lable,self.B_Lable,self.Save])
        for i in self.disable:
            i.setEnabled(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FrameMaker"))
        self.R_Text.setText(_translate("Dialog", "R"))
        self.G_Text.setText(_translate("Dialog", "G"))
        self.B_Text.setText(_translate("Dialog", "B"))
        self.Save.setText(_translate("Dialog", "저장"))
        self.Load.setText(_translate("Dialog", "불러오기"))

    def R_Value_Changed(self):
        if(self.R_Lable.text()==""):
            self.R_Lable.setText("0")
        if(len(self.R_Lable.text())>1 and self.R_Lable.text()[0]=='0'):
            t=self.R_Lable.text()
            t=t[1:]
            self.R_Lable.setText(t)
        if(int(self.R_Lable.text())>500):
            self.R_Lable.setText("500")
        self.R_Slider.setValue(int(self.R_Lable.text()))
        self.example_image()

    def G_Value_Changed(self):
        if(self.G_Lable.text()==""):
            self.G_Lable.setText("0")
        if(len(self.G_Lable.text())>1 and self.G_Lable.text()[0]=='0'):
            t=self.G_Lable.text()
            t=t[1:]
            self.G_Lable.setText(t)
        if(int(self.G_Lable.text())>500):
            self.G_Lable.setText("500")
        self.G_Slider.setValue(int(self.G_Lable.text()))
        self.example_image()

    def B_Value_Changed(self):
        if(self.B_Lable.text()==""):
            self.B_Lable.setText("0")
        if(len(self.B_Lable.text())>1 and self.B_Lable.text()[0]=='0'):
            t=self.B_Lable.text()
            t=t[1:]
            self.B_Lable.setText(t)
        if(int(self.B_Lable.text())>500):
            self.B_Lable.setText("500")
        self.B_Slider.setValue(int(self.B_Lable.text()))
        self.example_image()
    

    def R_Slider_Changed(self):
        self.R_Lable.setText(str(self.R_Slider.value()))
        self.example_image()

    def G_Slider_Changed(self):
        self.G_Lable.setText(str(self.G_Slider.value()))
        self.example_image()

    def B_Slider_Changed(self):
        self.B_Lable.setText(str(self.B_Slider.value()))
        self.example_image()


    def load_image(self):
        options = QtWidgets.QFileDialog.Options()
        self.loadDir = QtWidgets.QFileDialog.getOpenFileName(Dialog, 'Open Image', "",
                                                         "Images (*.png *.jpeg *.jpg *.bmp)", options=options)
        if(self.loadDir[0]!=''):
            for i in self.disable:
                i.setEnabled(True)
            self.example_image()

    def save_image(self):
        options = QtWidgets.QFileDialog.Options()
        saveDir = QtWidgets.QFileDialog.getSaveFileName(Dialog,'Save GIF',"",
                                                          "Images (*.gif)", options=options)
        if(saveDir[0]!=''):
            self.example_image()
            makeGIF.main(1,self.loadDir[0],self.R_Slider.value(),self.G_Slider.value(),self.B_Slider.value(),saveDir[0])
        
    def example_image(self):
        if(len(self.loadDir)):
            c_ex_image = makeGIF.changeRGB(self.R_Slider.value(),self.G_Slider.value(),self.B_Slider.value(),self.ex_image)
            exam_img = makeGIF.combine(Image.open(self.loadDir[0]), c_ex_image)
            qtim=ImageQt(exam_img)
            self.exImage.setPixmap(QtGui.QPixmap.fromImage(qtim))
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
