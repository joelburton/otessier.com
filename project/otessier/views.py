from django.views import generic
from consulting.models import PracticeArea, Quote


class HomepageView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)

        if self.request.preview_mode:
            context['practicearea_list'] = PracticeArea.objects.prefetch_related('client_set')
            context['quote_list'] = Quote.objects.all
        else:
            context['practicearea_list'] = PracticeArea.published.prefetch_related('client_set')
            context['quote_list'] = Quote.published.all

        return context