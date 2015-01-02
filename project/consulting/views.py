from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import generic
from django.conf import settings

from consulting.forms import ContactUsForm

from .models import PracticeArea, Client, QAndA, Consultant, LibraryCategory


class PracticeAreaListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return PracticeArea.objects.prefetch_related('client_set')
        else:
            return PracticeArea.published.prefetch_related('client_set')


class PracticeAreaDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return PracticeArea.objects.prefetch_related('client_set')
        else:
            return PracticeArea.published.prefetch_related('client_set')

    def get_context_data(self, **kwargs):
        context = super(PracticeAreaDetailView, self).get_context_data(**kwargs)
        if "preview" in self.request.GET:
            context['practicearea_list'] = PracticeArea.objects.all()
        else:
            context['practicearea_list'] = PracticeArea.published.all()
        return context



###################################################################################################


class ClientListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Client.objects.prefetch_related('practiceareas')
        else:
            return Client.published.prefetch_related('practiceareas')


class ClientDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Client.objects.prefetch_related('practiceareas', 'clientwork_set')
        else:
            return Client.published.prefetch_related('practiceareas', 'clientwork_set')

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        if "preview" in self.request.GET:
            context['client_list'] = Client.objects.all()
        else:
            context['client_list'] = Client.published.all()
        return context




###################################################################################################


class QAndAListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return QAndA.objects
        else:
            return QAndA.published


class QAndADetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return QAndA.objects
        else:
            return QAndA.published

    def get_context_data(self, **kwargs):
        context = super(QAndADetailView, self).get_context_data(**kwargs)
        if "preview" in self.request.GET:
            context['qanda_list'] = QAndA.objects.all()
        else:
            context['qanda_list'] = QAndA.published.all()
        return context

###################################################################################################


class ConsultantListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Consultant.objects
        else:
            return Consultant.published


class ConsultantDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return Consultant.objects
        else:
            return Consultant.published

    def get_context_data(self, **kwargs):
        context = super(ConsultantDetailView, self).get_context_data(**kwargs)
        if "preview" in self.request.GET:
            context['consultant_list'] = Consultant.objects.all()
        else:
            context['consultant_list'] = Consultant.published.all()
        return context


###################################################################################################


class LibraryCategoryListView(generic.ListView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return LibraryCategory.objects
        else:
            return LibraryCategory.published

class LibraryCategoryDetailView(generic.DetailView):
    def get_queryset(self):
        if "preview" in self.request.GET:
            return LibraryCategory.objects.all().prefetch_related('libraryfile_set')
        else:
            return LibraryCategory.published.all().prefetch_related('libraryfile_set')


###################################################################################################


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
            settings.DEFAULT_FROM_EMAIL,
            ["oliver@otessier.com"],
            headers=headers,
        )
        message.send()
        messages.add_message(self.request, messages.SUCCESS, 'Message sent. Thank you.')

        return super(ContactUsFormView, self).form_valid(form)
