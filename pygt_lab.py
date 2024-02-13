from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QFileDialog, QLabel, QMainWindow, QStatusBar, QToolBar, QPlainTextEdit, QGridLayout, QPushButton, QMessageBox, QLineEdit, QSpinBox
from PyQt6.QtGui import QIcon, QAction, QPixmap

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Magic App')
        self.resize(680, 580)
        self.move(60, 15)
        self.createMenu()
        self.createTabs()
        self.currentFileName = ""
    
    def OpenImageFromFile(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self.tab_1, "Wybierz plik obrazu",  "Początkowa nazwa pliku", "JPG (*.jpg);; PNG (*.png)")
        if fileName:
            label = QLabel(self.tab_1)
            pixmap = QPixmap(fileName)
            label.setPixmap(pixmap)
            #self.resize(pixmap.width(),pixmap.height())
            label.show()
        return
    
    def NotepadOpen(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self.tab_1, "Wybierz plik tekstowy",  "Początkowa nazwa pliku", "TXT (*.txt)")
        if fileName:
            with open(fileName, 'r') as file:
                self.text_2.setPlainText(file.read())
                self.currentFileName = fileName
    
    def NotepadWyczysc(self):
        self.text_2.clear()

    def NotepadSave(self):
        if self.currentFileName is "":
            self.NotepadSaveAs()
            return
        else:
            fileName = self.currentFileName
            Text = self.text_2.toPlainText()
            with open(fileName, 'w') as file:
                file.write(Text)
                self.currentFileName = fileName

    def NotepadSaveAs(self):
        fileName, selectedFilter = QFileDialog.getSaveFileName(None,'SaveTextFile','/', "Text Files (*.txt)")
        Text = self.text_2.toPlainText()
        if fileName: 
            if not fileName.endswith(".txt"):
                fileName=fileName+".txt"
            with open(fileName, 'w') as file:
                file.write(Text)
                self.currentFileName = fileName

    def Task3Clear(self):
        self.text_31.clear()
        self.text_32.clear()
        self.number_33.clear()
        self.text_34.clear()

    def Task3Connect(self):
        self.text_34.setText(self.text_31.text()+self.text_32.text()+str(self.number_33.value()))

    def createMenu(self):
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu("File")
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)

        self.fileMenu1 = self.menu.addMenu("Task 1")
        self.actionTask1 = QAction('Open', self)
        self.actionTask1.setShortcut('Ctrl+1')
        self.actionTask1.triggered.connect(self.OpenImageFromFile)
        self.fileMenu1.addAction(self.actionTask1)

        self.fileMenu2 = self.menu.addMenu("Task 2")
        self.actionTask21 = QAction('Clear', self)
        self.actionTask21.setShortcut('Ctrl+W')
        self.actionTask21.triggered.connect(self.NotepadWyczysc)
        self.fileMenu2.addAction(self.actionTask21)
        self.actionTask22 = QAction('Open', self)
        self.actionTask22.setShortcut('Ctrl+2')
        self.actionTask22.triggered.connect(self.NotepadOpen)
        self.fileMenu2.addAction(self.actionTask22)
        self.actionTask23 = QAction('Save', self)
        self.actionTask23.setShortcut('Ctrl+S')
        self.actionTask23.triggered.connect(self.NotepadSave)
        self.fileMenu2.addAction(self.actionTask23)
        self.actionTask24 = QAction('Save as', self)
        self.actionTask24.setShortcut('Ctrl+K')
        self.actionTask24.triggered.connect(self.NotepadSaveAs)
        self.fileMenu2.addAction(self.actionTask24)

        self.fileMenu3 = self.menu.addMenu("Task 3")
        self.actionTask31 = QAction('Clear', self)
        self.actionTask31.setShortcut('Ctrl+3')
        self.actionTask31.triggered.connect(self.Task3Clear)
        self.fileMenu3.addAction(self.actionTask31)
    
    def createTabs(self):
        self.tabs = QTabWidget()
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        self.tabs.addTab(self.tab_1, "Pierwsza zakładka")        
        self.tabs.addTab(self.tab_2, "Druga zakładka")        
        self.tabs.addTab(self.tab_3, "Trzecia zakładka")
        self.setCentralWidget(self.tabs)
        self.text_2 = QPlainTextEdit()
        self.text_2.insertPlainText("Tutaj wpisz swój tekst.\n")
        self.text_2.resize(400,200)
        button_21 = QPushButton("Zapisz")
        button_21.clicked.connect(self.NotepadSave)
        button_22 = QPushButton("Wyczysc")
        button_22.clicked.connect(self.NotepadWyczysc)
        layout_2 = QGridLayout()
        layout_2.addWidget(self.text_2,0,0,1,0)
        layout_2.addWidget(button_21,1,0)
        layout_2.addWidget(button_22,1,1)
        self.tab_2.setLayout(layout_2)
        label_31 = QLabel("Pole A")
        label_32 = QLabel("Pole B")
        label_33 = QLabel("Pole C")
        label_34 = QLabel("Pole A + B + C")
        self.text_31 = QLineEdit()
        self.text_32 = QLineEdit()
        self.number_33 = QSpinBox()
        self.text_34 = QLineEdit()
        self.text_34.setReadOnly(True)
        self.text_31.textChanged.connect(self.Task3Connect)
        self.text_32.textChanged.connect(self.Task3Connect)
        self.number_33.valueChanged.connect(self.Task3Connect)
        layout_3 = QGridLayout()
        layout_3.addWidget(label_31,0,0)
        layout_3.addWidget(label_32,1,0)
        layout_3.addWidget(label_33,2,0)
        layout_3.addWidget(label_34,3,0)
        layout_3.addWidget(self.text_31,0,1)
        layout_3.addWidget(self.text_32,1,1)
        layout_3.addWidget(self.number_33,2,1)
        layout_3.addWidget(self.text_34,3,1)
        self.tab_3.setLayout(layout_3)

# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()