import html

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
        q_text_html = html.unescape(q.text)
        return [ q_text_html, q.answer]
        # print(f"{self.question_number}: {q_text_html} ")
        # return f"{self.question_number}: {q_text_html} "
        # user_answer = input(f"Q{self.question_number}: {q_text_html} (True/False)?: ")
        # self.check_answer(user_answer, q.answer)

    def check_answer(self,answer_user, correct_answer):
        if answer_user.lower() == correct_answer.lower():
            self.score +=1
            return True
        else:
            return False