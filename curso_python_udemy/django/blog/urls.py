from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]


# https://docs.djangoproject.com/en/5.1/topics/http/urls/