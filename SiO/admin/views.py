from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Administrator

from SiO.admin.forms import SignUpForm

# TODO: Controller (en del av backend) for registrering av ny member


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'admin/signup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            association = form.cleaned_data.get('association')
            union_position = form.cleaned_data.get('union_position')
            Administrator.objects.create_user(username=username, password=password, email=email,
                                              first_name=first_name, last_name=last_name,
                                              union_position=union_position, association=association)
            user = authenticate(username=username, password=password, email=email,
                                first_name=first_name, last_name=last_name,
                                union_position=union_position, association=association)
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'admin/signup.html',
                      {'form': SignUpForm()})

