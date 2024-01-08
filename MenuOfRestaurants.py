import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from FastFood import *
from meal1L1W1 import *
from ItmOfW5 import *
from FuncsOfItmsOfW5 import *

class Manu(qtw.QMainWindow, FastFood, Meal1L1W1, ItemsOfW5, FunctionsOfItemsOfW5):
    def __init__(self):
        super().__init__()

        # Your existing initialization code goes here...

        # Call the __init__ method of the base class (QMainWindow)
        qtw.QMainWindow.__init__(self)
        # Or you can use super() again:
        # super(Manu, self).__init__()

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

        # Adding Second Window into Main Windows
        self.WindowSecond()
        
        # Adding Third Window into Main Windows
        self.WindowThird()
        
        # Adding Four Window into Main Windows
        self.WindowFour()
        
        # Adding Five Window into Main Windows
        self.WindowFive()

        # Show the app
        self.show()
        
        # Initialize the components from the inherited classes
        FastFood.__init__(self)
        Meal1L1W1.__init__(self)
        ItemsOfW5.__init__(self)

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

        self.ShFastFood()        

        # Adding the window to the main layout
        self.MainLayoutOfWindowOne.addWidget(self.Oyna1OfW1)

        self.Oyna2OfW1 = qtw.QWidget()
        self.Oyna2OfW1.setStyleSheet("background-color: pink")

        # set a layput in the window of the mains of the first layout
        self.LaytOfMeansOfL1W1 = qtw.QHBoxLayout()

        # Remove spaces from the layout's sides and between windows in the layout
        self.LaytOfMeansOfL1W1.setSpacing(20)
        self.LaytOfMeansOfL1W1.setContentsMargins(0, 0, 0, 0)

        self.ShMeal1L1W1()

        self.tem = None
        self.tem = self.PulisT1L1W1.clicked.connect(self.AddToSum(124000, self.SumLabel.text()))
        self.SumLabel.setText(self.tem)

        # Adding the window to the main layout
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