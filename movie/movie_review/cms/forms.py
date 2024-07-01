from django.forms import ModelForm
from cms.models import Movie


class MovieForm(ModelForm):
    """映画のフォーム"""
    class Meta:
        model = Movie
        fields = ('name', 'company', 'time', )