from django.urls import path, include, re_path
import article.views
urlpatterns = [
    path('articles/all/', article.views.animals),
    path('articles/get/<int:animal_id>/', article.views.animal),
    path('articles/addcomment/<int:animal_id>/', article.views.addcomment),
    path('page/<int:page_number>/', article.views.animals),
    path('', article.views.animals),
]