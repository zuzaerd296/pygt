from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton

# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow

class Window(QMainWindow):
    #Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt6 Lab')
        self.setGeometry(100, 100, 780, 580)
        self.createMenu()
        self.createTabs()
    
    
    # Funkcja dodająca pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)

        self.task1Menu = self.menu.addMenu("Task1")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionOpen = QAction('Open', self)
        self.actionOpen.setShortcut('Ctrl+G')
        self.actionOpen.triggered.connect(self.close)
        self.task1Menu.addAction(self.actionOpen)

        self.task2Menu = self.menu.addMenu("Task2")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionClear = QAction('Clear', self)
        self.actionClear.setShortcut('Ctrl+W')
        self.actionClear.triggered.connect(self.close)
        self.task2Menu.addAction(self.actionClear)
        self.actionOpen = QAction('Open', self)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.triggered.connect(self.close)
        self.task2Menu.addAction(self.actionOpen)
        self.actionSave = QAction('Save', self)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.triggered.connect(self.close)
        self.task2Menu.addAction(self.actionSave)
        self.actionSaveAs = QAction('Save as', self)
        self.actionSaveAs.setShortcut('Ctrl+K')
        self.actionSaveAs.triggered.connect(self.close)
        self.task2Menu.addAction(self.actionSaveAs)

        self.task3Menu = self.menu.addMenu("Task3")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionClear = QAction('Clear', self)
        self.actionClear.setShortcut('Ctrl+Q')
        self.actionClear.triggered.connect(self.close)
        self.task3Menu.addAction(self.actionClear)

    
    # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()
        
        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        
        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Task1")        
        self.tabs.addTab(self.tab_2, "Task2")        
        self.tabs.addTab(self.tab_3, "Task3")
        
        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)

    

    





# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()

