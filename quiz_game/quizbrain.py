class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
    def next_question(self):
        current_question = self.question_list
        self.question_number +=1
        input(f"q.{self.question_number}:{current_question.text}(True/false)")
