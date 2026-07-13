from django.urls import path
from . import views

app_name = 'blog'

# http://dominio.com.br/
# blog/
urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'), # url:blog/post/id o id deve ser dinâmico
    path('exemplo/', views.exemplo, name='exemplo')
]