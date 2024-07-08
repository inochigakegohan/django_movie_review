import json
from collections import OrderedDict
from django.http import HttpResponse
from cms.models import Movie


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def movie_list(request):
    """映画と感想のJSONを返す"""
    movies = []
    for movie in Movie.objects.all().order_by('id'):

        impressions = []
        for impression in movie.impressions.order_by('id'):
            impression_dict = OrderedDict([
                ('id', impression.id),
                ('comment', impression.comment),
            ])
            impressions.append(impression_dict)

        movie_dict = OrderedDict([
            ('id', movie.id),
            ('name', movie.name),
            ('company', movie.company),
            ('time', movie.time),
            ('impressions', impressions)
        ])
        movies.append(movie_dict)

    data = OrderedDict([ ('movies', movies) ])
    return render_json_response(request, data)
