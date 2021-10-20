from turtle import Turtle

ALIGNMENT = "center"
FONT = 20

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/justa/vscode/udemy/100 days of code/day 20_day 21 snake/snakeGame/data.txt") as data:
            self.high_score = int(data.read())
            print(self.high_score)

        self.penup()
        self.goto(x = 0, y = 280)
        self.color("white")
        self.hideturtle()     
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score is {self.score}. Your high score is: {self.high_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(x = 0, y = 0)
    #     self.write(f"Game over. Your score was: {self.score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:/Users/justa/vscode/udemy/100 days of code/day 20_day 21 snake/snakeGame/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
