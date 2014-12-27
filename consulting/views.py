from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import generic
from consulting.forms import ContactUsForm

from .models import PracticeArea, Client, QAndA, Consultant, LibraryCategory


class PracticeAreaListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return PracticeArea.objects.show_private().prefetch_related('client_set')
        else:
            return PracticeArea.objects.prefetch_related('client_set')


class PracticeAreaDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return PracticeArea.objects.show_private().prefetch_related('client_set')
        else:
            return PracticeArea.objects.prefetch_related('client_set')


class ClientListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Client.objects.show_private().prefetch_related('practiceareas')
        else:
            return Client.objects.prefetch_related('practiceareas')


class ClientDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Client.objects.show_private().prefetch_related('practiceareas')
        else:
            return Client.objects.prefetch_related('practiceareas')

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)

        # We want to only show client work that is published
        if "preview" in self.request.GET:
            context['clientworks'] = self.object.clientwork_set.show_private().all()
        else:
            context['clientworks'] = self.object.clientwork_set.all()

        return context


class QAndAListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return QAndA.objects.show_private()
        else:
            return QAndA.objects


class QAndADetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return QAndA.objects.show_private()
        else:
            return QAndA.objects


class ConsultantListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Consultant.objects.show_private()
        else:
            return Consultant.objects


class ConsultantDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Consultant.objects.show_private()
        else:
            return Consultant.objects


class LibraryCategoryListView(generic.ListView):
    queryset = LibraryCategory.objects.all().prefetch_related('libraryfile_set')


class ContactUsFormView(generic.FormView):
    """View for contact us form."""

    form_class = ContactUsForm
    template_name = "consulting/contact_form.html"
    success_url = "/"

    def form_valid(self, form):
        from_email = form.cleaned_data['from_email']
        body = form.cleaned_data['body']
        subject = form.cleaned_data['subject']

        headers = {'Reply-To': from_email}

        message = EmailMessage(
            "[Contact Us Form] %s" % subject,
            body,
            "oliver@otessier.com",
            ["oliver@otessier.com"],
            headers=headers,
        )
        message.send()
        messages.add_message(self.request, messages.SUCCESS, 'Message sent. Thank you.')

        return super(ContactUsFormView, self).form_valid(form)
