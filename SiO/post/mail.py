from crispy_forms.bootstrap import FormActions
# from crispy_forms.layout import Button, MultiField, Div, HTML, \
#     Field, Fieldset, Reset, Submit
from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file
from django import forms
from django.core.urlresolvers import reverse

from .models import Email
# from .views import mailPost
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, HTML, \
    Field, Submit, Button, Fieldset
from crispy_forms.bootstrap import FormActions


#  Bytt ut med variabeldata hentet vra views.
# class mailHandler(forms.ModelForm):
#     # TODO: gjør om sender til å auto-hente foreningsnavn og sende dette som avsendernavn
#     # sender = forms.CharField(
#     #     widget=forms.EmailInput(attrs={'class': 'form-control'}),
#     #     max_length=254,
#     #     required=True)
#     # TODO: endre receiver så den kan ta flere epostadresser, hver av dem maks 254 bokstaver lang
#     receiver = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=254,
#         label='Send To',
#         required=True)
#     # TODO Legg til en "Er du sikker på at du vil sende uten emne"-melding
#     subject = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=130,  # ###max length satt til 130 da denne er max length før truncate på gmail og outlook
#         required=False)
#     message = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=1500,
#         required=True)
#
#     class Meta:
#         model = Email
#         fields = ['receiver', 'subject', 'message', ]

class mailHandler(forms.Form):
    # ###sender = forms.CharField(label='Sender')
    subject = forms.CharField(required=False)
    receiver = forms.EmailField(label='Send To')
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50}),
                              required=False)

    # ###class Meta:
    #     ###model = Email
    #     ###fields = ['sender', 'receiver', 'subject', 'message', ]

    def __init__(self, *args, **kwargs):
        super(mailHandler, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        # self.helper.label_class = 'col-sm-3 col-md-3'
        # self.helper.field_class = 'col-sm-9 col-md-9'
        # ###self.helper.form_action = reverse('submit_form')
        # ###self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            Field(
                None,
                Div(
                    HTML('''
                           {% if messages %}
                           {% for message in messages %}
                           <center><p {% if message.tags %}
                           class="alert alert-{{ message.tags }}"
                           {% endif %}>{{ message }}</p></center>{% endfor %}{% endif %}
                            '''),
            # ###Field('subject'),
            # ###Field('sender'),
            # ###Field('receiver'),
            # ###Field('message'),
            # ###)
                    # ###Div(
                    #     # ###'report_format',
                    #     # ###Field('sender', required=True),
                    #     # ###Field('receiver', required=True),
                    #     # ###'optional_fields',
                    #     # ###css_class='well col-sm-4 col-md-4',
                    # ),
                    # Fieldset('Post email',
                    Div('subject',
                        # ###'sender',
                        Field('receiver', placeholder='Email address',
                              required=True),
                        'message',
                        FormActions(
                            Submit('submit', 'Send Email', css_class='btn btn-lg btn-block'),
                            # Submit('submit', 'Send Email', css_class='btn btn-info'),
                            # Submit('cancel', 'Cancel', css_class='btn btn-primary'),
                            # ###css_class='btn btn-lg'
                            # ###css_class='pull-right'
                        ),
                        # ###css_class='col-sm-8 col-md-8',
                        ),
                             # ),
                    # ###css_class='row'
                ),
            ),
        )
    #     # ###self.fields['subject'].initial = '[GlucoseTracker] Glucose Data Report'




