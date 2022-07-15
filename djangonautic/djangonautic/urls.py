"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_view
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', article_view.article_list, name="home")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)