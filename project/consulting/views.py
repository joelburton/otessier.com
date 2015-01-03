from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import generic
from django.conf import settings

from consulting.forms import ContactUsForm

from .models import PracticeArea, Client, QAndA, Consultant, LibraryCategory


class WorkflowMixin(object):
    def get_queryset(self):
        if self.request.preview_mode:
            return self.model.objects
        else:
            return self.model.published


class PortletListMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PortletListMixin, self).get_context_data(**kwargs)
        context[self.model._meta.model_name + '_list'] = self.get_queryset()
        return context


###################################################################################################


class PracticeAreaListView(WorkflowMixin, generic.ListView):
    model = PracticeArea

    def get_queryset(self):
        qs = super(PracticeAreaListView, self).get_queryset()
        return qs.prefetch_related('client_set')


class PracticeAreaDetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = PracticeArea

    def get_queryset(self):
        qs = super(PracticeAreaDetailView, self).get_queryset()
        return qs.prefetch_related('client_set')


###################################################################################################


class ClientListView(WorkflowMixin, generic.ListView):
    model = Client

    def get_queryset(self):
        qs = super(ClientListView, self).get_queryset()
        return qs.prefetch_related('practiceareas')


class ClientDetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = Client

    def get_queryset(self):
        qs = super(ClientDetailView, self).get_queryset()
        return qs.prefetch_related('practiceareas', 'clientwork_set')


###################################################################################################


class QAndAListView(WorkflowMixin, generic.ListView):
    model = QAndA


class QAndADetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = QAndA

###################################################################################################


class ConsultantListView(WorkflowMixin, generic.ListView):
    model = Consultant


class ConsultantDetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = Consultant


###################################################################################################


class LibraryCategoryListView(WorkflowMixin, generic.ListView):
    model = LibraryCategory


class LibraryCategoryDetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = LibraryCategory

    def get_queryset(self):
        qs = super(LibraryCategoryDetailView, self).get_queryset()
        return qs.prefetch_related('libraryfile_set')


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
