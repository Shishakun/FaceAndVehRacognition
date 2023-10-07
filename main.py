import sys
import cv2

import threading
import pyaudio
import librosa
import numpy as np
import matplotlib.pyplot as plt
import keras

import Yamnet.yamnet.params as params
import Yamnet.yamnet.yamnet as yamnet_model
from loguru import logger

from UI.addUsers import Ui_AddUsersWidget as AddUsersWidget
from UI.zastava import Ui_Zastava as ZastavaMainWindow


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt


# класс для демонстрации видео
class VideoThread(QThread):
    image_data = pyqtSignal(object)

    def run(self):
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()

            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resized_image = cv2.resize(rgb_image, (750, 480))
                self.image_data.emit(resized_image)

            if cv2.waitKey(1) == 27:
                break

        video_capture.release()

class VideoThreadFace(QThread):
    image_data_face = pyqtSignal(object)

    def run(self):
        video_capture_face = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture_face.read()

            if ret:
                rgb_image_face = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resized_image_face = cv2.resize(rgb_image_face, (640, 640))
                self.image_data_face.emit(resized_image_face)

            if cv2.waitKey(1) == 27:
                break

        video_capture_face.release()
        
# Добавление юзера в БД
class AddUserWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = AddUsersWidget()
        self.ui.setupUi(self)
        
        self.video_thread_face = VideoThreadFace()
        self.video_thread_face.image_data_face.connect(self.update_image_face)
        self.video_thread_face.start()

    def update_image_face(self, image):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.ui.videoFromWebCam.setPixmap(
            pixmap.scaled(
                self.ui.videoFromWebCam.size(), aspectRatioMode=Qt.KeepAspectRatio
            )
        )


# Основной графический интерфейс
class Zastava(QtWidgets.QMainWindow):
    def __init__(self):
        super(Zastava, self).__init__()
        self.ui = ZastavaMainWindow()
        self.ui.setupUi(self)
        self.ui.addUserButton.clicked.connect(self.open_addUser)
        self.widget = None

        self.worker = Worker()
        self.worker.update_text_signal.connect(self.display_yamnet_result)

        # Видеозахват
        self.video_thread = VideoThread()
        self.video_thread.image_data.connect(self.update_image)
        self.video_thread.start()

    def update_image(self, image):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.ui.videoPotokFaceRecog.setPixmap(
            pixmap.scaled(
                self.ui.videoPotokFaceRecog.size(), aspectRatioMode=Qt.KeepAspectRatio
            )
        )
        self.ui.videoWindowAllRecog.setPixmap(
            pixmap.scaled(
                self.ui.videoWindowAllRecog.size(), aspectRatioMode=Qt.KeepAspectRatio
            )
        )

    def update_audio(self):
        self.worker.process_audio()

    # Открытие виджета добавления пользователя
    def open_addUser(self):
        if self.widget is None:
            self.widget = AddUserWidget()
        self.widget.show()

    # Отображение результата работы yamnet
    def display_yamnet_result(self, result):
        self.ui.YamnetTextBox.setText(result)


class Worker(QtCore.QObject):
    update_text_signal = QtCore.pyqtSignal(str)

    def process_audio(self):
        yamnet = yamnet_model.yamnet_frames_model(params)
        yamnet.load_weights("Yamnet/yamnet/yamnet.h5")
        yamnet_classes = yamnet_model.class_names("Yamnet/yamnet/yamnet_class_map.csv")

        frame_len = int(params.SAMPLE_RATE * 1)  # 1sec

        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=params.SAMPLE_RATE,
            input=True,
            frames_per_buffer=frame_len,
        )

        cnt = 0
        plt.ion()
        while True:
            # data read
            data = stream.read(frame_len, exception_on_overflow=False)

            # byte --> float
            frame_data = librosa.util.buf_to_float(data, n_bytes=2, dtype=np.int16)

            # model prediction
            scores, melspec = yamnet.predict(np.reshape(frame_data, [1, -1]), steps=1)
            prediction = np.mean(scores, axis=0)

            top5_i = np.argsort(prediction)[::-1][:2]

            # append result to list
            result = "Текущее событие:\n" + "".join(
                "  {:12s}: {:.3f}".format(yamnet_classes[i], prediction[i])
                for i in top5_i
            )
            self.update_text_signal.emit(result)

        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Zastava()
    application.show()
    thread = threading.Thread(target=application.update_audio)
    thread.start()
    sys.exit(app.exec_())
