from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Movie
from cms.forms import MovieForm


def movie_list(request):
    """映画の一覧"""
    # return HttpResponse('映画の一覧')
    movies = Movie.objects.all().order_by('id')
    return render(request,
                  'cms/movie_list.html',  # 使用するテンプレート
                  {'movies': movies})  # テンプレートに渡すデータ


def movie_edit(request, movie_id=None):
    """映画の編集"""
    # return HttpResponse('映画の編集')
    if movie_id:  # movie_id が指定されている (修正時)
        movie = get_object_or_404(Movie, pk=movie_id)
    else:  # movie_id が指定されていない (追加時)
        movie = Movie()

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            movie = form.save(commit=False)
            movie.save()
            return redirect('cms:movie_list')
    else:  # GET の時
        form = MovieForm(instance=movie)  # movie インスタンスからフォームを作成

    return render(request, 'cms/movie_edit.html', dict(form=form, movie_id=movie_id))


def movie_del(request, movie_id):
    """映画の削除"""
    return HttpResponse('映画の削除')
