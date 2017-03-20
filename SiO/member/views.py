from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Member, Association
from django.http import HttpResponse
from django.http import QueryDict
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import generic
from django.db.models import F
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

import json

from SiO.CoAdmin.models import Administrator
# from SiO.member.models import member_asoc
from SiO.member.forms import EditRegForm, RegAsoc, RegForm


# TODO: Controller (en del av backend) for registrering av ny member


# def member_overview(request):
#     member = Member.objects.all()
#     context = {'member': member}
#     return render(request, 'member/member_overview.html', context)

class member_overview(ListView):

    # model = Member
    # form_class = RegForm
    template_name = 'member/member_overview.html'
    # queryset = Member.objects.all()
    paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super(ListView, self).get_context_data(**kwargs)
    #     list_exam = Member.objects.all()
    #     paginator = Paginator(list_exam, self.paginate_by)
    #
    #     page = self.request.GET.get('page')
    #
    #     try:
    #         file_exams = paginator.page(page)
    #     except PageNotAnInteger:
    #         file_exams = paginator.page(1)
    #     except EmptyPage:
    #         file_exams = paginator.page(paginator.num_pages)
    #
    #     context['list_exams'] = file_exams
    #     return context

    # def search(self):
    #     # queryset_list = Member.objects.active()
    #     query = self.request.GET.get("q")
    #     if query:
    #         Member.objects.filter(first_name__icontains=query)

    # def get_queryset(self, *args, **kwargs):
    def get_queryset(self):
        # user = self.request.administrator
        # return Member.objects.filter(asoc_name=user)
        # return Member.objects.select_related(association=administrator.association)
        # return Member.objects.filter(association__in=Association.objects.filter(
        #     administrator__in=Administrator.objects.filter(asoc_name=asoc_name)))
        query = self.request.GET.get("q")
        if query:
            queryset = Member.objects.filter(association=self.request.user.association).filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )
            return queryset
        # elif query:
        #     qs = Member.objects.all()
        #     for term in query.split():
        #         qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
        #     return qs
        else:
            queryset = Member.objects.filter(association=self.request.user.association)
            return queryset

    # def get_queryset(self):
    #     user = self.request.user
    #     member_no = self.request.member_no
    #     asoc_admin = Administrator.objects.filter(asoc_name=user.asoc_name)
    #     asoc_member = Member.objects.filter(asoc_name=member_no.asoc_name)
    #     if user.is_authenticated():
    #         if asoc_admin == asoc_member:
    #             return Member.objects.all()

    # def get_asoc_name(self, user):
    #     CoAdmin = Administrator.objects.get(user=user)
    #     # memb = Member.asoc_name
    #     if CoAdmin == Administrator.objects.get(user=user):
    #         return Member.objects.filter(asoc_name__icontains='hioa')
    #         # return queryset



    # if Administrator.association == Member.association:
        # queryset = Member.objects.filter(Q(asoc_name='asoc_name'))

            # queryset = Member.objects.all()
            # Member.objects.filter(administrator__isnull=True).values_list('association', flat=True)

    # queryset = member_asoc.objects.filter(user__asoc_name=F('member_no__asoc_name'))

    # queryset = Member.objects.filter(asoc_name=F('asoc_name'))

        # return queryset

        # if Member.objects.filter(association__icontains=Administrator.username):
        #     queryset = Member.objects.filter(association__icontains=Administrator.username)
        # return queryset

        # if Member.objects.filter(association__icontains=Administrator.username):
        # queryset = Member.objects.filter(association='association').prefetch_related(self, 'association__administrator_set')
        # return queryset

        # TODO:Denne får fram kun forening CoAdmin er medlem av (hardkodet)
        # queryset = Member.objects.filter(association__icontains='HiOA')

        # qs = super(member_overview, self).get_queryset()
        # return qs.filter(association=self.kwargs['association'])
        # return Member.objects.filter(association=Member.association)
        # return Member.objects.filter(association__in=Administrator.objects.filter(association='association'))
        # return Administrator.objects.filter(association__in=Member.objects.filter(association='association'))
        # return queryset
    # queryset = Member.objects.filter(association='association')
    # return super(ListView, self).formfield_for_foreignkey(db_field, request, **kwargs)

# def member_edit(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     context = {'member': member}
#     return render(request, 'member/member_edit.html', context)

# class member_edit(CreateView):
#     model = Member
#     template_name = 'member/member_edit.html'
#     fields = '__all__'


# def member_update(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     member.first_name = request.POST['first_name']
#     member.last_name = request.POST['last_name']
#     member.email = request.POST['email']
#     member.student_status = request.POST['student_status']
#     member.reg_date = request.POST['reg_date']
#     member.gender = request.POST['gender']
#     member.birthday = request.POST['birthday']
#     member.save()
#     return redirect('member_overview')

