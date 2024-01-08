import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class ItemsOfW5(qtw.QWidget):
    def __init__(self):
        self.CountOfMealsOrdered = None
        self.OrderButton = None
        self.ShoSum = None

    def ShItemsOfW5(self):
        # Creating Label for counting the number of the ordered meals
        self.CountOfMealsOrdered = qtw.QLabel('<div align="center">Buyurtmalar soni: 0</div>')
        self.CountOfMealsOrdered.setStyleSheet("""
                                                background-color: white;
                                                color: black;
                                                background-position: center;
                                                """)
        self.CountOfMealsOrdered.setFont(qtg.QFont("Calibri", 25))

        self.MainLayoutOfWindowFive.addWidget(self.CountOfMealsOrdered)

        # Creating A button to order meals
        self.OrderButton = qtw.QPushButton("Buyurtma berish")
        self.OrderButton.setStyleSheet("""
                                        background-color: white;
                                        color: black;
                                        background-position: center;
                                        """)
        self.OrderButton.setFont(qtg.QFont("Calibri", 25))

        self.MainLayoutOfWindowFive.addWidget(self.OrderButton)

        # Creating a label for showing the price of all the ordered meals
        self.ShoSum = qtw.QLabel('<div align="center"> 155 000 som</div>')
        self.ShoSum.setStyleSheet("""
                                                background-color: white;
                                                color: black;
                                                background-position: center;
                                                """)
        self.ShoSum.setFont(qtg.QFont("Montserrot", 20, weight=80))

        self.MainLayoutOfWindowFive.addWidget(self.ShoSum)


        
