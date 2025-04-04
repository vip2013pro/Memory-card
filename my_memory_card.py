#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup, QMessageBox
from random import shuffle
class Question():
    def __init__(self, questions, s_true1, s_wrong2, s_wrong3, s_wrong4):
        self.questions = questions
        self.s_true1 = s_true1
        self.s_wrong2 = s_wrong2
        self.s_wrong3 = s_wrong3
        self.s_wrong4 = s_wrong4
application = QApplication([])
window = QWidget()
window.setFixedSize(400, 300)
question = QLabel('Сколько на улице голубей?')
variable = QGroupBox('голуби')
s_variable1 = QRadioButton('2')
s_variable2 = QRadioButton('250')
s_variable3 = QRadioButton('около 0')
s_variable4 = QRadioButton('5')
button = QPushButton('ответ')
line = QVBoxLayout()
lineV = QVBoxLayout()
lineH = QHBoxLayout()
line.addWidget(s_variable1, alignment = Qt.AlignLeft)
line.addWidget(s_variable2, alignment = Qt.AlignLeft)
lineV.addWidget(s_variable3, alignment = Qt.AlignLeft)
lineV.addWidget(s_variable4, alignment = Qt.AlignLeft)
lineH.addLayout(line)
lineH.addLayout(lineV)
variable.setLayout(lineH)
rightanswear = QGroupBox('ы')
rightanswear.hide()
right = QLabel('ы')
left = QLabel('ы')
lineVV = QVBoxLayout()
lineVV.addWidget(right, alignment = Qt.AlignLeft)
lineVV.addWidget(left, alignment = Qt.AlignCenter)
rightanswear.setLayout(lineVV)
lineVVV = QVBoxLayout()
lineVVV.addWidget(question, alignment = Qt.AlignCenter)
lineVVV.addWidget(variable)
lineVVV.addWidget(rightanswear)
lineVVV.addWidget(button, alignment = Qt.AlignCenter)
window.setLayout(lineVVV)
btngroup = QButtonGroup()
btngroup.addButton(s_variable1)
btngroup.addButton(s_variable2)
btngroup.addButton(s_variable3)
btngroup.addButton(s_variable4)
answears = [s_variable1, s_variable2, s_variable3, s_variable4]
def show_result():
    variable.hide()
    rightanswear.show()
    button.setText('Следующий вопрос')

def show_question():
    rightanswear.hide()
    variable.show()
    button.setText('Ответить')
    btngroup.setExclusive(False)
    s_variable1.setChecked(False)
    s_variable2.setChecked(False)
    s_variable3.setChecked(False)
    s_variable4.setChecked(False)
    btngroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        show_result()
        check_answear()
    else:
        show_question()
        next_question()

    

def ask(quesask:Question):
    shuffle(answears)
    answears[0].setText(quesask.s_true1)
    answears[1].setText(quesask.s_wrong2)
    answears[2].setText(quesask.s_wrong3)
    answears[3].setText(quesask.s_wrong4)
    left.setText(quesask.s_true1)
    question.setText(quesask.questions)
    

def check_answear():
    if answears[0].isChecked():
        global countofrightanswears
        right.setText('Правильно')
    else:
        right.setText('Неправильно')
    if answears[0].isChecked():
        countofrightanswears += 1
    
    
countofrightanswears = 0   
cur_question = 0

def next_question():
    global cur_question, countofrightanswears
    if cur_question >= len(questions1) - 1:
        final()
        cur_question = 0
        countofrightanswears = 0
    else:
        cur_question += 1
    question = questions1[cur_question]
    ask(question) 






questions1 = [
    Question('Сколько вам лет?', '-1', '1', '0', '144'),
    Question('Сколько мне лет?', '-1', '1', '0', '144'),
    Question('Сколько лет?', '-1', '1', '0', '144'),
    Question('?', '-1', '1', '0', '144')
]
quesask = Question('ы1', 'ы2', 'ы3', 'ы4', 'ы5')
ask(questions1[cur_question])
button.clicked.connect(start_test)  
def final():
    result = QMessageBox()
    formula = countofrightanswears / len(questions1) * 100
    result.setText(f'Поздавляем! Кол-во ваших правильных ответов:{formula}%')
    result.exec_()















window.show()
application.exec_()
















