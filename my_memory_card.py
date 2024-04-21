#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QLabel, QPushButton,
QRadioButton, QHBoxLayout,QVBoxLayout, QGroupBox, QButtonGroup)
from random import shuffle, randint

score = 0
total = 0

class Question():
    def __init__(self, question, r_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.r_ans = r_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    rb_group.hide()
    ans_group.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    ans_group.hide()
    rb_group.show()
    btn_ok.setText('Ответить')
    RadioBtnG.setExclusive(False)
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    RadioBtnG.setExclusive(True)

# def start_test():
#     if btn_ok.text() == 'Ответить':
#         show_result()
#     else:
#         show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.r_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.r_ans)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    global score
    if answers[0].isChecked():
        score += 1
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    
    print(f'Статистика:\n-Всего вопросов: {total}\n-Правильных ответов: {score}\n-Рейтинг: {score/total*100}%')
        
def next_question():
    global total
    total += 1
    cur_question = randint(0, len(questions_list)-1)
    
    while cur_question in mw.temp:
        cur_question = randint(0, len(questions_list)-1)
    mw.temp.append(cur_question)
    
    if len(mw.temp) == len(questions_list):
        mw.temp = [cur_question]
    
    q = questions_list[cur_question]
    ask(q)

    

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

questions_list = []
questions_list.append(Question('Государственный язык Бразилия', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Как назывался особый головной убор, который носили фараоны в Древнем Египте?','Немес', 'Картуз', 'Корона', 'Убрус'))
questions_list.append(Question('У какого животного самые большие глаза относительно тела?', 'У долгопята', 'У лемура', 'У летучей мыши', 'У тупайи'))
questions_list.append(Question('Как называли строителя в старину?', 'Зодчий', 'Бондарь', 'Бортник', 'Кормчий'))
questions_list.append(Question('Какое из этих растений — плотоядное?', 'Росянка', 'Володушка', 'Мытник', 'Астрагал'))

memory_card = QApplication([])
mw = QWidget()

mw.temp = []
#mw.cur_question = -1

question = QLabel('Вопрос')
rb_group = QGroupBox('Варианты ответов')
rb1 = QRadioButton('ответ 1')
rb2 = QRadioButton('ответ 2')
rb3 = QRadioButton('ответ 3')
rb4 = QRadioButton('ответ 4')

answers = [rb1, rb2, rb3, rb4]

RadioBtnG = QButtonGroup()
RadioBtnG.addButton(rb1)
RadioBtnG.addButton(rb2)
RadioBtnG.addButton(rb3)
RadioBtnG.addButton(rb4)

l12 = QVBoxLayout()
l34 = QVBoxLayout()
group_l = QHBoxLayout()
l12.addWidget(rb1)
l12.addWidget(rb2)
l34.addWidget(rb3)
l34.addWidget(rb4)
group_l.addLayout(l12)
group_l.addLayout(l34)
rb_group.setLayout(group_l)

ans_group = QGroupBox('Результат теста')
lb_result = QLabel('Правильно/Неправильно')
lb_correct= QLabel('верный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignCenter))
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)
ans_group.setLayout(layout_res)

btn_ok = QPushButton('Ответить')
btn_ok.clicked.connect(click_OK)

layout_q = QHBoxLayout()
layout_g = QHBoxLayout()
layout_b = QHBoxLayout()

layout_q.addWidget(question)
layout_g.addWidget(rb_group)
ans_group.hide()
layout_g.addWidget(ans_group)
layout_b.addStretch(1)
layout_b.addWidget(btn_ok, stretch=2)
layout_b.addStretch(1)

main_l = QVBoxLayout()

main_l.addLayout(layout_q, stretch=2)
main_l.addLayout(layout_g, stretch=8)
main_l.addStretch(1)
main_l.addLayout(layout_b, stretch=1)
main_l.addStretch(1)
main_l.setSpacing(5)

mw.setLayout(main_l)
mw.setWindowTitle('Memory Card')
mw.resize(600, 500)
next_question()
mw.show()
memory_card.exec_()