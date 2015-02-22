from random import choice

from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import Prefetch
from django.views import generic
from django.conf import settings
from django.core.cache import cache

from .forms import ContactUsForm

from .models import PracticeArea, Client, QAndA, Consultant, LibraryCategory, Quote, LibraryFile, \
    ClientWork


# noinspection PyUnresolvedReferences
class WorkflowMixin(object):
    """Mixin to add workflow-awareness to generic views.

    Changes the queryset to get only published objects when not in preview_mode.
    """

    def get_queryset(self):
        if self.request.preview_mode:
            return self.model.objects
        else:
            return self.model.published


# noinspection PyUnresolvedReferences
class PortletListMixin(object):
    """Mixin to get all-items-of-type lists in portlets.

    Many views (such as a client detail page) show a portlet listing all clients; this
    get this from the same queryset as the original question.
    """

    # noinspection PyProtectedMember
    def get_context_data(self, **kwargs):
        context = super(PortletListMixin, self).get_context_data(**kwargs)

        # for Client, this created an item called 'client_list' in the context.
        #
        # prefetch_related(None) makes sure we don't ask for any prefetches--since these wouldn't
        # be needed for the portlet

        context[self.model._meta.model_name + '_list'] = (
            self.get_queryset().prefetch_related(None).only('title', 'slug'))
        return context


class PortletCommonMixin(object):
    """Mixin to show random quotes/Q&A; used on many views."""

    def _get_random(self, name, qs):
        """Return a random item from the query; cache possibilities for future use.

        name: name to cache this by
        qs: queryset to search
        """

        objs = cache.get(name)
        if not objs:
            objs = qs.order_by()  # don't waste time sorting
            cache.set(name, objs)
        if objs:
            return choice(objs)

    def random_quote(self):
        return self._get_random('quotes', Quote.published.values('quote', 'author'))

    def random_qanda(self):
        return self._get_random('qandas', QAndA.published.only('title', 'slug', 'description'))


###################################################################################################


class PracticeAreaListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = PracticeArea

    def get_queryset(self):
        """Return practiceareas and related clients."""

        qs = super(PracticeAreaListView, self).get_queryset()
        related_qs = Client.objects if self.request.preview_mode else Client.published
        return qs.prefetch_related(Prefetch('client_set', queryset=related_qs.all()))


class PracticeAreaDetailView(WorkflowMixin,
                             PortletListMixin,
                             PortletCommonMixin,
                             generic.DetailView):
    model = PracticeArea

    def get_queryset(self):
        """Return practicearea and related clients."""

        qs = super(PracticeAreaDetailView, self).get_queryset()
        related_qs = Client.objects if self.request.preview_mode else Client.published
        return qs.prefetch_related(Prefetch('client_set', queryset=related_qs.all()))


###################################################################################################


class ClientListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = Client

    def get_queryset(self):
        """Return clients and related practice areas."""

        qs = super(ClientListView, self).get_queryset()
        related_qs = PracticeArea.objects if self.request.preview_mode else PracticeArea.published
        return qs.prefetch_related(Prefetch('practiceareas', queryset=related_qs.all()))


class ClientDetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = Client

    def get_queryset(self):
        """Return client and related practice area and client work."""

        qs = super(ClientDetailView, self).get_queryset()
        related_pas = PracticeArea.objects if self.request.preview_mode else PracticeArea.published
        related_works = ClientWork.objects if self.request.preview_mode else ClientWork.published
        return qs.prefetch_related(
            Prefetch('practiceareas', queryset=related_pas.all()),
            Prefetch('clientwork_set', queryset=related_works.all()),
            )


###################################################################################################


class QAndAListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = QAndA


class QAndADetailView(WorkflowMixin, PortletListMixin, generic.DetailView):
    model = QAndA

###################################################################################################


class ConsultantListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = Consultant


class ConsultantDetailView(WorkflowMixin,
                           PortletCommonMixin,
                           PortletListMixin,
                           generic.DetailView):
    model = Consultant


###################################################################################################


class LibraryCategoryListView(WorkflowMixin, PortletCommonMixin, generic.ListView):
    model = LibraryCategory


class LibraryCategoryDetailView(WorkflowMixin,
                                PortletCommonMixin,
                                PortletListMixin,
                                generic.DetailView):
    model = LibraryCategory

    def get_queryset(self):
        """Return library category and related files."""

        qs = super(LibraryCategoryDetailView, self).get_queryset()
        related_qs = LibraryFile.objects if self.request.preview_mode else LibraryFile.published
        return qs.prefetch_related(Prefetch('libraryfile_set', queryset=related_qs.all()))


###################################################################################################


class ContactUsFormView(generic.FormView):
    """View for contact us form."""

    form_class = ContactUsForm
    template_name = "consulting/contact_form.html"
    success_url = "/"

    def form_valid(self, form):
        """If form is valid, send the email."""

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
