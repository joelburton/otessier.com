from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import strip_tags

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from model_utils import Choices
from model_utils.models import StatusModel
from model_utils.models import TimeStampedModel
import watson


WORKFLOW_STATUS = Choices('private', 'published')


class SearchAdapter(watson.SearchAdapter):
    """Standard search adapter for our site."""

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_description(self, obj):
        return obj.description


###################################################################################################


class PracticeArea(TimeStampedModel, StatusModel, models.Model):
    """Consulting practice area."""

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        max_length=25,
        unique=True,
        help_text='Determines the URL. Do not change this after an item is published.',
    )

    title = models.CharField(
        max_length=40,
        unique=True,
    )

    short_description = models.CharField(
        max_length=100,
        unique=True,
        help_text='Appears on home page carousel.',
    )

    icon_name = models.CharField(
        max_length=15,
        unique=True,
        help_text='Font Awesome icon name (without the leading "fa-").',
    )

    description = models.TextField(
        help_text='Appears on listing page, but not on detail page.',
    )

    body = models.TextField()

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        ordering = ['position', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('practicearea.detail', kwargs={'slug': self.slug})


###################################################################################################


class Client(TimeStampedModel, StatusModel, models.Model):
    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        max_length=40,
        unique=True,
        help_text='Determines the URL. Do not change this after an item is published.',
    )

    title = models.CharField(
        max_length=40,
        unique=True,
        help_text='Short name of client, used throughout site.',
    )

    organization = models.CharField(
        max_length=70,
        unique=True,
        help_text='Long name for organization. Only used on client detail page.',
    )

    image = models.ImageField(
        upload_to='clients',
        help_text='Logo for client, which is resized automatically . Make as square as possible.',
    )

    image_display = ImageSpecField(
        source='image',
        processors=[ResizeToFit(180, 180)],
        format='PNG',
    )

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(90, 90)],
        format='PNG',
    )

    description = models.TextField(
        help_text='Short description of client and work. Show on listing and detail page.',
    )

    body = models.TextField()

    practiceareas = models.ManyToManyField(
        PracticeArea,
        verbose_name='practice areas',
        null=True,
    )

    url = models.URLField(
        max_length=100,
        blank=True,
        verbose_name='URL',
        help_text="URL for this client (don't forget the http://)."
    )

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('client.detail', kwargs={'slug': self.slug})


class ClientSearchAdapter(SearchAdapter):
    """Search adapater for clients."""

    def get_content(self, obj):
        """Content to search."""

        # Adds in info from reference and client work.
        results = super(SearchAdapter, self).get_content(obj)
        for ref in obj.clientreference_set.all():
            results += " " + (" ".join([ref.title, ref.job_title, ref.phone, ref.email]))
        for work in obj.clientwork_set.all():
            results += " " + (" ".join([work.title, work.description, work.body]))
        return results


class ClientReference(TimeStampedModel, models.Model):
    """Reference for a client project.

    References are associated with a client, but this is just to keep track of which
    client this reference goes with. The important (and visible to the public) association
    is with the ClientWork.
    """

    client = models.ForeignKey(
        Client,
    )

    title = models.CharField(
        max_length=40,
        verbose_name='name',
    )

    job_title = models.CharField(
        max_length=40,
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        max_length=40,
        blank=True
    )

    position = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['client', 'title']]
        ordering = ['position']

    def __str__(self):
        return self.title


class ClientWork(StatusModel, TimeStampedModel, models.Model):
    """Work project for a client."""

    STATUS = WORKFLOW_STATUS

    client = models.ForeignKey(
        Client
    )

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        help_text='Short description of work. Shows up in bold on client detail page.',
    )

    body = models.TextField(
        help_text='Long description of work. Shows up on client detail page.',
    )

    references = models.ManyToManyField(
        ClientReference,
        blank=True,
        help_text='References for this client work.',
    )

    position = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['client', 'title']]
        ordering = ['position']


###################################################################################################


