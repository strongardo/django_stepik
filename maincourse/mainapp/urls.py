from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='root'),
    path('home/', views.home_page, name='home'),
    path('words_list/', views.words_list_page, name='words_list'),
    path('add_word/', views.add_word_page, name='add_word'),
]
