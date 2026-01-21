from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents = int(file.read())
        self.highscore = contents
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()


    def update_score(self):
        self.clear()
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.highscore):
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()