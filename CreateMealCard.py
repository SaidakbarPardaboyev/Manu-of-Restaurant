import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from ItmOfW5 import *

class MealCard(qtw.QMainWindow): 
    def __init__(self, name: str, price: str, imageURL: str):
        super().__init__()

        self.name = name
        self.price = price
        self.imageURL = imageURL
        self.setFixedSize(125, 175)
        self.setStyleSheet("""
                            color: red;
                            background-color: white;
                                    """)
        
        central_widget = qtw.QWidget(self)
        self.setCentralWidget(central_widget)

        cardlayout = qtw.QVBoxLayout(central_widget)
        cardlayout.setContentsMargins(0, 0, 0, 0)
        
        self.InnerWindow = qtw.QWidget()
        cardlayout.addWidget(self.InnerWindow)

        # create first mean
        self.Taom = qtw.QPushButton(self.InnerWindow)
        self.Taom.setGeometry(0, 0, 125, 175)
        self.Taom.setStyleSheet(f"""
                            QPushButton {{
                                    position: center;
                                    background-position: center;
                                    background-image: url({self.imageURL});
                                    border-top-left-radius: 30px;
                                    border-top-right-radius: 30px;
                                    border-bottom-left-radius: 30px;
                                    border-bottom-right-radius: 30px;
                                    }}
                                    """)
        
        self.Taom_Name = qtw.QLabel(f"{self.name}", self.Taom)
        self.Taom_Name.setStyleSheet("""
                                         color: black;
                                         """)
        self.Taom_Name.setGeometry(20, 90, 100, 50)
        self.Taom_Name.setFont(qtg.QFont("Calibri", 10, weight=100))

        self.Minus = qtw.QPushButton("-", self.InnerWindow)
        self.Minus.setGeometry(0, 145, 20, 30)
        self.Minus.setStyleSheet("""background-color: green;
            color: white;
            border-top-left-radius: 0px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 0px;""")
        self.Minus.setFont(qtg.QFont("Calobri", 10, weight=100))

        self.Shower_Number = qtw.QLabel("0", self.InnerWindow)
        self.Shower_Number.setAlignment(qtc.Qt.AlignCenter)
        self.Shower_Number.setGeometry(20, 145, 20, 30)
        self.Shower_Number.setStyleSheet("""background-color: green;
            color: white;
            """)
        self.Shower_Number.setFont(qtg.QFont("Calobri", 9, weight=100))

        
        self.Pulis = qtw.QPushButton("+", self.InnerWindow)
        self.Pulis.setGeometry(40, 145, 20, 30)
        self.Pulis.setStyleSheet("""background-color: green;
            color: white;
            border-top-left-radius: 0px;
            border-top-right-radius: 20px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;""")
        self.Pulis.setFont(qtg.QFont("Calobri", 10, weight=100))

        self.Taom_Price = qtw.QLabel(f"{self.price}", self.InnerWindow)
        self.Taom_Price.setGeometry(65, 145, 50, 30)
        self.Taom_Price.setAlignment(qtc.Qt.AlignCenter)
        self.Taom_Price.setFont(qtg.QFont("Calibri", 9, weight=100))
        self.Taom_Price.setStyleSheet("""
            background-color: white;
            color: black;
            border-top-left-radius: 0px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 30px;
                                        """)
        
        self.InnerWindow.show()