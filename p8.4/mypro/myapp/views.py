from django.shortcuts import render
from .forms import myForm


# Create your views here.
def my_view(request):
    form=myForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            data = {
                'name': name,
                'email': email,
                'message': message
            }
            # You can perform further actions with the data, such as saving it to a database or sending an email.
            return render(request, 'myapp/success.html', {'data': data})
    return render(request, 'myapp/form.html', {'form': form})