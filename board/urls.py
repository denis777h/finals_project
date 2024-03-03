from django.urls import path, include
from rest_framework import serializers
from .views import login_view, BoardList, BoardDetailView, ViewUsernameSerilez, ViewPublic_boardSerilez



urlpatterns = [
    path('login/', login_view, name='login'),
    path('board/', BoardList.as_view(), name='board'),
    path('board/<str:new_str>/', BoardDetailView.as_view(), name='id'),
    path('board-api/',ViewUsernameSerilez.as_view({'get': 'list'}), name='api-username'),
    path('board-api/board',ViewPublic_boardSerilez.as_view({'get': 'list'}), name='api-board_public'),
       
    
    
    
]

