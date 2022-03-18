from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain_my: QuizBrain):
        self.quiz_brain_my = quiz_brain_my

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height= 250)
        self.canvas.grid(column=0, row=1,columnspan=2, pady=30)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text",
            font=("Arial", 15, "italic"))

        right_button_image = PhotoImage(file="./images/true.png")
        self.button_right = Button(image=right_button_image,
                                   highlightthickness=0,
                                   command=self.true_answer)

        self.button_right.grid(column=0, row=2)

        false_button_image = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=false_button_image,
                                   highlightthickness=0,
                                   command=self.false_answer)
        self.button_false.grid(column=1, row=2)

        self.label = Label(text="Score: 0", background= THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text_answer = self.quiz_brain_my.next_question()
        q_text = q_text_answer[0]
        self.correct_answer = q_text_answer[1]
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_answer(self):
        print(self.quiz_brain_my.next_question())
        self.give_feedback(self.quiz_brain_my.check_answer("true", self.correct_answer))

    def false_answer(self):
        print(self.quiz_brain_my.next_question())
        is_right = self.quiz_brain_my.check_answer("false", self.correct_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
