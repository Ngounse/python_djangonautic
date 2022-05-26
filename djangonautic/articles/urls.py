from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('test/', views.article_test, name="test"),
    path(r'<slug>/', views.article_detail, name="detail"),
]
