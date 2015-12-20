"""Forms for consulting project.

These are mostly to handle TinyMCE appearance.
"""


from django.forms import Form, CharField, EmailField, Textarea, ModelForm
from django.forms.widgets import TextInput
from tinymce.widgets import TinyMCE

from .models import PracticeArea, ClientWork, Consultant, QAndA, Client, \
    LibraryCategory, LibraryFile, SiteConfiguration, ClientReference


class ContactUsForm(Form):
    """Contact Us form."""

    subject = CharField(
            max_length=50,
            required=False,
    )

    from_email = EmailField(
            max_length=50,
            label='Your Email Address',
            required=True,
    )

    body = CharField(
            widget=Textarea(),
            label='Message',
    )


#########################################################################################
# All the following forms are included just so we can set some widget info for
# TinyMCE; they're just used the Django admin and don't do anything very exotic.


class PracticeAreaForm(ModelForm):
    class Meta:
        model = PracticeArea
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 600}),
        }


class ClientWorkForm(ModelForm):
    class Meta:
        model = ClientWork
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 250}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 175}),
        }


class ConsultantForm(ModelForm):
    class Meta:
        model = Consultant
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 300}),
        }


class QAndAForm(ModelForm):
    class Meta:
        model = QAndA
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'question': TinyMCE(mce_attrs={'height': 50}),
            'answer': TinyMCE(mce_attrs={'height': 300}),
        }


class LibraryCategoryForm(ModelForm):
    class Meta:
        model = LibraryCategory
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
        }


class LibraryFileForm(ModelForm):
    class Meta:
        model = LibraryFile
        exclude = []
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
        }


class SiteConfigurationForm(ModelForm):
    class Meta:
        model = SiteConfiguration
        exclude = []
        widgets = {
            'about_footer': TinyMCE(mce_attrs={'height': 50}),
            'about_homepage': TinyMCE(mce_attrs={'height': 50}),
        }


class ClientReferenceForm(ModelForm):
    class Meta:
        model = ClientReference
        exclude = []
        widgets = {
            'title': TextInput(attrs={'size': 20}),
            'job_title': TextInput(attrs={'size': 30}),
            'phone': TextInput(attrs={'size': 15}),
            'email': TextInput(attrs={'size': 25}),
            'position': TextInput(attrs={'size': 3}),
        }