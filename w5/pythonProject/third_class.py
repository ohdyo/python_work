from data import question_data
from question_model import Question
from quiz_bran import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("-----------")
print("모든 문제를 풀었습니다.")
print(f"최종 점수는 {quiz.score}/{len(quiz.question_list)} 입니다.")