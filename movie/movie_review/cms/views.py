from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Movie

def movie_list(request):
    """映画の一覧"""
    # return HttpResponse('映画の一覧')
    movies = Movie.objects.all().order_by('id')
    return render(request,
                  'cms/movie_list.html',  # 使用するテンプレート
                  {'movies': movies})  # テンプレートに渡すデータ


def movie_edit(request, movie_id=None):
    """映画の編集"""
    return HttpResponse('映画の編集')


def movie_del(request, movie_id):
    """映画の削除"""
    return HttpResponse('映画の削除')
