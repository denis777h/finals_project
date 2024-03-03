from imaplib import _Authenticator
from pyexpat.errors import messages
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework import permissions
from board.serializers import *

from .models import Public_board, Username, Relevance_board
from .forms import LogoutFormsView
    
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        phone = request.POST['phone']
        output= "<h1> Логин</h2><h3> Пароль </h4><h5> Телефон</h6>"
        return HttpResponse(output)
    else:
        man = LogoutFormsView()
        return render(request, "login.html", {"form": LogoutFormsView})
        


class BoardList(ListView):
    model = Public_board
    template_name = 'board_list.html'
    context_object_name = 'board/'
    board = Public_board.objects.all()
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'title'
        context["content"] = 'content'
        return context
    
    



class BoardDetailView(DetailView):
    model = Public_board
    template_name = 'index.html'
    
    
    def get_object(self, queryset=None):
       if queryset == None:
           queryset = self.get_queryset() 
           new_str = self.kwargs.get('new_str') or self.request.GET.get('new_str') or None
           queryset = queryset.filter(pk=new_str)
           obj = queryset.get()
    
    
    
    
class ViewUsernameSerilez(viewsets.ModelViewSet):
    queryset = Username.objects.all()
    serializer_class = SerilezUsername 
    
    
    
class ViewPublic_boardSerilez(viewsets.ModelViewSet):
    queryset = Public_board.objects.all()
    serializer_class = SerilezPublic_board
    
    