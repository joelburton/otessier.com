from django.forms import Form, CharField, EmailField, Textarea, ModelForm
from tinymce.widgets import TinyMCE
from consulting.models import PracticeArea, ClientWork, Consultant, QAndA, Client, Quote, \
    LibraryCategory, LibraryFile, SiteConfiguration


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


class PracticeAreaForm(ModelForm):
    class Meta:
        model = PracticeArea
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 600}),
        }


class ClientWorkForm(ModelForm):
    class Meta:
        model = ClientWork
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 250}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 175}),
        }


class ConsultantForm(ModelForm):
    class Meta:
        model = Consultant
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'body': TinyMCE(mce_attrs={'height': 300}),
        }


class QAndAForm(ModelForm):
    class Meta:
        model = QAndA
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
            'question': TinyMCE(mce_attrs={'height': 50}),
            'answer': TinyMCE(mce_attrs={'height': 300}),
        }


class LibraryCategoryForm(ModelForm):
    class Meta:
        model = LibraryCategory
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
        }


class LibraryFileForm(ModelForm):
    class Meta:
        model = LibraryFile
        widgets = {
            'description': TinyMCE(mce_attrs={'height': 50}),
        }


class SiteConfigurationForm(ModelForm):
    class Meta:
        model = SiteConfiguration
        widgets = {
            'about_footer': TinyMCE(mce_attrs={'height': 50}),
            'about_homepage': TinyMCE(mce_attrs={'height': 50}),
        }

