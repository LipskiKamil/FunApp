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
    def clean_game_code(self):
        game_code = self.cleaned_data.get('game_code')
        if Game.objects.filter(game_code=game_code).exists():
            raise forms.ValidationError("Gra o takim kodzie już istnieje!")
        return game_code
