from consulting.models import Quote, QAndA


def random_quote(request):
    return {
        'random_quote': Quote.objects.first()  # FIXME
    }


def random_qanda(request):
    return {
        'random_qanda': QAndA.objects.first()  # FIXME
    }
