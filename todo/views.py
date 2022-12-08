from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todos to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated] # TokenAuthentication

    def create(self, request):
        todo = Todo.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            user=self.request.user,
        )
        serialized_obj = serializers.serialize('json', [todo])
        return HttpResponse(serialized_obj, content_type='application/json')


def login_view(request):

    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'login/login.html', {'successful': True, })
        else:
            return render(request, 'login/login.html', {'error': True, })

    return render(request, 'login/login.html')


def register_view(request):

    if request.method == 'POST':
        username, password, email = request.POST['username'], request.POST[
            'password'], request.POST['email']
        user = User.objects.create_user(username, email, password)
        user = authenticate(username=username, password=password)
        Token.objects.create(user=user)
        login(request, user)
        return render(request, 'register/register.html', {'successful': True})
    return render(request, 'register/register.html')
