from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 映画
    path('movie/', views.movie_list, name='movie_list'),  # 一覧
    path('movie/add/', views.movie_edit, name='movie_add'),  # 登録
    path('movie/mod/<int:movie_id>/', views.movie_edit, name='movie_mod'),  # 修正
    path('movie/del/<int:movie_id>/', views.movie_del, name='movie_del'),  # 削除
]
