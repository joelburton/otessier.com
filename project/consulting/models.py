from pyexpat import model
from django.core.urlresolvers import reverse
from django.db import models

from model_utils import Choices
from model_utils.models import StatusModel
from model_utils.models import TimeStampedModel

WORKFLOW_STATUS = Choices('private', 'published')


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

    def show_private(self):
        return super(PublishedManager, self).get_queryset()


class PracticeArea(TimeStampedModel, StatusModel, models.Model):
    """Consulting practice area."""

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        max_length=20,
        unique=True,
    )

    title = models.CharField(
        max_length=30,
        unique=True,
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

    objects = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('practicearea.detail', kwargs={'slug': self.slug}) + (
            "?preview" if self.status == 'private' else "")


class Client(TimeStampedModel, StatusModel, models.Model):

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        max_length=40,
        unique=True,
    )

    title = models.CharField(
        max_length=40,
        unique=True,
    )

    description = models.TextField(
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
    )

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        pass

    objects = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('client.detail', kwargs={'slug': self.slug}) + (
            "?preview" if self.status == 'private' else "")


class ClientReference(TimeStampedModel, models.Model):
    """Reference for a client project.

    References are associated with a client, but this is just to keep track of which
    client this reference goes with. The important (and visible to the public) association
    is with the ClientWork.
    """

    client = models.ForeignKey(
        Client,
    )

    name = models.CharField(
        max_length=40,
    )

    job_title = models.CharField(
        max_length=40,
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    email = models.EmailField(
        max_length=40,
        blank=True
    )

    position = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['client', 'name']]
        ordering = ['position']

    def __str__(self):
        return self.name


class ClientWork(StatusModel, TimeStampedModel, models.Model):
    """Work project for a client."""

    STATUS = WORKFLOW_STATUS

    client = models.ForeignKey(
        Client
    )

    title = models.CharField(
        max_length=40,
    )

    description = models.TextField()

    references = models.ManyToManyField(
        ClientReference,
        blank=True,
    )

    position = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['client', 'title']]
        ordering = ['position']

    objects = PublishedManager()


class Consultant(TimeStampedModel, StatusModel, models.Model):
    """Consultant of firm."""

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        max_length=20,
        unique=True,
    )

    name = models.CharField(
        max_length=40,
        unique=True,
    )

    photo = models.ImageField(
        upload_to="consultants",
        null=True,
        blank=True,
    )

    description = models.TextField()

    body = models.TextField()

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        ordering = ['position', 'name']

    objects = PublishedManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consultant.detail', kwargs={'slug': self.slug}) + (
            "?preview" if self.status == 'private' else "")


    @property
    def title(self):
        return self.name


class QAndA(TimeStampedModel, StatusModel, models.Model):

    STATUS = WORKFLOW_STATUS

    slug = models.SlugField(
        unique=True,
    )

    title = models.CharField(
        max_length=75,
        unique=True,
    )

    question = models.TextField()

    answer = models.TextField()

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        verbose_name = 'Question and Answer'
        ordering = ['position', '-created']

    objects = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qanda.detail', kwargs={'slug': self.slug}) + (
            "?preview" if self.status == 'private' else "")


class Quote(TimeStampedModel, StatusModel, models.Model):
    """Quote about the firm. Used in the UI."""

    STATUS = WORKFLOW_STATUS

    quote = models.TextField()

    name = models.CharField(
        max_length=40,
    )

    job_title = models.CharField(
        max_length=40,
        blank=True,
    )

    organization = models.CharField(
        max_length=50,
        blank=True,
    )

    class Meta:
        pass

    objects = PublishedManager()

    def __str__(self):
        return self.quote


class LibraryCategory(models.Model):
    """Category for library."""

    title = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name_plural = 'library categories'

    def __str__(self):
        return self.title


class LibraryFile(TimeStampedModel, StatusModel, models.Model):
    """File in the library."""

    STATUS = WORKFLOW_STATUS

    librarycategory = models.ForeignKey(
        LibraryCategory,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    title = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
    )

    asset = models.FileField(
        upload_to='library',
        blank=True,
        null=True
    )

    url = models.URLField(
        blank=True,
    )

    position = models.PositiveSmallIntegerField(
        default=100,
    )

    # FIXME: type, size

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

