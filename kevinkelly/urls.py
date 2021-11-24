from django.urls import path

from . import views

urlpatterns = [
    path('json_response', views.json_response, name='json_response'),
    path('html_template_response', views.html_template_response, name='html_template_response')
]
