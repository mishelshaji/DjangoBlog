from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {"form": AuthenticationForm()})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                target = request.GET.get('next')
                if target is not None:
                    return redirect(target)
                return redirect('admin_home')
            return render(request, 'accounts/login.html', {"form": form})


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html', {"form": UserRegistrationForm()})
    elif request.method == "POST":
        ucf = UserRegistrationForm(request.POST)
        if ucf.is_valid():
            user = ucf.save(commit=False)
            user.set_password(ucf.cleaned_data.get('password1'))
            user.save()
            return redirect('login')
        return render(request, 'accounts/register.html', {"form": ucf})

def user_logout(request):
    logout(request)
    return redirect('homepage')