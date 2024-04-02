from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            messages.success(request, 'A user in added. Please login!')

            return redirect('/')
        
    else:
        form = SignupForm()

    return render(request, 'userauth/signup.html', {
        'form': form,
        'title': 'Signup'
    })

        
