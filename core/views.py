from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

# def login_view(request):
#     return render(request, 'core/login.html')

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
                      'form' : form
                  })