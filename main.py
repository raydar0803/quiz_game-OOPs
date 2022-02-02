from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_over = False;
while quiz.still_has_questions() and not quiz_over:
    quiz.next_question()
    choice = input("Do you want to continue the quiz? Type 'yes' or 'no'. ")
    print('\n')
    if choice == "no":
        quiz_over = True

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
