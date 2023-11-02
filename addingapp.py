#this is made with pyqt5



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QDateEdit, QDateTimeEdit, QAbstractSpinBox, QCalendarWidget
from PyQt5.QtCore import QSortFilterProxyModel, Qt, QDate, QTime
from PyQt5.QtGui import QIcon

class DataEntryApp(QWidget):
    def __init__(self):

        #window description
        super().__init__()
        self.setWindowTitle('Store Details')
        self.setWindowIcon(QIcon('906310.ico'))
        self.setMinimumWidth(1200)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.setLayout(self.layout)

        self.model = QStandardItemModel()
        subLayouts = {}

        subLayouts['DateTime'] = QHBoxLayout()
        self.layout.addLayout(subLayouts['DateTime'])

        labelDate = QLabel('Requirements Date: ')
        self.lineEditDate = QDateEdit()
        self.lineEditDate.setCalendarPopup(True)

        #alignment of the date widget
        subLayouts['DateTime'].addWidget(labelDate, 0, alignment=Qt.AlignLeft)
        subLayouts['DateTime'].addWidget(self.lineEditDate, 3)

        # row 2
        subLayouts[2] = QHBoxLayout()
        self.layout.addLayout(subLayouts[2])

        # Material codes
        self.comboCodes = QComboBox()
        subLayouts[2].addWidget(QLabel('Material Code: '), alignment = Qt.AlignRight)
        subLayouts[2].addWidget(self.comboCodes, 1)
        self.comboCodes.setFont(QFont('', 12))
        self.comboCodes.setModel(self.model)

        # Material names/description
        self.combonames = QComboBox()
        subLayouts[2].addWidget(QLabel('Material Description: '), alignment=Qt.AlignRight)
        subLayouts[2].addWidget(self.combonames, 3)
        self.combonames.setFont(QFont('', 12))
        self.combonames.setModel(self.model)



        # add data as key value pairs
        for k, v in data.items():
            Codes = QStandardItem(k)
            self.model.appendRow(Codes)
            for value in v:
                names = QStandardItem(value)
                Codes.appendRow(names)

        #calling update function
        self.comboCodes.currentIndexChanged.connect(self.updateCodesCombo)
        self.updateCodesCombo(0)

    #to update the selected value according to the key value pair
    def updateCodesCombo(self, index):
        indx = self.model.index(index, 0, self.comboCodes.rootModelIndex())
        self.combonames.setRootModelIndex(indx)
        self.combonames.setCurrentIndex(0)


data = {
    '8100041585': ['PENCIL ERASER PLASTIC SMALL'], '2100766458': ['ACTUATOR, DFC-1120'],'2100782005': ['ALUMINIUM TAPE,SELF ADHESSIVE,50 MMX30M'],'8100055481': ['ARC SUIT, CAT-2/8-CAL/CM2 P/N-8-CAL'], '2100219188': ['ASSY,FLSH BK ART FOR LPG RGLTR;BRS;ESAB'], '2200066831': ['BATT,DRY CELL,PNCL,1.5 VDC,STD,AAA 1.5V'], '2200145002': ['BATTERY ( 6F22 ),9 VOLT'], '4200010508': ['BATTERY OF AA SIZE, 1.5Volt, NICKEL-CADM'], '2200093187': ['BATTERY,PENCIL CELL,AAA,1.5V'], '8100033567': ['BETADINE OINTMENT']
}

if __name__== '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
                      QWidget {
                        font-size: 20px;
                      }
                    ''')
    myApp = DataEntryApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
