import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class FastFood(qtw.QWidget):
    def __init__(self):
        # Initialize properties
        self.Oyna1OfW1 = None
        self.LaytOfOyna1OfW1 = None
        self.TitleW1 = None
        self.MainLayoutOfWindowOne = None

    def ShFastFood(self, name):
        # Adding a Window into the main layout
        self.Oyna1OfW1 = qtw.QWidget()
        self.Oyna1OfW1.setFixedSize(905, 40)
        self.Oyna1OfW1.setStyleSheet("""
            border-top-left-radius: 35px;
            border-top-right-radius: 35px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;                       
            """)

        # Creating Neasted Layout into first window of the main layout        
        self.LaytOfOyna1OfW1 = qtw.QVBoxLayout()

        # Remove spaces from the nested layout's sides and between windows in the nested layout
        self.LaytOfOyna1OfW1.setContentsMargins(0, 0, 0, 0)

        # Name of the Window
        self.TitleW1 = qtw.QPushButton(f"{name}")
        self.TitleW1.setStyleSheet("""color: black;
                                    background-color: #FFF1A7;
                                    border-top-left-radius: 0px;
                                    border-top-right-radius: 0px;
                                    border-bottom-left-radius: 25px;
                                    border-bottom-right-radius: 25px;  
                                   """)
        self.TitleW1.setFont(qtg.QFont("Calibri", 20, weight=100))
        self.TitleW1.setFixedSize(300, 40)

        # Add Button into the layput
        self.LaytOfOyna1OfW1.addWidget(self.TitleW1, alignment=qtc.Qt.AlignCenter)

        # Add the nested layout into the first Window
        self.Oyna1OfW1.setLayout(self.LaytOfOyna1OfW1)