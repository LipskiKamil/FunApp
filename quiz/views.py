import json
import random
from venv import logger

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from quiz.forms import JoinGameForm, GameForm
from quiz.models import Game, Player, QuizAnswer, QuizQuestion, AnswerOrDrink, ChineseProverb
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

def JoinGame(request):
    if request.method == 'POST':
        form = JoinGameForm(request.POST)
        if form.is_valid():
            game_code = form.cleaned_data['game_code']
            nickname = form.cleaned_data['nickname']

            try:
                game = Game.objects.get(game_code=game_code)

                if game.is_started:
                    return render(request, 'JoinGame.html', {'form': form, 'error_message': 'Gra o podanym kodzie już trwa!'})

                player = Player(game=game, nickname=nickname)
                player.save()


                return redirect('waiting_room', game_code=game_code, nickname=nickname)

            except Game.DoesNotExist:

                return render(request, 'JoinGame.html', {'form': form, 'error_message': 'Gra o podanym kodzie nie istnieje'})

    else:
        form = JoinGameForm()

    return render(request, 'JoinGame.html', {'form': form})


class CreateGameView(View):
    template_name = 'CreateGame.html'  # Update with the correct template path

    def get(self, request):
        form = GameForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            # Save the form data to the Game model
            game = form.save(commit=False)
            game.is_active = True  # Update based on your requirements
            game.is_started = False  # Update based on your requirements
            game.save()

            # Assign the selected questions to the game
            form.save_m2m()

            return redirect('JoinGame')  # Update with the correct URL name or path
        else:
            error_message = "Invalid form submission. Please check the entered data."
            context = {'form': form, 'error_message': error_message}
            return render(request, self.template_name, context)
def waiting_room(request, game_code, nickname):
    game = Game.objects.get(game_code=game_code)
    players = Player.objects.filter(game=game)

    return render(request, 'waiting_room.html',
                  {'game_code': game_code, 'nickname': nickname, 'players': players})

def start_game(request, game_code, nickname):
    try:
        game = Game.objects.get(game_code=game_code)
        game.is_started = True
        game.save()


        return redirect('gamequiz', game_code=game_code, nickname=nickname)

    except Game.DoesNotExist:
        return render(request, 'error_page.html', {'error_message': 'Gra nie istnieje'})

def leave_game(request, game_code, nickname):
    try:
        game = Game.objects.get(game_code=game_code)
        player = Player.objects.get(game=game, nickname=nickname)
        player.delete()

        return redirect('index')

    except (Game.DoesNotExist, Player.DoesNotExist):
        return render(request, 'error_page.html', {'error_message': 'Gra lub gracz nie istnieje'})


def gamequiz(request, game_code, nickname):
    game = Game.objects.get(game_code=game_code)
    questions = game.questions.all()

    request.session['nickname'] = nickname
    question_answers_dict = {}
    for question in questions:
        answers = QuizAnswer.objects.filter(question=question)
        question_answers_dict[question] = answers

    return render(request, 'gamequiz.html',
                  {'game_code': game_code, 'nickname': nickname, 'questions': questions, 'answers': question_answers_dict})

def submit_answers(request, game_code, nickname):
    if request.method == 'POST':
        game = Game.objects.get(game_code=game_code)
        questions = game.questions.all()
        player_score = 0

        for question in questions:
            selected_answer = request.POST.get(f'answer_{question.id}')

            if selected_answer == question.quizanswer_set.first().letter:
                # Jeżeli wybrana odpowiedź zgadza się z poprawną odpowiedzią, przyznaj punkt
                player_score += 1

        # Zaktualizuj wynik gracza w obiekcie Player
        player = Player.objects.get(game=game, nickname=nickname)
        player.score = player_score
        player.save()

        # Przekieruj na stronę podsumowania
        return redirect('summary', game_code=game_code)

    return HttpResponse("Method Not Allowed", status=405)

def summary(request, game_code):
    game = Game.objects.get(game_code=game_code)
    players = Player.objects.filter(game=game).order_by('-score')

    return render(request, 'summary.html', {'game': game, 'players': players})





@ensure_csrf_cookie
def random_question(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Pobierz wszystkie pytania
        all_questions = AnswerOrDrink.objects.all()

        if all_questions:
            # Wybierz losowe pytanie, jeśli lista nie jest pusta
            random_question = random.choice(all_questions)

            return JsonResponse({'question': random_question.AnswerOrDrinkQuestion})
        else:
            return JsonResponse({'question': 'Brak dostępnych pytań'})
    else:
        return render(request, 'QOD.html')

@ensure_csrf_cookie
def DailyChineseProverb(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        all_proverbs = ChineseProverb.objects.all()
        if all_proverbs:
            random_proverb = random.choice(all_proverbs)
            return JsonResponse({'random_proverb': random_proverb.ChineseProverb})
        else:
            return JsonResponse({'question': 'Brak dostępnych porzekadeł'})
    else:
        return render(request, 'ChineseProverb.html')

