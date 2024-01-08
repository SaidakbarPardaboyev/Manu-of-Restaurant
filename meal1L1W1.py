import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from FuncsOfItmsOfW5 import *

class Meal1L1W1(qtw.QWidget, FunctionsOfItemsOfW5):
    def __init__(self):
        super().__init__()

        qtw.QWidget.__init__(self)

        # Initialize properties
        self.WindForFirstMealOfL1W1 = None
        self.Taom1L1W1 = None
        self.Taom1L1W1Name = None
        self.MinutT1L1W1 = None
        self.ShowerNumberT1L1W1 = None
        self.PulisT1L1W1 = None
        self.Taom1L1W1Price = None

    def ShMeal1L1W1(self):
        # Creating a window for the first meal
        self.WindForFirstMealOfL1W1 = qtw.QWidget()

        # create first mean
        self.Taom1L1W1 = qtw.QPushButton(self.WindForFirstMealOfL1W1)
        self.Taom1L1W1.setGeometry(20, 10, 125, 175)
        self.Taom1L1W1.setStyleSheet("""
                                    background-position: center;
                                    background-image: url("C:/Users/user/Desktop/MANU of Restaurants/Lavash.png");
                                    border-top-left-radius: 30px;
                                    border-top-right-radius: 30px;
                                    border-bottom-left-radius: 30px;
                                    border-bottom-right-radius: 30px;
                                    """)
        
        self.Taom1L1W1Name = qtw.QLabel("Mol go'shili\nLavash", self.Taom1L1W1)
        self.Taom1L1W1Name.setStyleSheet("""
                                         color: black;
                                         """)
        self.Taom1L1W1Name.setGeometry(20, 90, 100, 50)
        self.Taom1L1W1Name.setFont(qtg.QFont("Calibri", 10, weight=100))

        self.MinutT1L1W1 = qtw.QPushButton("-", self.WindForFirstMealOfL1W1)
        self.MinutT1L1W1.setGeometry(20, 155, 20, 30)
        self.MinutT1L1W1.setStyleSheet("""background-color: green;
            color: white;
            border-top-left-radius: 0px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 0px;""")
        self.MinutT1L1W1.setFont(qtg.QFont("Calobri", 10, weight=100))

        self.ShowerNumberT1L1W1 = qtw.QLabel('<div align="center">0</div>', self.WindForFirstMealOfL1W1)
        self.ShowerNumberT1L1W1.setGeometry(40, 155, 20, 30)
        self.ShowerNumberT1L1W1.setStyleSheet("""background-color: green;
            color: white;
            """)
        self.ShowerNumberT1L1W1.setFont(qtg.QFont("Calobri", 9, weight=100))

        
        self.PulisT1L1W1 = qtw.QPushButton("+", self.WindForFirstMealOfL1W1)
        self.PulisT1L1W1.setGeometry(60, 155, 20, 30)
        self.PulisT1L1W1.setStyleSheet("""background-color: green;
            color: white;
            border-top-left-radius: 0px;
            border-top-right-radius: 20px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;""")
        self.PulisT1L1W1.setFont(qtg.QFont("Calobri", 10, weight=100))

        self.Taom1L1W1Price = qtw.QLabel("124 000", self.WindForFirstMealOfL1W1)
        self.Taom1L1W1Price.setGeometry(85, 155, 50, 30)
        self.Taom1L1W1Price.setFont(qtg.QFont("Calibri", 9, weight=100))
        self.Taom1L1W1Price.setStyleSheet("""
            background-color: white;
            color: black;
            border-top-left-radius: 0px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 30px;
                                        """)

        self.LaytOfMeansOfL1W1.addWidget(self.WindForFirstMealOfL1W1)

        self.Oyna2OfW1.setLayout(self.LaytOfMeansOfL1W1)