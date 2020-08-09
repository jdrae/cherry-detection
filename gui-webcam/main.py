from PyQt5.QtWidgets import QApplication

from device import Camera
from gui import StartWindow


app = QApplication([])
start_window = StartWindow()
start_window.show()
app.exit(app.exec_())