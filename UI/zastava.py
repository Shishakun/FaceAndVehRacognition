from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Zastava(object):
    def setupUi(self, Zastava):
        Zastava.setObjectName("Zastava")
        Zastava.resize(1480, 945)
        Zastava.setMinimumSize(QtCore.QSize(0, 0))
        Zastava.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.centralwidget = QtWidgets.QWidget(Zastava)
        self.centralwidget.setMinimumSize(QtCore.QSize(1480, 800))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerContainer = QtWidgets.QWidget(self.centralwidget)
        self.headerContainer.setEnabled(True)
        self.headerContainer.setMaximumSize(QtCore.QSize(999999, 999999))
        self.headerContainer.setStyleSheet("*{padding:0px}")
        self.headerContainer.setObjectName("headerContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.headerContainer)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonContainer = QtWidgets.QFrame(self.headerContainer)
        self.buttonContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonContainer.setObjectName("buttonContainer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonContainer)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vehicleRecognition = QtWidgets.QPushButton(self.buttonContainer)
        self.vehicleRecognition.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(46, 46, 46);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}"
        )
        self.vehicleRecognition.setObjectName("vehicleRecognition")
        self.vehicleRecognition.clicked.connect(self.show_page_1)
        self.horizontalLayout.addWidget(self.vehicleRecognition)
        self.faceRecognition = QtWidgets.QPushButton(self.buttonContainer)
        self.faceRecognition.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(35, 35, 35);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}\n"
            "QPushButton:unactive{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}"
        )
        self.faceRecognition.setObjectName("faceRecognition")
        self.faceRecognition.clicked.connect(self.show_page_2)
        self.horizontalLayout.addWidget(self.faceRecognition)
        self.verticalLayout_2.addWidget(self.buttonContainer)
        self.stackedWidgetPage = QtWidgets.QStackedWidget(self.headerContainer)
        self.stackedWidgetPage.setObjectName("stackedWidgetPage")
        self.allRecPage = QtWidgets.QWidget()
        self.allRecPage.setObjectName("allRecPage")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.allRecPage)
        self.horizontalLayout_4.setContentsMargins(0, 6, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainContainerAllRecog = QtWidgets.QWidget(self.allRecPage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainContainerAllRecog.sizePolicy().hasHeightForWidth()
        )
        self.mainContainerAllRecog.setSizePolicy(sizePolicy)
        self.mainContainerAllRecog.setObjectName("mainContainerAllRecog")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainContainerAllRecog)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 12)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftContainerAllRecog = QtWidgets.QWidget(self.mainContainerAllRecog)
        self.leftContainerAllRecog.setMinimumSize(QtCore.QSize(1080, 0))
        self.leftContainerAllRecog.setObjectName("leftContainerAllRecog")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftContainerAllRecog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.videoContainerAllRecog = QtWidgets.QWidget(self.leftContainerAllRecog)
        self.videoContainerAllRecog.setObjectName("videoContainerAllRecog")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.videoContainerAllRecog)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.videoTitleAllRecog = QtWidgets.QLabel(self.videoContainerAllRecog)
        self.videoTitleAllRecog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.videoTitleAllRecog.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(46, 46, 46);\n"
            "border-radius: 10px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px; "
        )
        self.videoTitleAllRecog.setAlignment(QtCore.Qt.AlignCenter)
        self.videoTitleAllRecog.setObjectName("videoTitleAllRecog")
        self.verticalLayout_4.addWidget(self.videoTitleAllRecog)
        self.videoWindowAllRecog = QtWidgets.QLabel(self.videoContainerAllRecog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.videoWindowAllRecog.sizePolicy().hasHeightForWidth()
        )
        self.videoWindowAllRecog.setSizePolicy(sizePolicy)
        self.videoWindowAllRecog.setMinimumSize(QtCore.QSize(1000, 700))
        self.videoWindowAllRecog.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.videoWindowAllRecog.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.videoWindowAllRecog.setFrameShadow(QtWidgets.QLabel.Raised)
        self.videoWindowAllRecog.setAlignment(Qt.AlignCenter)
        self.videoWindowAllRecog.setObjectName("videoWindowAllRecog")
        self.verticalLayout_4.addWidget(self.videoWindowAllRecog)
        self.verticalLayout_3.addWidget(self.videoContainerAllRecog)
        self.soundRecognitionContainer = QtWidgets.QWidget(self.leftContainerAllRecog)
        self.soundRecognitionContainer.setObjectName("soundRecognitionContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.soundRecognitionContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.soundTitle = QtWidgets.QLabel(self.soundRecognitionContainer)
        self.soundTitle.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "font: bold 20px;\n"
            "min-width: 10em;\n"
            "padding: 6px; "
        )
        self.soundTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.soundTitle.setObjectName("soundTitle")
        self.verticalLayout_5.addWidget(self.soundTitle)
        self.YamnetTextBox = QtWidgets.QTextBrowser(self.soundRecognitionContainer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        self.YamnetTextBox.setStyleSheet(
            "QTextBrowser { text-align: center; color: white; font: bold 26px; padding: 6px; align-items: center};"
        )
        self.YamnetTextBox.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.YamnetTextBox.sizePolicy().hasHeightForWidth()
        )
        self.YamnetTextBox.setSizePolicy(sizePolicy)
        self.YamnetTextBox.setObjectName("YamnetTextBox")
        self.verticalLayout_5.addWidget(self.YamnetTextBox)
        self.verticalLayout_3.addWidget(self.soundRecognitionContainer)
        self.horizontalLayout_2.addWidget(self.leftContainerAllRecog)
        self.historyRecognitionContainer = QtWidgets.QWidget(self.mainContainerAllRecog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.historyRecognitionContainer.sizePolicy().hasHeightForWidth()
        )
        self.historyRecognitionContainer.setSizePolicy(sizePolicy)
        self.historyRecognitionContainer.setMaximumSize(QtCore.QSize(500, 16777215))
        self.historyRecognitionContainer.setObjectName("historyRecognitionContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.historyRecognitionContainer)
        self.verticalLayout_6.setContentsMargins(4, 0, 0, 0)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.historyRec1 = QtWidgets.QFrame(self.historyRecognitionContainer)
        self.historyRec1.setMinimumSize(QtCore.QSize(250, 0))
        self.historyRec1.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyRec1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyRec1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyRec1.setObjectName("historyRec1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.historyRec1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.historyFoto1 = QtWidgets.QLabel(self.historyRec1)
        self.historyFoto1.setMinimumSize(QtCore.QSize(170, 0))
        self.historyFoto1.setMaximumSize(QtCore.QSize(170, 170))
        self.historyFoto1.setStyleSheet("border-radius: 10px;")
        self.historyFoto1.setText("")
        self.historyFoto1.setObjectName("historyFoto1")
        self.horizontalLayout_3.addWidget(self.historyFoto1)
        self.historyText1 = QtWidgets.QLabel(self.historyRec1)
        self.historyText1.setMinimumSize(QtCore.QSize(170, 0))
        self.historyText1.setMaximumSize(QtCore.QSize(450, 16777215))
        self.historyText1.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyText1.setTextFormat(QtCore.Qt.AutoText)
        self.historyText1.setScaledContents(False)
        self.historyText1.setAlignment(QtCore.Qt.AlignCenter)
        self.historyText1.setWordWrap(True)
        self.historyText1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.historyText1.setObjectName("historyText1")
        self.horizontalLayout_3.addWidget(self.historyText1)
        self.verticalLayout_6.addWidget(self.historyRec1)
        self.historyRec2 = QtWidgets.QFrame(self.historyRecognitionContainer)
        self.historyRec2.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyRec2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyRec2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyRec2.setObjectName("historyRec2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.historyRec2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.historyFoto2 = QtWidgets.QLabel(self.historyRec2)
        self.historyFoto2.setMaximumSize(QtCore.QSize(170, 170))
        self.historyFoto2.setStyleSheet("border-radius: 10px;")
        self.historyFoto2.setText("")
        self.historyFoto2.setObjectName("historyFoto2")
        self.horizontalLayout_5.addWidget(self.historyFoto2)
        self.historyText2 = QtWidgets.QLabel(self.historyRec2)
        self.historyText2.setMinimumSize(QtCore.QSize(170, 0))
        self.historyText2.setMaximumSize(QtCore.QSize(450, 16777215))
        self.historyText2.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyText2.setText("")
        self.historyText2.setAlignment(QtCore.Qt.AlignCenter)
        self.historyText2.setWordWrap(True)
        self.historyText2.setObjectName("historyText2")
        self.horizontalLayout_5.addWidget(self.historyText2)
        self.verticalLayout_6.addWidget(self.historyRec2)
        self.historyRec3 = QtWidgets.QFrame(self.historyRecognitionContainer)
        self.historyRec3.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyRec3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyRec3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyRec3.setObjectName("historyRec3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.historyRec3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.historyFoto3 = QtWidgets.QLabel(self.historyRec3)
        self.historyFoto3.setMaximumSize(QtCore.QSize(170, 170))
        self.historyFoto3.setStyleSheet("border-radius: 10px;")
        self.historyFoto3.setText("")
        self.historyFoto3.setObjectName("historyFoto3")
        self.horizontalLayout_6.addWidget(self.historyFoto3)
        self.historyText3 = QtWidgets.QLabel(self.historyRec3)
        self.historyText3.setMinimumSize(QtCore.QSize(170, 0))
        self.historyText3.setMaximumSize(QtCore.QSize(450, 16777215))
        self.historyText3.setStyleSheet(
            "border-radius: 10px;color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyText3.setText("")
        self.historyText3.setAlignment(QtCore.Qt.AlignCenter)
        self.historyText3.setWordWrap(True)
        self.historyText3.setObjectName("historyText3")
        self.horizontalLayout_6.addWidget(self.historyText3)
        self.verticalLayout_6.addWidget(self.historyRec3)
        self.historyRec4 = QtWidgets.QFrame(self.historyRecognitionContainer)
        self.historyRec4.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyRec4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyRec4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyRec4.setObjectName("historyRec4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.historyRec4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.historyFoto4 = QtWidgets.QLabel(self.historyRec4)
        self.historyFoto4.setMaximumSize(QtCore.QSize(170, 170))
        self.historyFoto4.setStyleSheet("border-radius: 10px;")
        self.historyFoto4.setText("")
        self.historyFoto4.setObjectName("historyFoto4")
        self.horizontalLayout_7.addWidget(self.historyFoto4)
        self.historyText4 = QtWidgets.QLabel(self.historyRec4)
        self.historyText4.setMinimumSize(QtCore.QSize(170, 0))
        self.historyText4.setMaximumSize(QtCore.QSize(450, 16777215))
        self.historyText4.setStyleSheet(
            "border-radius: 10px;color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyText4.setText("")
        self.historyText4.setAlignment(QtCore.Qt.AlignCenter)
        self.historyText4.setWordWrap(True)
        self.historyText4.setObjectName("historyText4")
        self.horizontalLayout_7.addWidget(self.historyText4)
        self.verticalLayout_6.addWidget(self.historyRec4)
        self.historyRec5 = QtWidgets.QFrame(self.historyRecognitionContainer)
        self.historyRec5.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyRec5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyRec5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyRec5.setObjectName("historyRec5")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.historyRec5)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.historyFoto5 = QtWidgets.QLabel(self.historyRec5)
        self.historyFoto5.setMaximumSize(QtCore.QSize(170, 170))
        self.historyFoto5.setStyleSheet("border-radius: 10px;")
        self.historyFoto5.setText("")
        self.historyFoto5.setObjectName("historyFoto5")
        self.horizontalLayout_34.addWidget(self.historyFoto5)
        self.historyText65 = QtWidgets.QLabel(self.historyRec5)
        self.historyText65.setMinimumSize(QtCore.QSize(170, 0))
        self.historyText65.setMaximumSize(QtCore.QSize(450, 16777215))
        self.historyText65.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyText65.setText("")
        self.historyText65.setAlignment(QtCore.Qt.AlignCenter)
        self.historyText65.setWordWrap(True)
        self.historyText65.setObjectName("historyText65")
        self.horizontalLayout_34.addWidget(self.historyText65)
        self.verticalLayout_6.addWidget(self.historyRec5)
        self.historyRec6 = QtWidgets.QFrame(self.historyRecognitionContainer)
        self.historyRec6.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyRec6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyRec6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyRec6.setObjectName("historyRec6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.historyRec6)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.historyFoto6 = QtWidgets.QLabel(self.historyRec6)
        self.historyFoto6.setMaximumSize(QtCore.QSize(170, 170))
        self.historyFoto6.setStyleSheet("border-radius: 10px;")
        self.historyFoto6.setText("")
        self.historyFoto6.setObjectName("historyFoto6")
        self.horizontalLayout_8.addWidget(self.historyFoto6)
        self.historyText6 = QtWidgets.QLabel(self.historyRec6)
        self.historyText6.setMinimumSize(QtCore.QSize(170, 0))
        self.historyText6.setMaximumSize(QtCore.QSize(450, 16777215))
        self.historyText6.setStyleSheet(
            "border-radius: 10px;color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyText6.setText("")
        self.historyText6.setAlignment(QtCore.Qt.AlignCenter)
        self.historyText6.setWordWrap(True)
        self.historyText6.setObjectName("historyText6")
        self.horizontalLayout_8.addWidget(self.historyText6)
        self.verticalLayout_6.addWidget(self.historyRec6)
        self.horizontalLayout_2.addWidget(self.historyRecognitionContainer)
        self.horizontalLayout_4.addWidget(self.mainContainerAllRecog)
        self.stackedWidgetPage.addWidget(self.allRecPage)
        self.faceRecPage = QtWidgets.QWidget()
        self.faceRecPage.setObjectName("faceRecPage")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.faceRecPage)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.mainContainerFaceRecog = QtWidgets.QWidget(self.faceRecPage)
        self.mainContainerFaceRecog.setObjectName("mainContainerFaceRecog")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.mainContainerFaceRecog)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.videoFaceRecogContainer = QtWidgets.QWidget(self.mainContainerFaceRecog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.videoFaceRecogContainer.sizePolicy().hasHeightForWidth()
        )
        self.videoFaceRecogContainer.setSizePolicy(sizePolicy)
        self.videoFaceRecogContainer.setObjectName("videoFaceRecogContainer")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.videoFaceRecogContainer)
        self.verticalLayout_24.setContentsMargins(0, 4, 4, 0)
        self.verticalLayout_24.setSpacing(4)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.videoTitleFaceRecogText = QtWidgets.QLabel(self.videoFaceRecogContainer)
        self.videoTitleFaceRecogText.setMaximumSize(QtCore.QSize(16777215, 40))
        self.videoTitleFaceRecogText.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(46, 46, 46);\n"
            "border-radius: 10px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px; "
        )
        self.videoTitleFaceRecogText.setAlignment(QtCore.Qt.AlignCenter)
        self.videoTitleFaceRecogText.setObjectName("videoTitleFaceRecogText")
        self.verticalLayout_24.addWidget(self.videoTitleFaceRecogText)
        self.videoPotokFaceRecog = QtWidgets.QLabel(self.videoFaceRecogContainer)
        self.videoPotokFaceRecog.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.videoPotokFaceRecog.setAlignment(QtCore.Qt.AlignCenter)
        self.videoPotokFaceRecog.setText("")
        self.videoPotokFaceRecog.setObjectName("videoPotokFaceRecog")
        self.verticalLayout_24.addWidget(self.videoPotokFaceRecog)
        self.usersButtonPanel = QtWidgets.QFrame(self.videoFaceRecogContainer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.usersButtonPanel.sizePolicy().hasHeightForWidth()
        )
        self.usersButtonPanel.setSizePolicy(sizePolicy)
        self.usersButtonPanel.setMaximumSize(QtCore.QSize(12389, 40))
        self.usersButtonPanel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usersButtonPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usersButtonPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usersButtonPanel.setObjectName("usersButtonPanel")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.usersButtonPanel)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.addUserButton = QtWidgets.QPushButton(self.usersButtonPanel)
        self.addUserButton.setMinimumSize(QtCore.QSize(182, 32))
        self.addUserButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addUserButton.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(35, 35, 35);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}\n"
            "QPushButton:unactive{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}"
        )
        self.addUserButton.setObjectName("addUserButton")
        self.horizontalLayout_9.addWidget(self.addUserButton)
        self.verticalLayout_24.addWidget(self.usersButtonPanel)
        self.horizontalLayout_33.addWidget(self.videoFaceRecogContainer)
        self.historyFaceRecogContainer = QtWidgets.QWidget(self.mainContainerFaceRecog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.historyFaceRecogContainer.sizePolicy().hasHeightForWidth()
        )
        self.historyFaceRecogContainer.setSizePolicy(sizePolicy)
        self.historyFaceRecogContainer.setMinimumSize(QtCore.QSize(500, 0))
        self.historyFaceRecogContainer.setMaximumSize(QtCore.QSize(500, 16777215))
        self.historyFaceRecogContainer.setObjectName("historyFaceRecogContainer")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.historyFaceRecogContainer)
        self.verticalLayout_23.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_23.setSpacing(4)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.historyFaceRecog1 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog1.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog1.setObjectName("historyFaceRecog1")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.historyFaceRecog1)
        self.horizontalLayout_35.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.historyForoFaceRecog1 = QtWidgets.QLabel(self.historyFaceRecog1)
        self.historyForoFaceRecog1.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog1.setText("")
        self.historyForoFaceRecog1.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog1.setObjectName("historyForoFaceRecog1")
        self.horizontalLayout_35.addWidget(self.historyForoFaceRecog1)
        self.historyInfoFaceRecog1 = QtWidgets.QLabel(self.historyFaceRecog1)
        self.historyInfoFaceRecog1.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog1.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog1.setText("")
        self.historyInfoFaceRecog1.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog1.setWordWrap(True)
        self.historyInfoFaceRecog1.setObjectName("historyInfoFaceRecog1")
        self.horizontalLayout_35.addWidget(self.historyInfoFaceRecog1)
        self.verticalLayout_23.addWidget(self.historyFaceRecog1)
        self.historyFaceRecog2 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog2.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog2.setObjectName("historyFaceRecog2")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.historyFaceRecog2)
        self.horizontalLayout_36.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.historyForoFaceRecog2 = QtWidgets.QLabel(self.historyFaceRecog2)
        self.historyForoFaceRecog2.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog2.setText("")
        self.historyForoFaceRecog2.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog2.setObjectName("historyForoFaceRecog2")
        self.horizontalLayout_36.addWidget(self.historyForoFaceRecog2)
        self.historyInfoFaceRecog2 = QtWidgets.QLabel(self.historyFaceRecog2)
        self.historyInfoFaceRecog2.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog2.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog2.setText("")
        self.historyInfoFaceRecog2.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog2.setWordWrap(True)
        self.historyInfoFaceRecog2.setObjectName("historyInfoFaceRecog2")
        self.horizontalLayout_36.addWidget(self.historyInfoFaceRecog2)
        self.verticalLayout_23.addWidget(self.historyFaceRecog2)
        self.historyFaceRecog7 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog7.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog7.setObjectName("historyFaceRecog7")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.historyFaceRecog7)
        self.horizontalLayout_41.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.historyForoFaceRecog7 = QtWidgets.QLabel(self.historyFaceRecog7)
        self.historyForoFaceRecog7.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog7.setText("")
        self.historyForoFaceRecog7.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog7.setObjectName("historyForoFaceRecog7")
        self.horizontalLayout_41.addWidget(self.historyForoFaceRecog7)
        self.historyInfoFaceRecog7 = QtWidgets.QLabel(self.historyFaceRecog7)
        self.historyInfoFaceRecog7.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog7.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog7.setText("")
        self.historyInfoFaceRecog7.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog7.setWordWrap(True)
        self.historyInfoFaceRecog7.setObjectName("historyInfoFaceRecog7")
        self.horizontalLayout_41.addWidget(self.historyInfoFaceRecog7)
        self.verticalLayout_23.addWidget(self.historyFaceRecog7)
        self.historyFaceRecog6 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog6.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog6.setObjectName("historyFaceRecog6")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.historyFaceRecog6)
        self.horizontalLayout_40.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.historyForoFaceRecog6 = QtWidgets.QLabel(self.historyFaceRecog6)
        self.historyForoFaceRecog6.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog6.setText("")
        self.historyForoFaceRecog6.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog6.setObjectName("historyForoFaceRecog6")
        self.horizontalLayout_40.addWidget(self.historyForoFaceRecog6)
        self.historyInfoFaceRecog6 = QtWidgets.QLabel(self.historyFaceRecog6)
        self.historyInfoFaceRecog6.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog6.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog6.setText("")
        self.historyInfoFaceRecog6.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog6.setWordWrap(True)
        self.historyInfoFaceRecog6.setObjectName("historyInfoFaceRecog6")
        self.horizontalLayout_40.addWidget(self.historyInfoFaceRecog6)
        self.verticalLayout_23.addWidget(self.historyFaceRecog6)
        self.historyFaceRecog5 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog5.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog5.setObjectName("historyFaceRecog5")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.historyFaceRecog5)
        self.horizontalLayout_39.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.historyForoFaceRecog5 = QtWidgets.QLabel(self.historyFaceRecog5)
        self.historyForoFaceRecog5.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog5.setText("")
        self.historyForoFaceRecog5.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog5.setObjectName("historyForoFaceRecog5")
        self.horizontalLayout_39.addWidget(self.historyForoFaceRecog5)
        self.historyInfoFaceRecog5 = QtWidgets.QLabel(self.historyFaceRecog5)
        self.historyInfoFaceRecog5.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog5.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog5.setText("")
        self.historyInfoFaceRecog5.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog5.setWordWrap(True)
        self.historyInfoFaceRecog5.setObjectName("historyInfoFaceRecog5")
        self.horizontalLayout_39.addWidget(self.historyInfoFaceRecog5)
        self.verticalLayout_23.addWidget(self.historyFaceRecog5)
        self.historyFaceRecog4 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog4.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog4.setObjectName("historyFaceRecog4")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.historyFaceRecog4)
        self.horizontalLayout_38.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.historyForoFaceRecog4 = QtWidgets.QLabel(self.historyFaceRecog4)
        self.historyForoFaceRecog4.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog4.setText("")
        self.historyForoFaceRecog4.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog4.setObjectName("historyForoFaceRecog4")
        self.horizontalLayout_38.addWidget(self.historyForoFaceRecog4)
        self.historyInfoFaceRecog4 = QtWidgets.QLabel(self.historyFaceRecog4)
        self.historyInfoFaceRecog4.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog4.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog4.setText("")
        self.historyInfoFaceRecog4.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog4.setWordWrap(True)
        self.historyInfoFaceRecog4.setObjectName("historyInfoFaceRecog4")
        self.horizontalLayout_38.addWidget(self.historyInfoFaceRecog4)
        self.verticalLayout_23.addWidget(self.historyFaceRecog4)
        self.historyFaceRecog3 = QtWidgets.QFrame(self.historyFaceRecogContainer)
        self.historyFaceRecog3.setStyleSheet(
            "background-color: rgb(46, 46, 46);\n" "border-radius: 10px;"
        )
        self.historyFaceRecog3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFaceRecog3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFaceRecog3.setObjectName("historyFaceRecog3")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.historyFaceRecog3)
        self.horizontalLayout_37.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.historyForoFaceRecog3 = QtWidgets.QLabel(self.historyFaceRecog3)
        self.historyForoFaceRecog3.setMaximumSize(QtCore.QSize(150, 150))
        self.historyForoFaceRecog3.setText("")
        self.historyForoFaceRecog3.setAlignment(QtCore.Qt.AlignCenter)
        self.historyForoFaceRecog3.setObjectName("historyForoFaceRecog3")
        self.horizontalLayout_37.addWidget(self.historyForoFaceRecog3)
        self.historyInfoFaceRecog3 = QtWidgets.QLabel(self.historyFaceRecog3)
        self.historyInfoFaceRecog3.setMinimumSize(QtCore.QSize(300, 0))
        self.historyInfoFaceRecog3.setStyleSheet(
            "color: #ffffff;\n"
            "font-family: Roboto;\n"
            "font-size: 14px;\n"
            "font-weight: bold;"
        )
        self.historyInfoFaceRecog3.setText("")
        self.historyInfoFaceRecog3.setAlignment(QtCore.Qt.AlignCenter)
        self.historyInfoFaceRecog3.setWordWrap(True)
        self.historyInfoFaceRecog3.setObjectName("historyInfoFaceRecog3")
        self.horizontalLayout_37.addWidget(self.historyInfoFaceRecog3)
        self.verticalLayout_23.addWidget(self.historyFaceRecog3)
        self.horizontalLayout_33.addWidget(self.historyFaceRecogContainer)
        self.horizontalLayout_32.addWidget(self.mainContainerFaceRecog)
        self.stackedWidgetPage.addWidget(self.faceRecPage)
        self.verticalLayout_2.addWidget(self.stackedWidgetPage)
        self.verticalLayout.addWidget(self.headerContainer)
        Zastava.setCentralWidget(self.centralwidget)

        self.retranslateUi(Zastava)
        self.stackedWidgetPage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Zastava)

    def retranslateUi(self, Zastava):
        _translate = QtCore.QCoreApplication.translate
        Zastava.setWindowTitle(_translate("Zastava", "MainWindow"))
        self.vehicleRecognition.setText(_translate("Zastava", "Обнаружение объектов"))
        self.faceRecognition.setText(_translate("Zastava", "Контроль доступа"))
        self.videoTitleAllRecog.setText(_translate("Zastava", "Видеопоток"))
        self.soundTitle.setText(_translate("Zastava", "Анализ звукового окружения"))
        self.YamnetTextBox.setHtml(
            _translate(
                "Zastava",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                '</style></head><body style="color:white; font-size:7.8pt; font-weight:400; font-style:normal;">\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; color:white; -qt-block-indent:0; text-indent:0px; font-size:14.8pt;"><br /></p></body></html>',
            )
        )
        self.historyText1.setText(
            _translate("Zastava", "<html><head/><body><p><br/></p></body></html>")
        )
        self.videoTitleFaceRecogText.setText(_translate("Zastava", "Видеопоток"))
        self.addUserButton.setText(
            _translate("Zastava", "Добавить пользователя в базу данных")
        )

    def show_page_1(self):
        self.stackedWidgetPage.setCurrentIndex(0)
        self.vehicleRecognition.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(46, 46, 46);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}\n"
        )
        self.faceRecognition.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(35, 35, 35);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}\n"
        )

    def show_page_2(self):
        self.stackedWidgetPage.setCurrentIndex(1)
        self.vehicleRecognition.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(35, 35, 35);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}\n"
        )
        self.faceRecognition.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(46, 46, 46);\n"
            "color: #ffffff;\n"
            "border-style: outset;\n"
            "border-radius: 7px;\n"
            "font: bold 14px;\n"
            "min-width: 10em;\n"
            "padding: 6px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(46, 46, 46);\n"
            "}\n"
        )
