from django import forms
# from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import AbstractUser as Admin
from .models import Member, Association
# from SiO.CoAdmin.models import Member, Association
from django_popup_view_field.fields import PopupViewField

from .popups import GenderPopupView

from SiO.settings import ALLOWED_SIGNUP_DOMAINS
from SiO.CoAdmin.models import Administrator


# TODO: Her lages det validering


def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501


def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['member', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'member', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network', ]

    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


# def InvalidUsernameValidator(value):
#     if '@' in value or '+' in value or '-' in value:
#         raise ValidationError('Enter a valid username.')


def UniqueEmailValidator(value):
    if Member.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


# def validate_gender(value):
#     if not value in ('woman', 'man', 'female', 'male'):
#         raise ValidationError(u'%s is not a valid value for gender.' % value)


# def UniqueUsernameIgnoreCaseValidator(value):
#     if Member.objects.filter(username__iexact=value).exists():
#         raise ValidationError('User with this Username already exists.')

# def get_queryset(self):
#     queryset = Administrator.objects.filter(association=self.request.user.association)
#     return queryset

# CHOICES=[('Activ','Activ'),
#          ('Not activ','Not activ')]

# CHOICES = [('Activ', 'Activ'), ]
         # ('Not activ','Not activ')]
CHOICES = [('Female', 'Female'),
           ('Male', 'Male')]


class RegForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname', 'id': 'firstname'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname', 'id': 'lastname'}),
        max_length=30,
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'id': 'email'}),
        required=True,
        max_length=75)
    # association = forms.ModelChoiceField(queryset=Association.objects.none(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}),
    #                                      required=True)

    # association_choices = [(i['asoc_name'], i['asoc_name']) for i in Association.objects.values('asoc_name')]
    # association = forms.ChoiceField(choices=association_choices, widget=forms.Select(attrs={'class': 'form-control'}),
    #                               required=True)
    # asoc_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=30,
    #     required=True)

    # asoc_name = forms.ModelChoiceField(
    #     queryset=Association.objects.values('asoc_name'),
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     required=True)
    # student_status = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=30,
    #     required=True)
    # student_status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id': 'value'}))
    # reg_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3, attrs={'name': 'reg_date'}))
    date_of_birth = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3, attrs={'name': 'date_of_birth'}))
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'name': 'gender'}))
    # gender = PopupViewField(
    #     # ##Attrs for popup
    #     view_class=GenderPopupView,
    #     popup_dialog_title='What is your gender?',
    #     # ##Attr for CharField
    #     required=True,
    #     help_text='Enter either woman or man or female or male'
    # )
    # gender = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=30,
    #     required=False)
    end_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3, attrs={'name': 'end_date'}))

    class Meta:
        model = Member
        exclude = ['last_login', 'date_joined']
        fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'end_date']
        # fields = ['first_name', 'last_name', 'email', 'reg_date', ]

    # def __init__(self, user, *args, **kwargs):
    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(RegForm, self).__init__(*args, **kwargs)
        # self.fields['association'].queryset = Association.objects.filter(asoc_name=user.association)

        # association = kwargs.pop('association', None)
        # self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        # self.fields['username'].validators.append(InvalidUsernameValidator)
        # self.fields['username'].validators.append(
        #     UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)
        # self.fields['gender'].validators.append(validate_gender)
        # self.fields['association'].validators.append(get_queryset)
        # self.fields['association'].queryset = Association.objects.filter(asoc_name='asoc_name')

    # def clean(self):
    #     super(RegForm, self).clean()
    #     association = self.cleaned_data.get('association')
    #     if association:
    #         self.fields['association'].queryset = Association.objects.filter(asoc_name='asoc_name')


class EditRegForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname'}),
        max_length=30,
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
        required=True,
        max_length=75)
    # association = forms.ModelChoiceField(queryset=Association.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}),
    #                                      required=True)
    # student_status = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=30,
    #     required=True)
    # reg_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3, attrs={'name': 'reg_date'}))
    date_of_birth = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3, attrs={'name': 'date_of_birth'}))
    # gender = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=30,
    #     required=False)
    end_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3, attrs={'name': 'end_date'}))

    class Meta:
        model = Member
        exclude = ['last_login', 'date_joined']
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'end_date']

    def __init__(self, *args, **kwargs):
        super(EditRegForm, self).__init__(*args, **kwargs)
        # self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        # self.fields['username'].validators.append(InvalidUsernameValidator)
        # self.fields['username'].validators.append(
        #     UniqueUsernameIgnoreCaseValidator)
        # self.fields['email'].validators.append(UniqueEmailValidator)
        # self.fields['email'].validators.append(SignupDomainValidator)
        # self.fields['association'].validators.append(CanNotChangeAssociation)


class RegAsoc(forms.ModelForm):
    asoc_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    # user = forms.ModelChoiceField(queryset=Administrator.objects.all(),
    #                                        widget=forms.Select(attrs={'class': 'form-control'}),
    #                                        required=True)

    class Meta:
        model = Association
        fields = ['asoc_name', ]

    def __init__(self, user, *args, **kwargs):
        super(RegAsoc, self).__init__(*args, **kwargs)
        # self.fields['administrator'].queryset = Member.objects.filter(member=user.association)



    # def clean(self):
    #     super(RegForm, self).clean()
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if password and password != confirm_password:
    #         self._errors['password'] = self.error_class(
    #             ['Passwords don\'t match'])
    #     return self.cleaned_data
