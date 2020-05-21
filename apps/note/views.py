from django.shortcuts import render,redirect
from django.views.generic import View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm

class HomeView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        notes = Note.objects.all()
        context = {
            'notes':notes
        }
        return render(request,'note/index.html',context)

class AddNoteView(LoginRequiredMixin,View):
    def get(self,request):
        form = NoteForm()
        context = {
            'form':form,
        }
        return render(request,'note/add.html',context)
    def post(self,request):
        data = NoteForm(request.POST)
        if data.is_valid():
            data.instance.user = self.request.user            
            data.save()
            return redirect('home')

class DeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = '/'
    template_name = 'note/delete.html'


class UpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    success_url = '/'
    fields = ['text']
    template_name = 'note/add.html'

