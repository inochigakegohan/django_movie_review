from django.contrib import admin
from cms.models import Movie, Impression

#admin.site.register(Movie)
#admin.site.register(Impression)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'time',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Movie, MovieAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('movie',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）


admin.site.register(Impression, ImpressionAdmin)