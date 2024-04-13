from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.shortcuts import render, redirect

def home(request):
    # Retrieve the count of users from the database
    users_count = User.objects.count()

    # If the form is submitted
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Process the form data and save the user
            form.save()
            # Redirect to prevent form resubmission
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'home.html', {'users_count': users_count, 'form': form})
