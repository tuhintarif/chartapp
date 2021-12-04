from django.shortcuts import render, redirect
from .models import Subject
from .form import SubjectForm

# Create your views here.

def index(request):

    subjects = Subject.objects.all()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()

    context = {
        'subjects' : subjects,
        'form': form
    }

    return render(request, 'chart/index.html', context)
