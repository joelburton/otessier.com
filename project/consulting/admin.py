from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline
from django.db import models
from tinymce.widgets import TinyMCE
from consulting.forms import PracticeAreaForm, ClientWorkForm, ClientForm, ConsultantForm, QAndAForm, \
    LibraryCategoryForm, LibraryFileForm, SiteConfigurationForm

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
)


admin.site.site_header = "Oliver Tessier & Associates"


class ModelAdmin(admin.ModelAdmin):
    """Common features of our admin models."""

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE}
    # }

    class Media:
        js = ['http://tinymce.cachefly.net/4.1/tinymce.min.js']


###################################################################################################


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


admin.site.register(PracticeArea, PracticeAreaAdmin)


###################################################################################################


class ClientReferenceInline(admin.TabularInline, SortableInline):
    model = ClientReference
    extra = 0
    fields = ['title', 'job_title', 'phone', 'email', 'position']


class ClientWorkInline(admin.StackedInline, SortableInline):
    model = ClientWork
    form = ClientWorkForm
    extra = 0
    fields = ['title', 'description', 'body', 'references', 'status', 'position']
    sortable_field_name = 'position'


    def get_field_queryset(self, db, db_field, request):
        """Get queryset for the references field that relies on references for this client."""

        if db_field.name == 'references':
            if request._obj:
                return ClientReference.objects.filter(client_id=request._obj.id)
            else:
                # This is a new client, so show an empty list for references
                return ClientReference.objects.none()
        return super(ClientWorkInline, self).get_field_queryset(db, db_field, request)


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

    # XXX: don't know if I want, but it's a nice bit of code
    #
    # def get_inline_instances(self, request, obj=None):
    #     """Don't show ClientWork inline on object creation."""
    #
    #     inlines = super(ClientAdmin, self).get_inline_instances(request, obj)
    #     if not obj:
    #         return [inline for inline in inlines if not isinstance(inline, ClientWorkInline)]
    #     else:
    #         return inlines

    def get_form(self, request, obj=None, **kwargs):
        # Hook into this to put the client object on the request, so we can use it in
        # ClientWorkInline's get_field_queryset
        request._obj = obj
        return super(ClientAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Client, ClientAdmin)


###################################################################################################


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


admin.site.register(Consultant, ConsultantAdmin)


###################################################################################################


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


admin.site.register(QAndA, QAndAAdmin)


###################################################################################################


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


admin.site.register(Quote, QuoteAdmin)


###################################################################################################


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


admin.site.register(LibraryCategory, LibraryCategoryAdmin)


###################################################################################################


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


admin.site.register(LibraryFile, LibraryFileAdmin)


###################################################################################################


from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration


class SiteConfigurationAdmin(SingletonModelAdmin):
    form = SiteConfigurationForm
    class Media:
        js = ['http://tinymce.cachefly.net/4.1/tinymce.min.js']


admin.site.register(SiteConfiguration, SiteConfigurationAdmin)