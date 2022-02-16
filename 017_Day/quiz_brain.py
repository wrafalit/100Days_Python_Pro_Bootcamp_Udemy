class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)-1


    def next_question(self):
        q = self.question_list[self.question_number] # question from question_ban
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {q.text} (True/False)?: ")
        self.check_answer(user_answer, q.answer)

    def check_answer(self,answer_user, correct_answer):
        if answer_user.lower() == correct_answer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("You are wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number} \n")



