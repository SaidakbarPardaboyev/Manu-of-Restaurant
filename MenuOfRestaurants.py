import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from FastFood import *
import CreateMealCard
from ItmOfW5 import *
from FuncsOfItmsOfW5 import *

class Manu(qtw.QMainWindow, FastFood, ItemsOfW5, FunctionsOfItemsOfW5):
    def __init__(self):
        super().__init__()
        qtw.QMainWindow.__init__(self)

        # Create nested Windows in the main Window
        self.Window1 = qtw.QWidget(self)
        self.Window2 = qtw.QWidget(self)
        self.Window3 = qtw.QWidget(self)
        self.Window4 = qtw.QWidget(self)
        self.Window5 = qtw.QWidget(self)

        self.setStyleSheet("background-color: #FF3672")
        self.resize(1930, 990)
        self.move(0,0)
        # self.setMaximumSize(1880, 940)
        # self.setMinimumSize(1880, 940)

        # Adding First Window into Main Windows
        self.WindowOne()
        self.WindowSecond()
        self.WindowThird()
        self.WindowFour()
        self.WindowFive()

        # Show the app
        self.show()

    def WindowOne(self):
        # give size and shape to the first window
        self.Window1.setGeometry(20, 20, 905, 430)
        # self.Window1.setMaximumSize(600, 500)
        # self.Window1.setMinimumSize(600, 500)
        self.Window1.setStyleSheet("""
                                    background-color: #1C317A; 
                                    border-radius: 50px;
                                    """)

        # Creating A main layout into WindowOne
        self.MainLayoutOfWindowOne = qtw.QVBoxLayout(self.Window1)

        # Remove spaces from the main layout's sides and between windows in the main layout
        self.MainLayoutOfWindowOne.setSpacing(0)
        self.MainLayoutOfWindowOne.setContentsMargins(0, 0, 0, 0)

        self.ShFastFood()      

        # Adding the window to the main layout
        self.MainLayoutOfWindowOne.addWidget(self.Oyna1OfW1)

        self.Oyna2OfW1 = qtw.QWidget()
        self.Oyna2OfW1.setStyleSheet("background-color: pink")
        # set a layout in the window of the mains of the first layout
        self.LaytOfMeansOfL1W1 = qtw.QHBoxLayout(self.Oyna2OfW1)
        # Remove spaces from the layout's sides and between windows in the layout
        # self.LaytOfMeansOfL1W1.setSpacing(20)
        # self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal1 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", "C:/Users/user/Desktop/MANU of Restaurants/Lavash.png")
        self.LaytOfMeansOfL1W1.addWidget(self.Meal1)
        self.Meal1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal1.Taom_Price.text(), self.Meal1))
        self.Meal1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal1.Taom_Price.text(), self.Meal1))
        
        # self.Meal2 = CreateMealCard.Meal1L1W1()
        # self.LaytOfMeansOfL1W1.addWidget(self.Meal2)
        # self.Meal2.PulisT1L1W1.clicked.connect(lambda: self.PilusAll(self.Meal2.Taom1L1W1Price.text(), self.Meal2))

        # self.Meal3 = CreateMealCard.Meal1L1W1()
        # self.LaytOfMeansOfL1W1.addWidget(self.Meal3)
        # self.Meal3.PulisT1L1W1.clicked.connect(lambda: self.PilusAll(self.Meal3.Taom1L1W1Price.text(), self.Meal3))

        # self.Meal4 = CreateMealCard.Meal1L1W1()
        # self.LaytOfMeansOfL1W1.addWidget(self.Meal4)
        # self.Meal4.PulisT1L1W1.clicked.connect(lambda: self.PilusAll(self.Meal4.Taom1L1W1Price.text(), self.Meal4))

        # self.Meal5 = CreateMealCard.Meal1L1W1()
        # self.LaytOfMeansOfL1W1.addWidget(self.Meal5)
        # self.Meal5.PulisT1L1W1.clicked.connect(lambda: self.PilusAll(self.Meal5.Taom1L1W1Price.text(), self.Meal5))

        # self.Meal6 = CreateMealCard.Meal1L1W1()
        # self.LaytOfMeansOfL1W1.addWidget(self.Meal6)
        # self.Meal6.PulisT1L1W1.clicked.connect(lambda: self.PilusAll(self.Meal6.Taom1L1W1Price.text(), self.Meal6))

        self.MainLayoutOfWindowOne.addWidget(self.Oyna2OfW1)
        # Do not call show() here if you want to manage when to show the windows


    def WindowSecond(self):

        # self.layOut1W1 = qtw.QVBoxLayout()
        # self.Window1.setLayout(self.layOut1W1)
        self.Window2.setGeometry(955, 20, 905, 430)
        # self.Window1.setMaximumSize(600, 500)
        # self.Window1.setMinimumSize(600, 500)
        self.Window2.setStyleSheet("background-color: #1C317A; border-radius: 50px")

    def WindowThird(self):

        # self.layOut1W1 = qtw.QVBoxLayout()
         # self.Window1.setLayout(self.layOut1W1)
        self.Window3.setGeometry(20, 480, 905, 430)
        # self.Window1.setMaximumSize(600, 500)
        # self.Window1.setMinimumSize(600, 500)
        self.Window3.setStyleSheet("background-color: #1C317A; border-radius: 50px")
    
    def WindowFour(self):

        # self.layOut1W1 = qtw.QVBoxLayout()
        # self.Window1.setLayout(self.layOut1W1)
        self.Window4.setGeometry(955, 480, 905, 430)
        # self.Window1.setMaximumSize(600, 500)
        # self.Window1.setMinimumSize(600, 500)
        self.Window4.setStyleSheet("background-color: #1C317A; border-radius: 50px")
    
    def WindowFive(self):

        # self.layOut1W1 = qtw.QVBoxLayout()
        # self.Window1.setLayout(self.layOut1W1)
        self.Window5.setGeometry(20, 920, 1840, 50)
        # self.Window5.setMaximumSize(1840, 50)
        # self.Window5.setMinimumSize(1840, 50)
        self.Window5.setStyleSheet("""
                                   background-color: #1C317A;
                                   border-radius: 25px;
                                   """)
        
        # Creating A main layout into WindowOne
        self.MainLayoutOfWindowFive = qtw.QHBoxLayout()
        
        # Remove spaces from the main layout's sides and between windows in the main layout
        self.MainLayoutOfWindowFive.setSpacing(200)
        self.MainLayoutOfWindowFive.setContentsMargins(0, 0, 0, 0)

        self.ShItemsOfW5()

        self.Window5.setLayout(self.MainLayoutOfWindowFive)

    def PilusAll(self, newSumma: str, Obj: object):
        self.AddToSum(newSumma)
        self.AddOnetoTheLabel(Obj)
        self.AddOneToBuyurtSoni()

    def MinutAll(self, newSumma: str, Obj: object):
        self.DeletFromSum(newSumma)
        self.DeleteOneFromTheLabel(Obj)
        self.DeleteOneFromBuyurtSoni()

    def AddToSum(self, newSumma: str):
        VariForAddSumma = self.SumLabel.text()
        VariForAddSumma = VariForAddSumma[:-4]
        VariForAddSumma = VariForAddSumma.replace(" ", "")
        tem = newSumma
        tem = tem.replace(' ', '')
        VariForAddSumma = str(int(VariForAddSumma) + int(tem))
        VariForAddSumma = VariForAddSumma[::-1]
        # self.VariForAddSumma = ' '.join(self.VariForAddSumma[i:i+3] for i in range(0, len(self.VariForAddSumma), 3))

        new_text = VariForAddSumma[::-1] + ' som'
        self.SumLabel.setText(new_text)

    def AddOnetoTheLabel(self, Obj: object):
        Obj.Shower_Number.setText(str(int(Obj.Shower_Number.text()) + 1))

    def AddOneToBuyurtSoni(self):
        self.CountOfMealsOrdered.setText("Buyurtmalar soni: " + str(int(self.CountOfMealsOrdered.text()[18:]) + 1))

    def DeletFromSum(self, newSumma: str):
        VariForAddSumma = self.SumLabel.text()
        VariForAddSumma = VariForAddSumma[:-4]
        VariForAddSumma = int(VariForAddSumma.replace(" ", ""))
        tem = newSumma
        tem = int(tem.replace(' ', ''))
        if VariForAddSumma - tem >= 0:
            VariForAddSumma = str(int(VariForAddSumma) - tem)
            VariForAddSumma = VariForAddSumma[::-1]

            new_text = str(VariForAddSumma)[::-1] + ' som'
            self.SumLabel.setText(new_text)

    def DeleteOneFromTheLabel(self, Obj: object):
        tem = int(Obj.Shower_Number.text())
        if tem > 0:
            Obj.Shower_Number.setText(str(tem - 1))
        else:
            self.ShowErrorMessageBox()

    def DeleteOneFromBuyurtSoni(self):
        tem = int(self.CountOfMealsOrdered.text()[18:])
        if tem > 0:
            self.CountOfMealsOrdered.setText("Buyurtmalar soni: " + str(tem - 1))

    def ShowErrorMessageBox(self):
        MesBox = qtw.QMessageBox()
        MesBox.setWindowTitle("Buyurtnami bekir qilish xatosi")
        MesBox.setIcon(qtw.QMessageBox.Critical)

        MesBox.setText("Buyurtmalar sonini\nkamaytirishda xato\nqildingiz.")
        MesBox.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        MesBox.setDefaultButton(qtw.QMessageBox.Ok)
        
        responce = MesBox.exec_()


app = qtw.QApplication([])
manu = Manu()
app.exec_()