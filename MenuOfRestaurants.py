import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class Manu(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create nested Windows in the main Window
        self.Window1 = qtw.QWidget(self)
        self.Window2 = qtw.QWidget(self)
        self.Window3 = qtw.QWidget(self)
        self.Window4 = qtw.QWidget(self)
        # self.Window5 = qtw.QWidget(self)

        self.setStyleSheet("background-color: #FF3672")
        self.resize(1930, 990)
        self.move(0,0)
        # self.setMaximumSize(1880, 940)
        # self.setMinimumSize(1880, 940)

        # Adding First Window into Main Windows
        self.WindowOne()

        # Adding Second Window into Main Windows
        self.WindowSecond()
        
        # Adding Third Window into Main Windows
        self.WindowThird()
        
        # Adding Four Window into Main Windows
        self.WindowFour()
        
        # # Adding Five Window into Main Windows
        # self.WindowFive()

        # Show the app
        self.show()

        # all Properties
        # self.layOut1W1 = None
        

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

        # Adding a Window into the main layout
        self.Oyna1OfW1 = qtw.QWidget()
        self.Oyna1OfW1.setFixedSize(905, 50)
        self.Oyna1OfW1.setStyleSheet("""
            border-top-left-radius: 35px;
            border-top-right-radius: 35px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;                       
            background-color: #1C317;
            """)

        # Creating Neasted Layout into first window of the main layout        
        self.LaytOfOyna1OfW1 = qtw.QVBoxLayout()

        # Remove spaces from the nested layout's sides and between windows in the nested layout
        self.LaytOfOyna1OfW1.setContentsMargins(0, 0, 0, 0)

        # Name of the Window
        self.TitleW1 = qtw.QPushButton("Fast Food")#, self.LaytOfOyna1OfW1)
        self.TitleW1.setStyleSheet("""color: black;
                                    background-color: #FF3672;
                                    border-top-left-radius: 0px;
                                    border-top-right-radius: 0px;
                                    border-bottom-left-radius: 25px;
                                    border-bottom-right-radius: 25px;  
                                   """)
        self.TitleW1.setFont(qtg.QFont("Calibri", 20, weight=100))
        self.TitleW1.setFixedSize(300, 50)

        # Add Button into the layput
        self.LaytOfOyna1OfW1.addWidget(self.TitleW1, alignment=qtc.Qt.AlignCenter)

        # Add the nested layout into the first Window
        self.Oyna1OfW1.setLayout(self.LaytOfOyna1OfW1)

        # Adding the window to the main layout
        self.MainLayoutOfWindowOne.addWidget(self.Oyna1OfW1)
        
        self.Oyna2OfW1 = qtw.QWidget()
        self.Oyna2OfW1.setStyleSheet("background-color: pink")

        # set a layput in the window of the mains of the first layout
        self.LaytOfMeansOfL1W1 = qtw.QHBoxLayout()


        # Creating a window for the first meal
        self.WindForFirstMealOfL1W1 = qtw.QWidget()

        # Remove spaces from the layout's sides and between windows in the layout
        self.LaytOfMeansOfL1W1.setSpacing(20)
        self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

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
        self.Taom1L1W1Name.setStyleSheet("color: black;")
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
        
        self.MainLayoutOfWindowOne.addWidget(self.Oyna2OfW1)
        


    def PulisMinusT1W1(self):
        pass


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
    
    # def WindowFive(self):

    #     # self.layOut1W1 = qtw.QVBoxLayout()
    #     # self.Window1.setLayout(self.layOut1W1)
    #     self.Window5.setGeometry(20, 880, 1880, 50)
    #     self.Window5.setMaximumSize(1840, 50)
    #     self.Window5.setMinimumSize(1840, 50)
    #     self.Window5.setStyleSheet("background-color: red")



app = qtw.QApplication([])
manu = Manu()
app.exec_()


        # # Set the background image using a QLabel
        # self.background_label = qtw.QLabel(self)
        # self.background_label.setGeometry(0, 0, 1880, 940)
        # background_image = qtg.QPixmap("C:/Users/user/Desktop/MANU of Restaurants/bb.png")
    


    # def animateButton(self,name):
    #     # Create a property animation for the button's geometry
    #     animation = qtw.QPropertyAnimation(name, b"geometry")

    #     # Define the start and end values for the animation
    #     start_rect = qtc.QRect(name.geometry())
    #     end_rect = qtc.QRect(name.geometry().x(), name.geometry().y(),
    #                      name.geometry().width() + 50, name.geometry().height() + 10)

    #     # Set the start and end values for the animation
    #     animation.setStartValue(start_rect)
    #     animation.setEndValue(end_rect)

    #     # Set the duration of the animation in milliseconds
    #     animation.setDuration(500)

    #     # Start the animation
    #     animation.start()    
        # self.background_label.setPixmap(background_image)



        # self.Taom1W1ningCountButton = qtw.QPushButton(self.Window1)
        # self.Taom1W1ningCountButton.setStyleSheet("""
        #     background-color: green;
        #     border-top-left-radius: 0px;
        #     border-top-right-radius: 20px;
        #     border-bottom-left-radius: 20px;
        #     border-bottom-right-radius: 0px;
        # """)
        # self.Taom1W1ningCountButton.setGeometry(20, 195, 60, 30)