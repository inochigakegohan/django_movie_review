from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    # 映画
    path('v1/movies/', views.movie_list, name='movie_list'),   # 一覧
]