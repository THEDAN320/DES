import sys
sys.path.insert(0, "libraly")
sys.path.insert(0, "ui")
sys.path.insert(0, "image")
    
import _DES

import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QTimer, QSize, Qt,QUrl
from PySide6.QtGui import QPixmap, QImage

from code import Ui_MainWindow

class apps(QMainWindow):
    def __init__(self):
        super(apps, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.des = _DES.DES()
        
        #connect buttons
        self.ui.encode_btn.clicked.connect(self.encode)
        self.ui.decode_btn.clicked.connect(self.decode)
        
    def encode(self):
        if len(self.ui.text_input_edit.toPlainText()) < 1 or len(self.ui.password_edit_1.text()) < 1:
            self.ui.code_output_edit.setText("enter text and password!")
            return
            
        self.des.encode(self.ui.text_input_edit.toPlainText().encode("utf-8"),self.ui.password_edit_1.text().encode("utf-8"))
        self.ui.code_output_edit.setText(self.des.m_code)
        string = "code - "+ self.des.m_code+ "\npassword - "+ _DES.sha256(self.ui.password_edit_1.text().encode("utf-8"))+"\n"
        with open("output.txt","w") as f:
            f.write(string)
        
    def decode(self):
        if len(self.ui.code_input_edit.toPlainText()) < 1 or len(self.ui.password_edit_2.text()) < 1:
            self.ui.text_output_edit.setText("enter text and password!")
            return
            
        self.des.decode(self.ui.code_input_edit.toPlainText().encode("utf-8"),self.ui.password_edit_2.text().encode("utf-8"))
        try:
            self.ui.text_output_edit.setText(self.des.code)
        except UnicodeDecodeError:
            self.ui.text_output_edit.setText("error convert byte to utf-8")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    window = apps()
    window.show()
    
    sys.exit(app.exec())
