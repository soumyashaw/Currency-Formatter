from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

def formatting(amount):                                            #Formatting Process
    amt = str(abs(amount)).split('.')
    whole = amt[0][::-1]
    list_amt = []
    for i in range(1,len(whole)+1):
        list_amt.append(whole[i-1])
        if (i%3==0) & (i!=len(whole)):
            list_amt.append(',')
    formatted_amt = ""
    formatted_amt = formatted_amt.join(list_amt[::-1])
    formatted_amt = formatted_amt + "." + amt[1][0:2]
    if(len(amt[1])==1):
        formatted_amt = formatted_amt + "0"
    
    if(amount<0):
        return("-$" + formatted_amt)
    else:
        return("$" + formatted_amt)

def onButtonClick():                                                     #On Click of 'Format' Button 
    answer.hide()
    text = amount.text()
    try:
        ans = formatting(float(text))
    except:
        ans = "NaN"
    answer.setText(str(ans))
    answer.show()

def DarkTheme():                                                          #Dark Theme
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

if __name__ == '__main__':
    app = QApplication([])                                            # 1. Instantiate ApplicationContext
    window = QWidget()
    window.setWindowIcon(QIcon('Icon.ico'))
    DarkTheme()
    window.resize(200,250)
    window.move(600,200)
    window.setWindowTitle("Curency Formatter")        # 2. App Title
    app.setStyle('Fusion')
    title = QLabel('Currency Formatter $',window)
    title.setFont(QFont("Times", 10, QFont.Bold))
    title.move(25,15)
    label = QLabel('Amount',window)
    label.move(25,45)
    amount = QLineEdit(window)                               # 3. Input from User
    amount.move(25,75)
    button = QPushButton('Format',window)              # 4. Formatting Command
    button.move(25,115)
    button.clicked.connect(onButtonClick)
    answer = QLabel(window)                                     # 5. Resulting Answer
    answer.move(25,150)
    window.show()
    exit_code = app.exec_()                                           # 6. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
