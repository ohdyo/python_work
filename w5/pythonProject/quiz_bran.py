class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (True/False) : ")
        self.check_anser(user_answer, current_question.answer)
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def check_anser(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("정답입니다! :)")
            print(f"지금까지 접수는 {self.score}/{len(self.question_list)}")
        else :
            print("틀렸습니다. :(")
            print(f"정답은 {question_answer} 입니다.")
            print(f"지금까지 접수는 {self.score}/{len(self.question_list)}")
