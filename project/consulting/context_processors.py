from random import choice

from consulting.models import Quote, QAndA

from django.core.cache import cache


def random_quote(request):
    quotes = cache.get('quotes')
    if not quotes:
        quotes = Quote.published.values('quote', 'author').order_by()
        cache.set('quotes', quotes)

    return {
        'random_quote': choice(quotes)
    }


def random_qanda(request):
    qandas = cache.get('qandas')
    if not qandas:
        qandas = QAndA.published.only('title', 'slug', 'description').order_by()
        cache.set('qandas', qandas)

    return {
        'random_qanda': choice(qandas)
    }
