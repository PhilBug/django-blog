from django.urls import path
from . import views


urlpatterns = [
    path('', views.post, name='posts'), # will be removed?
    path('<int:post_id>', views.post, name='post'),
]
