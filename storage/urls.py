from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('documents/', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('login/', views.login_view, name='login'),
]
