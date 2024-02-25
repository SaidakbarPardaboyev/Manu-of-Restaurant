import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from FastFood import *
import CreateMealCard
from ItmOfW5 import *
from FuncsOfItmsOfW5 import *
import pathlib

class Manu(qtw.QMainWindow, FastFood, ItemsOfW5, FunctionsOfItemsOfW5):
    def __init__(self):
        super().__init__()
        qtw.QMainWindow.__init__(self)

        self.path = str(pathlib.Path().resolve() / "/")
        
        # Create nested Windows in the main Window
        self.Window1 = qtw.QWidget(self)
        self.Window2 = qtw.QWidget(self)
        self.Window3 = qtw.QWidget(self)
        self.Window4 = qtw.QWidget(self)
        self.Window5 = qtw.QWidget(self)

        self.setStyleSheet("background-color: #FFF1A7;")
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
        self.Window1.setGeometry(20, 20, 905, 430)
        self.Window1.setStyleSheet("""
                                    background-color: #D5FFC6; 
                                    border-radius: 50px;
                                    """)

        # Creating A main layout into WindowOne
        self.MainLayoutOfWindowOne = qtw.QVBoxLayout(self.Window1)

        # Remove spaces from the main layout's sides and between windows in the main layout
        self.MainLayoutOfWindowOne.setSpacing(0)
        self.MainLayoutOfWindowOne.setContentsMargins(0, 0, 0, 0)

        self.ShFastFood("Fast Food")        

        # Adding the window to the main layout
        self.MainLayoutOfWindowOne.addWidget(self.Oyna1OfW1)

        self.Oyna2OfW1 = qtw.QWidget()
        # set a layout in the window of the mains of the first layout
        self.LaytOfMeansOfL1W1 = qtw.QHBoxLayout(self.Oyna2OfW1)
        # Remove spaces from the layout's sides and between windows in the layout
        # self.LaytOfMeansOfL1W1.setSpacing(20)
        # self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal1OfW1 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL1W1.addWidget(self.Meal1OfW1)
        self.Meal1OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal1OfW1.Taom_Price.text(), self.Meal1OfW1))
        self.Meal1OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal1OfW1.Taom_Price.text(), self.Meal1OfW1))

        self.Meal2OfW1 = CreateMealCard.MealCard("Tovuq go'shtli\nTrindvich", "24 000", f"{self.path}Trindvich.png")
        self.LaytOfMeansOfL1W1.addWidget(self.Meal2OfW1)
        self.Meal2OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal2OfW1.Taom_Price.text(), self.Meal2OfW1))
        self.Meal2OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal2OfW1.Taom_Price.text(), self.Meal2OfW1))
        
        self.Meal3OfW1 = CreateMealCard.MealCard("Mol go'shili\nShaurma", "22 000", f"{self.path}Shaurma.png")
        self.LaytOfMeansOfL1W1.addWidget(self.Meal3OfW1)
        self.Meal3OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal3OfW1.Taom_Price.text(), self.Meal3OfW1))
        self.Meal3OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal3OfW1.Taom_Price.text(), self.Meal3OfW1))
        
        self.Meal4OfW1 = CreateMealCard.MealCard("Gamgurger", "39 000", f"{self.path}Gamburger.png")
        self.LaytOfMeansOfL1W1.addWidget(self.Meal4OfW1)
        self.Meal4OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal4OfW1.Taom_Price.text(), self.Meal4OfW1))
        self.Meal4OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal4OfW1.Taom_Price.text(), self.Meal4OfW1))
        
        self.Meal5OfW1 = CreateMealCard.MealCard("Hot-Dog\nDabl", "22 000", f"{self.path}Hot-Dog Dabl.png")
        self.LaytOfMeansOfL1W1.addWidget(self.Meal5OfW1)
        self.Meal5OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal5OfW1.Taom_Price.text(), self.Meal5OfW1))
        self.Meal5OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal5OfW1.Taom_Price.text(), self.Meal5OfW1))

        self.MainLayoutOfWindowOne.addWidget(self.Oyna2OfW1)


        self.Oyna3OfW1 = qtw.QWidget()
        # set a layout in the window of the mains of the first layout
        self.LaytOfMeansOfL2W1 = qtw.QHBoxLayout(self.Oyna3OfW1)
        # Remove spaces from the layout's sides and between windows in the layout
        # self.LaytOfMeansOfL1W1.setSpacing(20)
        # self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal6OfW1 = CreateMealCard.MealCard("Hot-Dog\nMini", "9 000", f"{self.path}Hot-Dog Mini.png")
        self.LaytOfMeansOfL2W1.addWidget(self.Meal6OfW1)
        self.Meal6OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal6OfW1.Taom_Price.text(), self.Meal6OfW1))
        self.Meal6OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal6OfW1.Taom_Price.text(), self.Meal6OfW1))

        self.Meal7OfW1 = CreateMealCard.MealCard("Sub mol\ngo'shtidan", "20 000", f"{self.path}Sub mol goshtidan.png")
        self.LaytOfMeansOfL2W1.addWidget(self.Meal7OfW1)
        self.Meal7OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal7OfW1.Taom_Price.text(), self.Meal7OfW1))
        self.Meal7OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal7OfW1.Taom_Price.text(), self.Meal7OfW1))
        
        self.Meal8OfW1 = CreateMealCard.MealCard("tovuq go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL2W1.addWidget(self.Meal8OfW1)
        self.Meal8OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal8OfW1.Taom_Price.text(), self.Meal8OfW1))
        self.Meal8OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal8OfW1.Taom_Price.text(), self.Meal8OfW1))
        
        self.Meal9OfW1 = CreateMealCard.MealCard("Chizburger", "23 000", f"{self.path}Gamburger.png")
        self.LaytOfMeansOfL2W1.addWidget(self.Meal9OfW1)
        self.Meal9OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal9OfW1.Taom_Price.text(), self.Meal9OfW1))
        self.Meal9OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal9OfW1.Taom_Price.text(), self.Meal9OfW1))
        
        self.Meal10OfW1 = CreateMealCard.MealCard("Mol go'shili\nShaurma", "22 000", f"{self.path}Shaurma.png")
        self.LaytOfMeansOfL2W1.addWidget(self.Meal10OfW1)
        self.Meal10OfW1.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal10OfW1.Taom_Price.text(), self.Meal10OfW1))
        self.Meal10OfW1.Minus.clicked.connect(lambda: self.MinutAll(self.Meal10OfW1.Taom_Price.text(), self.Meal10OfW1))

        self.MainLayoutOfWindowOne.addWidget(self.Oyna3OfW1)


    def WindowSecond(self):
        self.Window2.setGeometry(955, 20, 905, 430)
        self.Window2.setStyleSheet("background-color: #D5FFC6; border-radius: 50px")
        
        # Creating A main layout into WindowOne
        self.MainLayoutOfWindowSecond = qtw.QVBoxLayout(self.Window2)

        # Remove spaces from the main layout's sides and between windows in the main layout
        self.MainLayoutOfWindowSecond.setSpacing(0)
        self.MainLayoutOfWindowSecond.setContentsMargins(0, 0, 0, 0)

        self.ShFastFood("Disertlar")        

        # Adding the window to the main layout
        self.MainLayoutOfWindowSecond.addWidget(self.Oyna1OfW1)

        self.Oyna2OfW2 = qtw.QWidget()
        # set a lay2out in the window of the mains of the first layout
        self.LaytOfMeansOfL1W2 = qtw.QHBoxLayout(self.Oyna2OfW2)
        # Remove spaces from the layout's sides and between 2windows in the layout
        # self.LaytOfMeansOfL1W1.setSpacing(20)
        # self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal1OfW2 = CreateMealCard.MealCard("Mevali Donut", "16 000", f"{self.path}Mevali Donut.png")
        self.LaytOfMeansOfL1W2.addWidget(self.Meal1OfW2)
        self.Meal1OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal1OfW2.Taom_Price.text(), self.Meal1OfW2))
        self.Meal1OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal1OfW2.Taom_Price.text(), self.Meal1OfW2))

        self.Meal2OfW2 = CreateMealCard.MealCard("Medovik", "17 000", f"{self.path}Medovik.png")
        self.LaytOfMeansOfL1W2.addWidget(self.Meal2OfW2)
        self.Meal2OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal2OfW2.Taom_Price.text(), self.Meal2OfW2))
        self.Meal2OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal2OfW2.Taom_Price.text(), self.Meal2OfW2))
        
        self.Meal3OfW2 = CreateMealCard.MealCard("Chizkeyk", "17 000", f"{self.path}hizkeyk.png")
        self.LaytOfMeansOfL1W2.addWidget(self.Meal3OfW2)
        self.Meal3OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal3OfW2.Taom_Price.text(), self.Meal3OfW2))
        self.Meal3OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal3OfW2.Taom_Price.text(), self.Meal3OfW2))
        
        self.Meal4OfW2 = CreateMealCard.MealCard("Ponchik Karamelli", "16 000", f"{self.path}Ponchik Karamelli.png")
        self.LaytOfMeansOfL1W2.addWidget(self.Meal4OfW2)
        self.Meal4OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal4OfW2.Taom_Price.text(), self.Meal4OfW2))
        self.Meal4OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal4OfW2.Taom_Price.text(), self.Meal4OfW2))
        
        self.Meal5OfW2 = CreateMealCard.MealCard("Chizkeyk", "17 000", f"{self.path}hizkeyk.png")
        self.LaytOfMeansOfL1W2.addWidget(self.Meal5OfW2)
        self.Meal5OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal5OfW2.Taom_Price.text(), self.Meal5OfW2))
        self.Meal5OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal5OfW2.Taom_Price.text(), self.Meal5OfW2))

        self.MainLayoutOfWindowSecond.addWidget(self.Oyna2OfW2)

        # The following line should have the same indentation level as the line above
        self.Oyna3OfW2 = qtw.QWidget()
        # set a layout in the window of the mains of the first layout
        self.LaytOfMeansOfL2W2 = qtw.QHBoxLayout(self.Oyna3OfW2)
        # Remove spaces from the layout's sides and between windows in the layout
        # self.LaytOfMeansOfL1W1.setSpacing(20)
        # self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal6OfW2 = CreateMealCard.MealCard("Chizkeyk", "17 000", f"{self.path}hizkeyk.png")
        self.LaytOfMeansOfL2W2.addWidget(self.Meal6OfW2)
        self.Meal6OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal6OfW2.Taom_Price.text(), self.Meal6OfW2))
        self.Meal6OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal6OfW2.Taom_Price.text(), self.Meal6OfW2))

        self.Meal7OfW2 = CreateMealCard.MealCard("Ponchik Karamelli", "16 000", f"{self.path}Ponchik Karamelli.png")
        self.LaytOfMeansOfL2W2.addWidget(self.Meal7OfW2)
        self.Meal7OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal7OfW2.Taom_Price.text(), self.Meal7OfW2))
        self.Meal7OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal7OfW2.Taom_Price.text(), self.Meal7OfW2))
        
        self.Meal8OfW2 = CreateMealCard.MealCard("Mevali Donut", "16 000", f"{self.path}Mevali Donut.png")
        self.LaytOfMeansOfL2W2.addWidget(self.Meal8OfW2)
        self.Meal8OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal8OfW2.Taom_Price.text(), self.Meal8OfW2))
        self.Meal8OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal8OfW2.Taom_Price.text(), self.Meal8OfW2))
        
        self.Meal9OfW2 = CreateMealCard.MealCard("Chizkeyk", "17 000", f"{self.path}hizkeyk.png")
        self.LaytOfMeansOfL2W2.addWidget(self.Meal9OfW2)
        self.Meal9OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal9OfW2.Taom_Price.text(), self.Meal9OfW2))
        self.Meal9OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal9OfW2.Taom_Price.text(), self.Meal9OfW2))
        
        self.Meal10OfW2 = CreateMealCard.MealCard("Mevali Donut", "16 000", f"{self.path}Mevali Donut.png")
        self.LaytOfMeansOfL2W2.addWidget(self.Meal10OfW2)
        self.Meal10OfW2.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal10OfW2.Taom_Price.text(), self.Meal10OfW2))
        self.Meal10OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal10OfW2.Taom_Price.text(), self.Meal10OfW2))

        self.MainLayoutOfWindowSecond.addWidget(self.Oyna3OfW2)

    def WindowThird(self):
        self.Window3.setGeometry(20, 480, 905, 430)
        self.Window3.setStyleSheet("background-color: #D5FFC6; border-radius: 50px")

        # Creating A main layout into WindowOne
        self.MainLayoutOfWindowThird = qtw.QVBoxLayout(self.Window3)

        # Remove spaces from the main layout's sides and between windows in the main layout
        self.MainLayoutOfWindowThird.setSpacing(0)
        self.MainLayoutOfWindowThird.setContentsMargins(0, 0, 0, 0)

        self.ShFastFood("Milliy Taomlar")        

        # Adding the window to the main layout
        self.MainLayoutOfWindowThird.addWidget(self.Oyna1OfW1)

        self.Oyna2OfW3 = qtw.QWidget()
        # set a lay2out in the window of the mains of the first layout
        self.LaytOfMeansOfL1W3 = qtw.QHBoxLayout(self.Oyna2OfW3)
        # Remove spaces from the layout's sides and between 2windows in the layout

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal1OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL1W3.addWidget(self.Meal1OfW3)
        self.Meal1OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal1OfW3.Taom_Price.text(), self.Meal1OfW3))
        self.Meal1OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal1OfW3.Taom_Price.text(), self.Meal1OfW3))

        self.Meal2OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL1W3.addWidget(self.Meal2OfW3)
        self.Meal2OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal2OfW3.Taom_Price.text(), self.Meal2OfW3))
        self.Meal2OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal2OfW3.Taom_Price.text(), self.Meal2OfW3))
        
        self.Meal3OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL1W3.addWidget(self.Meal3OfW3)
        self.Meal3OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal3OfW3.Taom_Price.text(), self.Meal3OfW3))
        self.Meal3OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal3OfW3.Taom_Price.text(), self.Meal3OfW3))
        
        self.Meal4OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL1W3.addWidget(self.Meal4OfW3)
        self.Meal4OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal4OfW3.Taom_Price.text(), self.Meal4OfW3))
        self.Meal4OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal4OfW3.Taom_Price.text(), self.Meal4OfW3))
        
        self.Meal5OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL1W3.addWidget(self.Meal5OfW3)
        self.Meal5OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal5OfW3.Taom_Price.text(), self.Meal5OfW3))
        self.Meal5OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal5OfW3.Taom_Price.text(), self.Meal5OfW3))

        self.MainLayoutOfWindowThird.addWidget(self.Oyna2OfW3)

        # The following line should have the same indentation level as the line above
        self.Oyna3OfW3 = qtw.QWidget()
        # set a layout in the window of the mains of the first layout
        self.LaytOfMeansOfL2W3 = qtw.QHBoxLayout(self.Oyna3OfW3)
        # Remove spaces from the layout's sides and between windows in the layout

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal6OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL2W3.addWidget(self.Meal6OfW3)
        self.Meal6OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal6OfW3.Taom_Price.text(), self.Meal6OfW3))
        self.Meal6OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal6OfW3.Taom_Price.text(), self.Meal6OfW3))

        self.Meal7OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL2W3.addWidget(self.Meal7OfW3)
        self.Meal7OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal7OfW3.Taom_Price.text(), self.Meal7OfW3))
        self.Meal7OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal7OfW3.Taom_Price.text(), self.Meal7OfW3))
        
        self.Meal8OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL2W3.addWidget(self.Meal8OfW3)
        self.Meal8OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal8OfW3.Taom_Price.text(), self.Meal8OfW3))
        self.Meal8OfW2.Minus.clicked.connect(lambda: self.MinutAll(self.Meal8OfW3.Taom_Price.text(), self.Meal8OfW3))
        
        self.Meal9OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL2W3.addWidget(self.Meal9OfW3)
        self.Meal9OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal9OfW3.Taom_Price.text(), self.Meal9OfW3))
        self.Meal9OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal9OfW3.Taom_Price.text(), self.Meal9OfW3))
        
        self.Meal10OfW3 = CreateMealCard.MealCard("Mol go'shili\nLavash", "25 000", f"{self.path}Lavash.png")
        self.LaytOfMeansOfL2W3.addWidget(self.Meal10OfW3)
        self.Meal10OfW3.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal10OfW3.Taom_Price.text(), self.Meal10OfW3))
        self.Meal10OfW3.Minus.clicked.connect(lambda: self.MinutAll(self.Meal10OfW3.Taom_Price.text(), self.Meal10OfW3))

        self.MainLayoutOfWindowThird.addWidget(self.Oyna3OfW3)
    
    def WindowFour(self):
        self.Window4.setGeometry(955, 480, 905, 430)
        self.Window4.setStyleSheet("background-color: #D5FFC6; border-radius: 50px")
        
        # Creating A main layout into WindowOne
        self.MainLayoutOfWindowFour = qtw.QVBoxLayout(self.Window4)

        # Remove spaces from the main layout's sides and between windows in the main layout
        self.MainLayoutOfWindowFour.setSpacing(0)
        self.MainLayoutOfWindowFour.setContentsMargins(0, 0, 0, 0)

        self.ShFastFood("Ichimliklar")        

        # Adding the window to the main layout
        self.MainLayoutOfWindowFour.addWidget(self.Oyna1OfW1)

        self.Oyna2OfW4 = qtw.QWidget()
        # set a lay2out in the window of the mains of the first layout
        self.LaytOfMeansOfL1W4 = qtw.QHBoxLayout(self.Oyna2OfW4)
        # Remove spaces from the layout's sides and between 2windows in the layout

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal1OfW4 = CreateMealCard.MealCard("7up Razliv", "25 000", f"{self.path}Razliv.png")
        self.LaytOfMeansOfL1W4.addWidget(self.Meal1OfW4)
        self.Meal1OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal1OfW4.Taom_Price.text(), self.Meal1OfW4))
        self.Meal1OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal1OfW4.Taom_Price.text(), self.Meal1OfW4))

        self.Meal2OfW4 = CreateMealCard.MealCard("kofe", "5 000", f"{self.path}kofe.png")
        self.LaytOfMeansOfL1W4.addWidget(self.Meal2OfW4)
        self.Meal2OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal2OfW4.Taom_Price.text(), self.Meal2OfW4))
        self.Meal2OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal2OfW4.Taom_Price.text(), self.Meal2OfW4))
        
        self.Meal3OfW4 = CreateMealCard.MealCard("Pepsi razliv", "9 000", f"{self.path}Pepsi razliv.png")
        self.LaytOfMeansOfL1W4.addWidget(self.Meal3OfW4)
        self.Meal3OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal3OfW4.Taom_Price.text(), self.Meal3OfW4))
        self.Meal3OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal3OfW4.Taom_Price.text(), self.Meal3OfW4))
        
        self.Meal4OfW4 = CreateMealCard.MealCard("Moxito", "12 000", f"{self.path}Moxito.png")
        self.LaytOfMeansOfL1W4.addWidget(self.Meal4OfW4)
        self.Meal4OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal4OfW4.Taom_Price.text(), self.Meal4OfW4))
        self.Meal4OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal4OfW4.Taom_Price.text(), self.Meal4OfW4))
        
        self.Meal5OfW4 = CreateMealCard.MealCard("Pepsi 0.5", "10 000", f"{self.path}Pepsi.png")
        self.LaytOfMeansOfL1W4.addWidget(self.Meal5OfW4)
        self.Meal5OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal5OfW4.Taom_Price.text(), self.Meal5OfW4))
        self.Meal5OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal5OfW4.Taom_Price.text(), self.Meal5OfW4))

        self.MainLayoutOfWindowFour.addWidget(self.Oyna2OfW4)

        # The following line should have the same indentation level as the line above
        self.Oyna3OfW4 = qtw.QWidget()
        # set a layout in the window of the mains of the first layout
        self.LaytOfMeansOfL2W4 = qtw.QHBoxLayout(self.Oyna3OfW4)
        # Remove spaces from the layout's sides and between windows in the layout

        # Create and add instances of Meal1L1W1 to the layout
        self.Meal6OfW4 = CreateMealCard.MealCard("Mirinda razliv", "9 000", f"{self.path}Mirinda razliv.png")
        self.LaytOfMeansOfL2W4.addWidget(self.Meal6OfW4)
        self.Meal6OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal6OfW4.Taom_Price.text(), self.Meal6OfW4))
        self.Meal6OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal6OfW4.Taom_Price.text(), self.Meal6OfW4))

        self.Meal7OfW4 = CreateMealCard.MealCard("Kichik sok", "3 000", f"{self.path}Kichik sok.png")
        self.LaytOfMeansOfL2W4.addWidget(self.Meal7OfW4)
        self.Meal7OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal7OfW4.Taom_Price.text(), self.Meal7OfW4))
        self.Meal7OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal7OfW4.Taom_Price.text(), self.Meal7OfW4))
        
        self.Meal8OfW4 = CreateMealCard.MealCard("7up Razliv", "25 000", f"{self.path}Razliv.png")
        self.LaytOfMeansOfL2W4.addWidget(self.Meal8OfW4)
        self.Meal8OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal8OfW4.Taom_Price.text(), self.Meal8OfW4))
        self.Meal8OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal8OfW4.Taom_Price.text(), self.Meal8OfW4))
        
        self.Meal9OfW4 = CreateMealCard.MealCard("kofe", "5 000", f"{self.path}kofe.png")
        self.LaytOfMeansOfL2W4.addWidget(self.Meal9OfW4)
        self.Meal9OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal9OfW4.Taom_Price.text(), self.Meal9OfW4))
        self.Meal9OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal9OfW4.Taom_Price.text(), self.Meal9OfW4))
        
        self.Meal10OfW4 = CreateMealCard.MealCard("Mirinda razliv", "9 000", f"{self.path}Mirinda razliv.png")
        self.LaytOfMeansOfL2W4.addWidget(self.Meal10OfW4)
        self.Meal10OfW4.Pulis.clicked.connect(lambda: self.PilusAll(self.Meal10OfW4.Taom_Price.text(), self.Meal10OfW4))
        self.Meal10OfW4.Minus.clicked.connect(lambda: self.MinutAll(self.Meal10OfW4.Taom_Price.text(), self.Meal10OfW4))

        self.MainLayoutOfWindowFour.addWidget(self.Oyna3OfW4)

    def WindowFive(self):

        # self.layOut1W1 = qtw.QVBoxLayout()
        # self.Window1.setLayout(self.layOut1W1)
        self.Window5.setGeometry(20, 920, 1840, 50)
        # self.Window5.setMaximumSize(1840, 50)
        # self.Window5.setMinimumSize(1840, 50)
        self.Window5.setStyleSheet("""
                                   background-color: #FFF1A7;
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
        self.DeletFromSum(newSumma, Obj)
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

    def DeletFromSum(self, newSumma: str, Obj: object):
        VariForAddSumma = self.SumLabel.text()
        VariForAddSumma = VariForAddSumma[:-4]
        VariForAddSumma = int(VariForAddSumma.replace(" ", ""))
        tem = newSumma
        tem = int(tem.replace(' ', ''))
        if VariForAddSumma - tem >= 0 and int(Obj.Shower_Number.text()) != 0:
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