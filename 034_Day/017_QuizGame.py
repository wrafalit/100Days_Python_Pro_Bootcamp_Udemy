from question_model import Question
from data import question_data
from  quiz_brain import QuizBrain
from  ui import QuizInterface

question_bank = []
for item in question_data:
    # print(item['text'])
    # print(item['answer'])
    question_bank.append(Question(item['text'], item['answer']))


quiz_brain_my = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_brain_my)

# while quiz_brain_my.still_has_questions():
#     quiz_brain_my.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz_brain_my.score}/{quiz_brain_my.question_number }")