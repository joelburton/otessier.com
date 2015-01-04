from django.forms import Form, CharField, EmailField, Textarea


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
