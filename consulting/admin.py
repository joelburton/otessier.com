from django.contrib import admin
from django.db.models import Count

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


class PracticeAreaAdmin(admin.ModelAdmin):

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

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    def num_clients(self, obj):
        return obj.num_clients
    num_clients.short_description = "# Clients"

    def get_queryset(self, request):
        qs = PracticeArea.objects.show_private()
        return qs.annotate(num_clients=Count('client', distinct=True))

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"


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
    def get_queryset(self, request):
        return ClientWork.objects.show_private()


class ClientAdmin(admin.ModelAdmin):
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

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_queryset(self, request):
        return Client.objects.show_private()


class ConsultantAdmin(admin.ModelAdmin):
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

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_queryset(self, request):
        return Consultant.objects.show_private()


class QAndAAdmin(admin.ModelAdmin):

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

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_queryset(self, request):
        return QAndA.objects.show_private()


class QuoteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {
            'fields': ['quote', 'name', 'job_title', 'organization', 'status']}),
        ('Advanced', {
            'fields': ['id', 'created', 'modified', 'status_changed'],
            'classes': ['grp-collapse', 'grp-closed']})
    ]

    readonly_fields = ['id', 'created', 'modified', 'status_changed']

    list_display = ['quote', 'name', 'job_title', 'organization', 'active']
    list_display_links = ['quote']

    search_fields = ['quote', 'name', 'job_title', 'organization']

    list_filter = ['status']

    ordering = ['-id']

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_queryset(self, request):
        return Quote.objects


class LibraryCategoryAdmin(admin.ModelAdmin):

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

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    def get_queryset(self, request):
        return LibraryCategory.objects


class LibraryFileAdmin(admin.ModelAdmin):

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

    def active(self, obj):
        return obj.status == 'published'
    active.boolean = True
    active.short_description = "Active?"

    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/tinymce_setup.js']

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_queryset(self, request):
        return LibraryFile.objects.show_private()


admin.site.register(PracticeArea, PracticeAreaAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(QAndA, QAndAAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(LibraryCategory, LibraryCategoryAdmin)
admin.site.register(LibraryFile, LibraryFileAdmin)
