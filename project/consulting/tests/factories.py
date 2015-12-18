import factory
from django.utils.text import slugify

from consulting import models


class PracticeAreaFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.PracticeArea
        django_get_or_create = ['title']

    title = "Coaching"
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    short_description = factory.LazyAttribute(lambda x: "Short Description of %s" % x.title)
    icon_name = factory.LazyAttribute(lambda x: slugify(x.title))
    description = "Description of PracticeArea."
    body = "<p>PracticeArea body.</p>"
    position = 1


class ClientFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Client
        django_get_or_create = ['slug']

    title = "IBM"
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    image = factory.django.ImageField(filename="client.jpg")
    description = "Client Description"
    body = "<p>Client body</p>"
    # practiceareas
    url = "http://ibm.com"
    position = factory.Sequence(lambda x: x)


class ClientReferenceFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ClientReference
        django_get_or_create = ["title"]

    title = "Herman Miller"
    job_title = "Designer"
    phone = "(415) 555-1212"
    email = "herman@miller.com"
    position = factory.Sequence(lambda x: x)


class ClientWorkFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ClientWork
        django_get_or_create = ["client", "title"]

    client = factory.SubFactory(ClientFactory)
    title = "Coaching Project"
    description = "Client work description."
    body = "<p>Client work body.</p>"
    # references
    position = factory.Sequence(lambda x: x)


class ConsultantFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Consultant
        django_get_or_create = ['title']

    title = "Joel Burton"
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    photo = factory.django.ImageField(filename="consultant.jpg")
    description = "Description of Consultant."
    body = "<p>Body of consultant.</p>"
    position = 1


class QAndAFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.QAndA
        django_get_or_create = ['title']

    title = "Why do birds sing?"
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    description = "Description of QAndA."
    question = factory.LazyAttribute(lambda x: x.title)
    answer = "<p>QAndA Answer</p>"
    credit = "Copyright by Joel"
    position = factory.Sequence(lambda x: x)


class QuoteFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Quote
        django_get_or_create = ['quote', 'author']

    quote = "Oliver is love."
    author = 'Gandhi'


class LibraryCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.LibraryCategory
        django_get_or_create = ['title']

    title = "Sample Budgets"
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    description = "Description of LibraryCategory."
    position = factory.Sequence(lambda x: x)


class LibraryFileFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.LibraryFile
        django_get_or_create = ['title', 'librarycategory']

    librarycategory = factory.SubFactory(LibraryCategoryFactory)
    title = "Sample Annual Budget"
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    description = "Description of LibraryFile."
    asset = factory.django.FileField(filename="libraryfile.txt")
    url = "http://url.com/libraryfile"
    position = factory.Sequence(lambda x: x)
