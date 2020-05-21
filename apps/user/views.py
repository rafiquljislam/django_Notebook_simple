from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        context={
            'form':UserCreationForm()
        }
        return render(request, 'user/login.html',context)

    def post(self, request, *args, **kwargs):
        data = UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            username = data.cleaned_data['username']
            password = data.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('home')