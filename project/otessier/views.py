"""Site-wide views."""

from django.views import generic
from consulting.models import PracticeArea, Quote


class HomepageView(generic.TemplateView):
    """View for site homepage."""

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """Get practice areas and quotes for homepage."""

        context = super().get_context_data(**kwargs)

        if self.request.preview_mode:
            pas = PracticeArea.objects
            quotes = Quote.objects

        else:
            pas = PracticeArea.published
            quotes = Quote.published

        context['practicearea_list'] = pas.only('title',
                                                'short_description',
                                                'icon_name',
                                                'slug').all()
        context['quote_list'] = quotes.values('quote', 'author').all()

        return context
