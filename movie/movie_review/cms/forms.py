from django.forms import ModelForm
from cms.models import Movie, Impression


class MovieForm(ModelForm):
    """映画のフォーム"""

    class Meta:
        model = Movie
        fields = ('name', 'company', 'time',)


class ImpressionForm(ModelForm):
    """感想のフォーム"""

    class Meta:
        model = Impression
        fields = ('comment',)