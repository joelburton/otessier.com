import re
from django.core.exceptions import ValidationError

from django.core.urlresolvers import reverse
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from model_utils import Choices
from model_utils.models import StatusModel
from model_utils.models import TimeStampedModel
import watson
from solo.models import SingletonModel


WORKFLOW_STATUS = Choices('private', 'published')


class SearchAdapter(watson.SearchAdapter):
    """Standard search adapter for our site."""

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_description(self, obj):
        return obj.description

    def get_model_name(self, obj):
        return obj._meta.verbose_name.title()


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
        blank=True,
        help_text='Organization full name. Used on detail page. If blank, title is used.',
    )

    image = models.ImageField(
        upload_to='clients',
        blank=True,
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

    body = models.TextField(
        help_text='Full text. Appears on client detail page.',
        blank=True,
    )

    practiceareas = models.ManyToManyField(
        PracticeArea,
        verbose_name='practice areas',
        blank=True,
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
        ordering = ['position', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('client.detail', kwargs={'slug': self.slug})


class ClientSearchAdapter(SearchAdapter):
    """Search adapter for clients.

    Adds in info from references and client work.
    """

    def get_content(self, obj):
        """Content to search."""

        def _mash(lst, attrs):  # _mashfrom c(cats, ['name', 'color']) => 'auden grey ezra orange'
            return " !1".join(" !2".join(getattr(obj, a) for a in attrs) for obj in lst)

        return " ".join([super(SearchAdapter, self).get_content(obj),
                         _mash(obj.clientreference_set.all(), ['job_title', 'phone', 'email']),
                         _mash(obj.clientwork_set.all(),      ['title', 'description', 'body'])])


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
        blank=True,
        help_text='Not shown to site viewers.',
    )

    email = models.EmailField(
        max_length=40,
        blank=True
    )

    position = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        unique_together = [['client', 'title']]
        ordering = ['position', 'created']

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
        blank=True,
    )

    references = models.ManyToManyField(
        ClientReference,
        blank=True,
        help_text='References for this client work.',
    )

    position = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        unique_together = [['client', 'title']]
        ordering = ['position', 'created']

    def __str__(self):
        return self.title


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
        ordering = ['position', '-id']

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
        return self.quote


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
    """Store file upload in library/ with name from slug and original extension.

    i.e., Joe Biden's 'my resume.txt' -> joe-biden.txt
    """

    extension = re.search(r'\.[a-zA-Z0-9]{1,6}$|', filename).group(0)
    return "library/" + instance.slug + extension


class LibraryFile(TimeStampedModel, StatusModel, models.Model):
    """File in the library."""

    STATUS = WORKFLOW_STATUS

    librarycategory = models.ForeignKey(
        LibraryCategory,
        verbose_name='library category',
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
        default='<p>hello</p>',
    )

    asset = models.FileField(
        upload_to=file_upload_to,
        blank=True,
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
        ordering = ['position', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the correct URL for this item."""

        return self.asset.url if self.asset else self.url

    def clean(self):
        """Ensure that either a file or URL is provided."""

        super(LibraryFile, self).clean()

        if not self.asset and not self.url:
            raise ValidationError("Must have either a file or a URL.")


###################################################################################################


class SiteConfiguration(SingletonModel):
    """Site configuration singleton.

    A good place to store Oliver-editable sitewide stuff.
    """

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

    class Meta:
        verbose_name = "Site Configuration"

    def __str__(self):
        return u"Site Configuration"

    def phone_digits(self):
        """Reduces phone to just numbers; used for creating tel:// links."""

        return re.sub(r'\D', '', self.phone)

    def get_absolute_url(self):
        return "/"