from django.db import models

# Create your models here.

class QuizQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_question = models.CharField(max_length=255)

    def __str__(self):
        return self.quiz_question

class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer_text_A = models.CharField(max_length=255, default="Answer Text")
    answer_text_B = models.CharField(max_length=255, default="Answer Text")
    answer_text_C = models.CharField(max_length=255, default="Answer Text")
    answer_text_D = models.CharField(max_length=255, default="Answer Text")
    letter = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return f"{self.question}.{self.answer_text_A}, {self.answer_text_B}, {self.answer_text_C}, {self.answer_text_D}"

class Game(models.Model):
    game_code = models.CharField(max_length=10, unique=True)
    host_name = models.CharField(max_length=50)
    questions = models.ManyToManyField('QuizQuestion')
    is_active = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)

class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nickname} - {self.game.game_code}, {self.score}"

class AnswerOrDrink(models.Model):
    id = models.AutoField(primary_key=True)
    AnswerOrDrinkQuestion = models.CharField(max_length=255)

    def __str__(self):
        return self.AnswerOrDrinkQuestion

class ChineseProverb(models.Model):
    ChineseProverb = models.CharField(max_length=255)

    def __str__(self):
        return self.ChineseProverb

