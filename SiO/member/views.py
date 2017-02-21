from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Member

from SiO.member.forms import RegForm

# TODO: Controller (en del av backend) for registrering av ny member


def membersignup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if not form.is_valid():
            return render(request, 'member/membersignup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            student_status = form.cleaned_data.get('student_status')
            reg_date = form.cleaned_data.get('reg_date')
            gender = form.cleaned_data.get('gender')
            birthday = form.cleaned_data.get('birthday')
            Member.objects.create(first_name=first_name, last_name=last_name, email=email,
                                  student_status=student_status, reg_date=reg_date,
                                  gender=gender, birthday=birthday)
            # user = authenticate(first_name=first_name, last_name=last_name, email=email,
            #                     student_status=student_status, reg_date=reg_date,
            #                     gender=gender, birthday=birthday)
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'member/membersignup.html',
                      {'form': RegForm()})
