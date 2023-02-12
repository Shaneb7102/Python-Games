from question_model import Question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []

for questions in question_data:
    question_text = (questions['question'])
    question_answer = (questions['correct_answer'])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain(question_bank)

quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()
print("Congratulations! You have completed the quiz!")
print(f"You're final score was {quiz.score}/{len(question_bank)} ")


