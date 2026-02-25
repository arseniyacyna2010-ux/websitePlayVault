from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['?', '?', '?'],
        'obj': {
            '?': '?',
            '?': '?',
            '?': '?'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
#def about(request):
    #return HttpResponse("<h4>страница про нас</h4>")
