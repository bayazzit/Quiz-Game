from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

playing = True
quiz = QuizBrain(question_bank)

while playing:
    if quiz.still_has_question():
        answer = quiz.next_question()
        if answer in ['exit', 'quit', 'off']:
            playing = False
    else:
        playing = False
