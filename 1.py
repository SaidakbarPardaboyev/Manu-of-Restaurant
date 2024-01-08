import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class AnimatedButton(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Animated Button')

        # Create a button
        self.button = QPushButton('Click me!', self)
        self.button.clicked.connect(self.animateButton)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.show()

    def animateButton(self):
        # Create a property animation for the button's geometry
        animation = QPropertyAnimation(self.button, b"geometry")

        # Define the start and end values for the animation
        start_rect = QRect(self.button.geometry())
        end_rect = QRect(self.button.geometry().x(), self.button.geometry().y(),
                         self.button.geometry().width() + 50, self.button.geometry().height() + 10)

        # Set the start and end values for the animation
        animation.setStartValue(start_rect)
        animation.setEndValue(end_rect)

        # Set the duration of the animation in milliseconds
        animation.setDuration(500)

        # Start the animation
        animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AnimatedButton()
    sys.exit(app.exec_())
