from random import randint

from consulting.models import Quote, QAndA, Consultant, PracticeArea


def random_quote(request):
    quotes = Quote.objects.all()
    return {
        'random_quote': quotes[randint(0, quotes.count()-1)]
    }


def random_qanda(request):
    qandas = QAndA.objects.all()
    return {
        'random_qanda': qandas[randint(0, qandas.count()-1)]
    }


def site_navigation(request):
    return {
        'site_consultants': Consultant.published.all(),
        'site_practiceareas': PracticeArea.published.all(),
    }