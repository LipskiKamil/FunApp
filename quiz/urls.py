from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import gamequiz, DailyChineseProverb, CreateGameView
from .views import JoinGame, random_question
from .views import leave_game
from .views import start_game
from .views import submit_answers
from .views import summary
from .views import waiting_room

urlpatterns = [
        path('', TemplateView.as_view(template_name='index.html'), name='index'),
        path('joingame/', JoinGame, name='JoinGame'),
        path('waiting_room/<str:game_code>/<str:nickname>/', waiting_room, name='waiting_room'),
        path('start_game/<str:game_code>/<str:nickname>/', start_game, name='start_game'),
        path('leave_game/<str:game_code>/<str:nickname>/', leave_game, name='leave_game'),
        path('gamequiz/<str:game_code>/<str:nickname>/', gamequiz, name='gamequiz'),
        path('<str:game_code>/<str:nickname>/submit_answers/', submit_answers, name='submit_answers'),
        path('<str:game_code>/summary/', summary, name='summary'),
        path('QOD/', random_question, name='random_question'),
        path('DailyChineseProverb/', DailyChineseProverb, name='daily_chinese_proverb'),
        path('create_game/', CreateGameView.as_view(), name='CreateGame'),
]