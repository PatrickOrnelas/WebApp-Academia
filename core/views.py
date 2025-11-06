from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Autenticação do usuário aqui
            return redirect('home')
    return render(request, 'core/login.html',
                   {'form': form})

# def logout_view(request):
#     return render(request, 'core/logout.html')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'core/register.html',
                  {
                      'form' : form})