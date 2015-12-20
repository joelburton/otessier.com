from django import forms
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline
from django.db import models
from solo.admin import SingletonModelAdmin

from .forms import PracticeAreaForm, ClientWorkForm, ClientForm, ConsultantForm, QAndAForm, \
    LibraryCategoryForm, LibraryFileForm, SiteConfigurationForm, ClientReferenceForm

from .models import (
    PracticeArea,
    Client,
    ClientReference,
    ClientWork,
    QAndA,
    Quote,
    Consultant,
    LibraryFile,
    LibraryCategory,
    SiteConfiguration,
)

admin.site.site_header = "Oliver Tessier & Associates"


class ModelAdmin(admin.ModelAdmin):
    """Common features of our admin models."""

    def active(self, obj):
        return obj.status == 'published'

    active.boolean = True
    active.short_description = "Active?"

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple}
    }


###################################################################################################


@admin.register(PracticeArea)
class PracticeAreaAdmin(ModelAdmin):
    form = PracticeAreaForm
    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'short_description', 'icon_name',
                       'description', 'body', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'short_description', 'modified', 'num_clients',
                    'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'description', 'body']

    list_filter = ['status']

    def num_clients(self, obj):
        return obj.client_set.count()

    num_clients.short_description = "# Clients"


###################################################################################################


class ClientReferenceInline(admin.TabularInline, SortableInline):
    model = ClientReference
    extra = 0
    fields = ['title', 'job_title', 'phone', 'email', 'position']
    form = ClientReferenceForm


class ClientWorkInline(admin.StackedInline, SortableInline):
    model = ClientWork
    form = ClientWorkForm
    extra = 0
    fields = ['title', 'description', 'body', 'references', 'status', 'position']
    sortable_field_name = 'position'

    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple}
    }

    def get_formset(self, request, obj=None, **kwargs):
        """Filter client references down to the ones that match this client."""

        formset = super(ClientWorkInline, self).get_formset(request, obj, **kwargs)
        references = formset.form.base_fields['references']
        references.queryset = references.queryset.filter(client=obj)
        return formset


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    form = ClientForm
    inlines = [ClientReferenceInline, ClientWorkInline]

    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'organization', 'image', 'description', 'body',
                       'practiceareas', 'url', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'description', 'body', 'url']

    list_filter = ['status', 'practiceareas']


###################################################################################################


@admin.register(Consultant)
class ConsultantAdmin(ModelAdmin):
    form = ConsultantForm
    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'photo', 'description', 'body', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'description', 'body']

    list_filter = ['status']


###################################################################################################


@admin.register(QAndA)
class QAndAAdmin(ModelAdmin):
    form = QAndAForm
    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'description', 'question', 'answer', 'credit',
                       'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'question', 'answer']

    list_filter = ['status']


###################################################################################################


@admin.register(Quote)
class QuoteAdmin(ModelAdmin):
    fieldsets = [
        ('', {
            'fields': ['quote', 'author', 'status']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['quote', 'author', 'active']
    list_display_links = ['quote']

    search_fields = ['quote', 'author']

    list_filter = ['status']

    ordering = ['-id']


###################################################################################################


@admin.register(LibraryCategory)
class LibraryCategoryAdmin(ModelAdmin):
    form = LibraryCategoryForm
    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'description', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['title', 'position', 'active']
    list_display_links = ['title']
    list_editable = ['position']

    search_fields = ['title', 'slug', 'description']


###################################################################################################


@admin.register(LibraryFile)
class LibraryFileAdmin(ModelAdmin):
    form = LibraryFileForm

    fieldsets = [
        ('', {
            'fields': ['librarycategory', 'title', 'slug', 'description', 'asset', 'url',
                       'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['collapse']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'librarycategory', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'description']

    list_filter = ['status']


###################################################################################################


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    form = SiteConfigurationForm
