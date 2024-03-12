from django import forms
from .models import Player, Game


class JoinGameForm(forms.ModelForm):
    game_code = forms.CharField(label='Kod Gry', max_length=10)
    nickname = forms.CharField(label='Nickname', max_length=50)

    class Meta:
        model = Player
        fields = ['game_code', 'nickname']

class GameForm(forms.ModelForm):
    game_code = forms.IntegerField()  # Add this line to make game_code an integer field

    class Meta:
        model = Game
        fields = ['game_code', 'host_name', 'questions']
        widgets = {
            'questions': forms.CheckboxSelectMultiple(),
        }
