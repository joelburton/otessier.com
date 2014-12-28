from django.contrib import admin
from django.utils.html import strip_tags

from grappelli.forms import GrappelliSortableHiddenMixin

from .models import (
    PracticeArea,
    Client,
    ClientReference,
    ClientWork,
    QAndA, Quote,
    Consultant,
    LibraryFile,
    LibraryCategory,
)


class ModelAdmin(admin.ModelAdmin):
    """Common features of our admin models."""

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"


###################################################################################################


class PracticeAreaAdmin(ModelAdmin):

    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'description', 'body', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'num_clients', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'description', 'body']

    list_filter = ['status']

    ordering = ['position', 'title']

    def num_clients(self, obj):
        return obj.client_set.count()
    num_clients.short_description = "# Clients"


admin.site.register(PracticeArea, PracticeAreaAdmin)


###################################################################################################


class ClientReferenceInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = ClientReference
    extra = 0
    fields = ['name', 'job_title', 'phone', 'email', 'position']
    sortable_field_name = 'position'

    def get_queryset(self, request):
        return ClientReference.objects


class ClientWorkInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = ClientWork
    extra = 0
    fields = ['title', 'description', 'references', 'status', 'position']
    sortable_field_name = 'position'


class ClientAdmin(ModelAdmin):
    inlines = [ClientReferenceInline, ClientWorkInline]

    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'description', 'body', 'practiceareas', 'url',
                       'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'description', 'body', 'url']

    list_filter = ['status', 'practiceareas']

    ordering = ['position', '-created']


admin.site.register(Client, ClientAdmin)


###################################################################################################


class ConsultantAdmin(ModelAdmin):
    fieldsets = [
        ('', {
            'fields': ['name', 'slug', 'photo', 'description', 'body', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'name', 'description', 'body']

    list_filter = ['status']

    ordering = ['position', 'name']


admin.site.register(Consultant, ConsultantAdmin)


###################################################################################################


class QAndAAdmin(ModelAdmin):

    fieldsets = [
        ('', {
            'fields': ['title', 'slug', 'question', 'answer', 'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'question', 'answer']

    list_filter = ['status']

    ordering = ['position', '-created']


admin.site.register(QAndA, QAndAAdmin)


###################################################################################################


class QuoteAdmin(ModelAdmin):
    fieldsets = [
        ('', {
            'fields': ['quote', 'name', 'job_title', 'organization', 'status']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['quote_no_html', 'name', 'job_title', 'organization', 'active']
    list_display_links = ['quote_no_html']

    search_fields = ['quote', 'name', 'job_title', 'organization']

    list_filter = ['status']

    ordering = ['-id']

    def quote_no_html(self, obj):
        return strip_tags(obj.quote)


admin.site.register(Quote, QuoteAdmin)


###################################################################################################


class LibraryCategoryAdmin(ModelAdmin):

    fieldsets = [
        ('', {
            'fields': ['title']}),
        ('Advanced', {
            'fields': ['id'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    readonly_fields = ['id']

    list_display = ['title']
    list_display_links = ['title']

    search_fields = ['title']

    ordering = ['title']


admin.site.register(LibraryCategory, LibraryCategoryAdmin)


###################################################################################################


class LibraryFileAdmin(ModelAdmin):

    fieldsets = [
        ('', {
            'fields': ['librarycategory', 'title', 'slug', 'description', 'asset', 'url',
                       'status', 'position']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['slug', 'title', 'librarycategory', 'modified', 'position', 'active']
    list_display_links = ['slug', 'title']
    list_editable = ['position']

    search_fields = ['slug', 'title', 'title']

    list_filter = ['status']

    ordering = ['position', '-created']


admin.site.register(LibraryFile, LibraryFileAdmin)
