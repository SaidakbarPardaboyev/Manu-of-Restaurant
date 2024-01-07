import PyQt5.QtWidgets as qtw
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

        self.setStyleSheet("background-color: #231E1E")
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

        # self.layOut1W1 = qtw.QVBoxLayout()
        # self.Window1.setLayout(self.layOut1W1)
        self.Window1.setGeometry(10, 10, 905, 460)
        # self.Window1.setMaximumSize(600, 500)
        # self.Window1.setMinimumSize(600, 500)
        self.Window1.setStyleSheet("background-color: #1C317A; border-radius: 50px")

        # Name of the Window
        self.TitleW1 = qtw.QPushButton("Fast Food", self.Window1)
        self.TitleW1.setGeometry(320, 0, 300, 30)
        self.TitleW1.setStyleSheet("color: black; background-color: #FFFFFF; border-radius: 15px")
        self.TitleW1.setFont(qtg.QFont("Calibri", 15))

        # create first mean
        self.Taom1W1 = qtw.QPushButton(self.Window1)
        self.Taom1W1.setGeometry(20, 50, 125, 175)
        self.Taom1W1.setStyleSheet("""background-color: white; border-radius: 100px
                                   border-bottom-left-radius: 5px;
                                   border-bottom-right-radius: 5px;""")

        # Set the image as the icon of the button
        self.Taom1W1.setStyleSheet("""
            QPushButton {
                background-image: url("C:/Users/user/Desktop/MANU of Restaurants/Lavash11.png");
                background-position: center;
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
            }
        """)

        self.Taom1W1Name = qtw.QLabel("Mol go'shili\nLavash", self.Taom1W1)
        self.Taom1W1Name.setStyleSheet("color: black; background-color: white;")
        self.Taom1W1Name.setGeometry(20, 90, 100, 50)
        self.Taom1W1Name.setFont(qtg.QFont("Calibri", 10, weight=100))

        self.Taom1W1ningCountButton = qtw.QPushButton(self.Window1)
        self.Taom1W1ningCountButton.setGeometry(20, 195, 60, 30)
        self.Taom1W1ningCountButton.setStyleSheet("background-color: green")

        self.Taom1W1Price = qtw.QLabel("24 000", self.Window1)
        self.Taom1W1Price.setGeometry(90, 195, 50, 30)
        self.Taom1W1Price.setFont(qtg.QFont("Calibri", 8))
        self.Taom1W1Price.setStyleSheet("background-color: white; color: black")
        

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
        self.Window3.setGeometry(10, 490, 905, 460)
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
        # self.background_label.setPixmap(background_image)