from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('comment', Coment.as_view(), name='comment'),
    path('comment/<str:slug>/', GetComment.as_view(), name='comment'),
]
