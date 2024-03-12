from django.contrib import admin
from .models import QuizAnswer
from .models import QuizQuestion
from .models import Game
from .models import Player
from .models import AnswerOrDrink
from .models import ChineseProverb
# Register your models here.

admin.site.register(QuizAnswer)
admin.site.register(QuizQuestion)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(AnswerOrDrink)
admin.site.register(ChineseProverb)