# def member_edit(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     form = RegForm(request.POST)
#     if form.is_valid():
#         member.first_name = form.cleaned_data.get('first_name')
#         member.last_name = form.cleaned_data.get('last_name')
#         member.email = form.cleaned_data.get('email')
#         member.student_status = form.cleaned_data.get('student_status')
#         member.reg_date = form.cleaned_data.get('reg_date')
#         member.gender = form.cleaned_data.get('gender')
#         member.birthday = form.cleaned_data.get('birthday')
#         member.save()
#     return redirect('member_edit')
    # messages.add_message(request,
    #                      messages.SUCCESS,
    #                      'Your profile was successfully edited.')
    # else:
    #     messages.add_message(request,
    #                          messages.SUCCESS,
    #                          'Something went wrong.')
    # return render(request, 'member/member_edit.html', {'form': form})
    #
    #     else:
    #         return redirect(request, '/')

# class member_update(UpdateView):
#     model = Member
#     template_name = 'member/member_edit.html'
#     fields = ['first_name', 'last_name', 'email', 'student_status', 'reg_date', 'gender', 'birthday', ]

# def member_edit(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     if request.method == 'POST':
#         form = RegForm(request.POST or None, instance=member)
#         if form.is_valid():
#             # member.first_name = form.cleaned_data.get('first_name')
#             # member.last_name = form.cleaned_data.get('last_name')
#             # member.email = form.cleaned_data.get('email')
#             # # member.student_status = form.cleaned_data.get('student_status')
#             # member.reg_date = form.cleaned_data.get('reg_date')
#             # # member.gender = form.cleaned_data.get('gender')
#             # # member.birthday = form.cleaned_data.get('birthday')
#             form.save()
#             return redirect('member_overview')
#     form = RegForm(instance=member)
#     return render(request, 'member/member_edit.html', {'form': form, 'member': member})


class member_edit(UpdateView):
    model = Member
    form_class = EditRegForm
    # pk_url_kwarg = 'member_no'
    success_url = reverse_lazy('member_overview')
    template_name = 'member/member_edit.html'


class member_delete(DeleteView):
    model = Member
    success_url = reverse_lazy('member_overview')
    template_name = 'member/member_delete.html'


def member_signup(request):
    if request.method == 'POST':
        form = RegForm(request.user, request.POST)
        if not form.is_valid():
            return render(request, 'member/member_signup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            # asoc_name = form.cleaned_data.get('asoc_name')
            asoc = form.cleaned_data.get('association')
            # asoc = Association.objects.get(id=asoc_pk.pk)
            student_status = form.cleaned_data.get('student_status')
            reg_date = form.cleaned_data.get('reg_date')
            gender = form.cleaned_data.get('gender')
            end_date = form.cleaned_data.get('end_date')
            Member.objects.create(first_name=first_name, last_name=last_name, email=email,
                                  student_status=student_status, association=asoc,
                                  reg_date=reg_date, gender=gender, end_date=end_date)
            # Member.objects.create(first_name=first_name, last_name=last_name, email=email,
            #                       reg_date=reg_date,)
            # Member.save()
            # user = authenticate(first_name=first_name, last_name=last_name, email=email,
            #                     student_status=student_status, reg_date=reg_date,
            #                     gender=gender, birthday=birthday)
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'member/member_signup.html',
                      {'form': RegForm(request.user)})


def asoc_signup(request):
    if request.method == 'POST':
        form = RegAsoc(request.POST)
        if not form.is_valid():
            return render(request, 'member/asoc_signup.html',
                          {'form': form})

        else:
            asoc_name = form.cleaned_data.get('asoc_name')
            Association.objects.create(asoc_name=asoc_name)
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'member/asoc_signup.html',
                      {'form': RegAsoc()})

# class member_delete(DeleteView):
#     def post(self, request, *args, **kwargs):
#         member = get_object_or_404(id=request.POST['member_no'])
#         member.delete()
#         return HttpResponseRedirect('/')
#
#     def get(self, request, *args, **kwargs):
#         member = Member.objects.get(id=kwargs['member_no'])
#         context = {'member': member}
#         return render_to_response("template.html", context, context_instance=RequestContext(request))


# def member_delete(request, member_no):
#     # member = get_object_or_404(Member, member=member_no)
#     member = Member.objects.get(member_no=member_no)
#     if request.method == "POST":
#         member.delete()
#         messages.success(request, "This has been deleted.")
#         return render(request, 'member/member_overview.html')
#     context = {'member': member}
#     return render(request, 'member/member_delete.html', context)

# def member_delete(request):
#
#     if request.method == 'DELETE':
#
#         member = Member.objects.get((QueryDict(request.body).get('member_no')))
#
#         member.delete()
#
#         response_data = {}
#         response_data['msg'] = 'Member was deleted.'
#
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )

# class member_delete(DeleteView):
#     model = Member
#     success_url = reverse_lazy('member_overview')
#     template_name = 'member/member_delete.html'
    # success_url = 'member/member_overview.html'

    # def get_success_url(self):
    #     return reverse('member_overview')
# def member_delete(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     # messages.add_message(request,
#     #                      messages.SUCCESS,
#     #                      'Are you sure?')
#     member.delete()
#     return render(request, 'member/member_overview.html')
#     # return redirect('/')
