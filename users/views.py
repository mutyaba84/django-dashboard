from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to some page after successful registration
            return redirect('login')  # You can change 'login' to the name of your login URL
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