class Consultant(TimeStampedModel, StatusModel, models.Model):
    """Consultant of firm."""

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        max_length=20,
        unique=True,
        help_text='Determines the URL. Do not change this after an item is published.',
    )

    title = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='name',
    )

    photo = models.ImageField(
        upload_to="consultants",
        null=True,
        blank=True,
        help_text='Resized automatically. Make as square as possible.',
    )

    photo_display = ImageSpecField(
        source='photo',
        processors=[ResizeToFit(180, 180)],
        format='JPEG',
    )

    photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[ResizeToFit(90, 90)],
        format='JPEG',
    )

    description = models.TextField(
        help_text='Short description of consultant. Shows on listing page and detail page.',
    )

    body = models.TextField()

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        ordering = ['position', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('consultant.detail', kwargs={'slug': self.slug})


###################################################################################################


class QAndA(TimeStampedModel, StatusModel, models.Model):
    """Nonprofit Question / Answer"""

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        unique=True,
        help_text='Determines the URL. Do not change this after an item is published.',
    )

    title = models.CharField(
        max_length=75,
        unique=True,
        help_text='Shows up in portlets, search results, and on the listing page.',
    )

    description = models.TextField(
        help_text='Short description of the question. Shows up on the listing page.',
    )

    question = models.TextField(
        help_text='Full question. Shows on the detail page.',
    )

    answer = models.TextField()

    credit = models.CharField(
        max_length=100,
        blank=True,
        help_text='Appears at bottom of answer. Used for providing publishing credit.',
    )

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        verbose_name = 'Question and Answer'
        ordering = ['position', '-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qanda.detail', kwargs={'slug': self.slug})


###################################################################################################


class Quote(TimeStampedModel, StatusModel, models.Model):
    """Quote about the firm. Used in the UI."""

    STATUS = WORKFLOW_STATUS

    quote = models.CharField(
        max_length=100,
    )

    author = models.CharField(
        max_length=75,
        help_text='Entire text for author, like "T.S. Eliot, Curmudgeon, Bank of England".',
    )

    class Meta:
        pass

    def __str__(self):
        return strip_tags(self.quote)


###################################################################################################


class LibraryCategory(TimeStampedModel, StatusModel, models.Model):
    """Category for library."""

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        unique=True,
        help_text='Determines the URL. Do not change this after an item is published.',
    )

    title = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        help_text='Description of category. Shows up on listing page and detail page.',
    )

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        verbose_name_plural = 'library categories'
        ordering = ['position', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('librarycategory.detail', kwargs={'slug': self.slug})


def file_upload_to(instance, filename):
    prefix = "library/"
    if "." in filename:
        junk, extension = filename.rsplit(".")
        return prefix + instance.slug + "." + extension
    else:
        return prefix + instance.slug


class LibraryFile(TimeStampedModel, StatusModel, models.Model):
    """File in the library."""

    STATUS = WORKFLOW_STATUS

    librarycategory = models.ForeignKey(
        LibraryCategory,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='Determines the URL. Do not change this after an item is published.',
    )

    title = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        help_text='Description of file/link. Shows up on category detail page.',
    )

    asset = models.FileField(
        upload_to=file_upload_to,
        blank=True,
        null=True,
        max_length=255,
        help_text='File asset.',
    )

    url = models.URLField(
        blank=True,
        max_length=255,
        help_text="Link URL (don't forget the http://)",
    )

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the correct URL for this item."""

        if self.asset:
            return self.asset.url
        return self.url


###################################################################################################


from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    email = models.EmailField(
        max_length=255,
        default='oliver@otessier.com',
        help_text='Email address shown on the site.',
    )

    about_footer = models.TextField(
        help_text='Appears in site footer.',
    )

    about_homepage = models.TextField(
        help_text='Appears on home page.',
    )

    phone = models.CharField(
        max_length=20,
        help_text='Appears in footer.',
    )

    def __str__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

    def phone_digits(self):
        """Reduces phone to just numbers; used for creating tel:// links."""

        return "".join([c for c in self.phone if c in "0123456789"])