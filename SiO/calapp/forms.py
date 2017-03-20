# from django import forms
# from SiO.CoAdmin.models import Event
# from SiO.member.models import Association
#
#
# class CalForm(forms.ModelForm):
#     association = forms.ModelChoiceField(queryset=Association.objects.none(),
#                                          widget=forms.Select(attrs={'class': 'form-control'}),
#                                          # widget=forms.Select(attrs={"onChange": 'getAsoc()'}),
#                                          # widget=forms.HiddenInput,
#                                          required=True)
#
#     class Meta:
#         model = Event
#         exclude = ['last_login', 'date_joined']
#         fields = ['association', ]
#         # fields = ['first_name', 'last_name', 'email', 'reg_date', ]
#
#     def __init__(self, user, *args, **kwargs):
#         super(CalForm, self).__init__(*args, **kwargs)
#         self.fields['association'].queryset = Association.objects.filter(asoc_name=user.association)
#

