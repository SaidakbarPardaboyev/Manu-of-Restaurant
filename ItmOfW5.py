import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class ItemsOfW5(qtw.QWidget):
    def __init__(self):
        self.CountOfMealsOrdered = None
        self.OrderButton = None
        self.SumLabel = None
        self.VariForAddSumma = None
        self.responce = None

    def ShItemsOfW5(self):
        # Creating Label for counting the number of the ordered meals
        self.CountOfMealsOrdered = qtw.QLabel("Buyurtmalar soni: 0")
        self.CountOfMealsOrdered.setAlignment(qtc.Qt.AlignCenter)
        self.CountOfMealsOrdered.setStyleSheet("""
                                                background-color: white;
                                                color: black;
                                                background-position: center;
                                                """)
        self.CountOfMealsOrdered.setFont(qtg.QFont("Calibri", 25))

        self.MainLayoutOfWindowFive.addWidget(self.CountOfMealsOrdered)

        # Creating A button to order meals
        self.OrderButton = qtw.QPushButton("Buyurtma berish", clicked= self.MesBoxForOrder)
        self.OrderButton.setStyleSheet("""
                                        background-color: white;
                                        color: black;
                                        background-position: center;
                                        """)
        self.OrderButton.setFont(qtg.QFont("Calibri", 25))

        self.MainLayoutOfWindowFive.addWidget(self.OrderButton)

        # Creating a label for showing the price of all the ordered meals
        self.SumLabel = qtw.QLabel("0 som")
        self.SumLabel.setAlignment(qtc.Qt.AlignCenter)
        self.SumLabel.setStyleSheet("""
                                    background-color: white;
                                    color: black;
                                    background-position: center;
                                    """)
        self.SumLabel.setFont(qtg.QFont("Montserrot", 20, weight=80))

        self.MainLayoutOfWindowFive.addWidget(self.SumLabel)

    def MesBoxForOrder(self):
        tem = self.CountOfMealsOrdered.text()[18:].replace(" ", "")
        if int(tem) > 0:
            MesBox = qtw.QMessageBox()
            MesBox.setWindowTitle("Buyurtma berish")
            MesBox.setIcon(qtw.QMessageBox.Information)

            MesBox.setText("Buyurtmangiz muvaffaqiyatli qabul qilindi.\nBuyurtmangiz yarim soat ishida\nyetkazib beriladi.\nBiz bilan hamkorlik qilganingiz uchun\nraxmat.")
            MesBox.setStandardButtons(qtw.QMessageBox.Ok)
            MesBox.setDefaultButton(qtw.QMessageBox.Ok)

            self.responce = MesBox.exec_()