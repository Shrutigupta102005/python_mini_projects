from question_model import question
from data import question_data
from quiz_brain import QuizBrain 

question_bank = []
for i in question_data:
    qtext = i["text"]
    atext = i["answer"]
    ques = question(qtext,atext)
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
quiz.next_question()
