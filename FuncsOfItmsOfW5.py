import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class FunctionsOfItemsOfW5():
    def __init__(self):
        self.VariForAddSumma = None

    def AddToSum(self, newSumma: int, oldSumma):
        self.VariForAddSumma = oldSumma[:-3]
        self.VariForAddSumma.replace(' ', '')
        self.VariForAddSumma = str(int(self.VariForAddSumma) + newSumma)
        self.VariForAddSumma = self.VariForAddSumma[::-1]
        self.VariForAddSumma = ' '.join(self.VariForAddSumma[i:i+3] for i in range(0, len(self.VariForAddSumma), 3))
        self.VariForAddSumma = self.VariForAddSumma[::-1] + ' som'
        
        return self.VariForAddSumma
