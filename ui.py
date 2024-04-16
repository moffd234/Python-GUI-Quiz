from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI:
    def __init__(self, qb: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # Sets up padding and background color
        self.quiz = qb

        # Canvas
        self.canvas = Canvas(background="white", width=300, height=250, highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, font=FONT, fill="black", width=280)
        # Labels
        self.score_label = Label(bg=THEME_COLOR, text=f"Score = {self.quiz.score}", highlightbackground=THEME_COLOR)

        # Buttons
        false_img = PhotoImage(file="./images/false.png")
        correct_img = PhotoImage(file="./images/true.png")
        self.wrong_button = Button(padx=0, pady=0, image=false_img, highlightbackground=THEME_COLOR,
                                   command=self.false_pressed)
        self.right_button = Button(padx=0, pady=0, image=correct_img, highlightbackground=THEME_COLOR,
                                   command=self.true_pressed)

        """
                0            1
          --------------|--------------
        0|              |  SCORE(L)
          --------------|--------------
        1|   CANVAS ----|--->>>>>>>>
          --------------|--------------
        2|  RIGHT(B)    |   WRONG(B)
        """

        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()  # Gets first question
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="false"))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="true"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
