from random import choice

from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import generic
from django.conf import settings
from django.core.cache import cache

from consulting.forms import ContactUsForm

from .models import PracticeArea, Client, QAndA, Consultant, LibraryCategory, Quote



class WorkflowMixin(object):
    """Mixin to add workflow-awareness to generic views.

    Changes the queryset to get only published objects when not in preview_mode.
    """

    def get_queryset(self):
        if self.request.preview_mode:
            return self.model.objects
        else:
            return self.model.published


class PortletListMixin(object):
    """Mixin to get all-items-of-type lists in portlets.

    Many views (such as a client detail page) show a portlet listing all clients; this
    get this from the same queryset as the original question.
    """

    def get_context_data(self, **kwargs):
        context = super(PortletListMixin, self).get_context_data(**kwargs)

        # for Client, this created an item called 'client_list' in the context.
        #
        # prefetch_related(None) makes sure we don't ask for any prefetches--since these wouldn't
        # be needed for the portlet

        context[self.model._meta.model_name + '_list'] = self.get_queryset().prefetch_related(None)
        return context


class PortletCommonMixin(object):
    """Mixin to show random quotes/Q&A; used on many views."""

    def random_quote(request):
        quotes = cache.get('quotes')
        if not quotes:
            quotes = Quote.published.values('quote', 'author').order_by()
            cache.set('quotes', quotes)
        return choice(quotes)

    def random_qanda(request):
        qandas = cache.get('qandas')
        if not qandas:
            qandas = QAndA.published.only('title', 'slug', 'description').order_by()
            cache.set('qandas', qandas)
        return choice(qandas)


###################################################################################################


class PracticeAreaListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = PracticeArea

    def get_queryset(self):
        qs = super(PracticeAreaListView, self).get_queryset()
        return qs.prefetch_related('client_set')


class PracticeAreaDetailView(WorkflowMixin, PortletListMixin, PortletCommonMixin, generic.DetailView):
    model = PracticeArea

    def get_queryset(self):
        qs = super(PracticeAreaDetailView, self).get_queryset()
        return qs.prefetch_related('client_set')


###################################################################################################


class ClientListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
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


class QAndAListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = QAndA


class QAndADetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = QAndA

###################################################################################################


class ConsultantListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = Consultant


class ConsultantDetailView(WorkflowMixin, PortletCommonMixin, PortletListMixin, generic.DetailView):
    model = Consultant


###################################################################################################


class LibraryCategoryListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
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
