from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMAGE_PATH = "100 days of code//day 34//Quizzler_app//images//true.png"
FALSE_IMAGE_PATH = "100 days of code//day 34//Quizzler_app//images//false.png"
FONT = ('Arial', 20, 'italic')


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)

        self.score_label = Label(text = f"Score: {self.score}", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some question", 
            fill = THEME_COLOR, 
            font = FONT
        )
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady=50)

        true_button_img = PhotoImage(file=TRUE_IMAGE_PATH)
        false_button_img = PhotoImage(file=FALSE_IMAGE_PATH)

        print(true_button_img)

        self.true_button = Button(
            image = true_button_img, 
            highlightthickness=0, 
            bg = THEME_COLOR, 
            bd= 0, 
            command = self.true_pressed
        )
        self.true_button.grid(row = 2, column = 0)

        self.false_button = Button(
            image = false_button_img, 
            highlightthickness=0, 
            bg = THEME_COLOR, 
            bd= 0, 
            command = self.false_pressed
        )
        self.false_button.grid(row = 2, column = 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        # if self.quiz.check_answer("True"):
        #     self.score += 1
        # self.canvas.itemconfig(self.score_label, text=f"Score: {score}")

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text = f"Score: {self.score}", fg = "white", bg = THEME_COLOR)
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)