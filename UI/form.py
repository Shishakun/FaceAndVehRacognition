import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QStackedWidget,
)


class MainWindow(QMainWindow):
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

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример использования QStackedWidget")
        self.setGeometry(100, 100, 300, 200)

        # Создаем главный виджет и вертикальный слой
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)

        # Создаем кнопки
        self.button1 = QPushButton("Кнопка 1", self.main_widget)
        self.button2 = QPushButton("Кнопка 2", self.main_widget)

        # Создаем QStackedWidget
        self.stacked_widget = QStackedWidget(self.main_widget)

        # Создаем страницы и добавляем их в QStackedWidget
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Добавляем виджет QStackedWidget и кнопки в вертикальный слой
        self.layout.addWidget(self.stacked_widget)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        # Устанавливаем активную страницу и изменяем дизайн кнопки1
        self.stacked_widget.setCurrentWidget(self.page1)
        self.button1.setStyleSheet("background-color: yellow")

        # Подключаем слоты к сигналам кнопок
        self.button1.clicked.connect(self.show_page1)
        self.button2.clicked.connect(self.show_page2)

        self.setCentralWidget(self.main_widget)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)
        self.button1.setStyleSheet("background-color: yellow")
        self.button2.setStyleSheet("")

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)
        self.button1.setStyleSheet("")
        self.button2.setStyleSheet("background-color: yellow")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
