from django.contrib import admin
from .models import Contact, About, Image, Region, Results
from django.utils.safestring import mark_safe


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'link')
    search_fields = ('name',)
    readonly_fields = ('preview', 'link')

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" style="max-height: 200px;">')

    preview.short_description = 'Предпросмотр'
    preview.allow_tags = True

    def link(self, obj):
        return mark_safe(obj.img.url)

    link.short_description = 'Cсылка'
    link.allow_tags = True


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'preview')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('preview',)
    fieldsets = (
        ("Основная информация", {"fields": ('first_name', 'last_name', 'img','preview')}),
        ("Роль в проекте", {"fields": ('role', 'description')}),
    )
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" style="max-height: 200px;">')

    preview.short_description = 'Предпросмотр'
    preview.allow_tags = True


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    fieldsets = (
        ("Основная информация", {"fields": ('name', 'status')}),
        ("Содержание", {"fields": ('html',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name"),
            },
        ),
    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    fieldsets = (
        ("Основная информация", {"fields": ('name', 'status')}),
        ("Содержание", {"fields": ('html',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name"),
            },
        ),
    )


@admin.register(Results)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    fieldsets = (
        ("Основная информация", {"fields": ('name', 'status')}),
        ("Содержание", {"fields": ('html',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name"),
            },
        ),
    )
