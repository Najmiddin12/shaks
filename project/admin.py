from django.contrib import admin
from .models import Links, Contact, Carousel, Service, ServicePhoto, Portfolio, PortfolioPhoto, PortfolioVideo, Testimonials, Team, Blog, Creator
from modeltranslation.admin import TranslationAdmin

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ("name", "url",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email_1", "email_1", "phone_1", "phone_2")

@admin.register(Carousel)
class CarouselAdmin(TranslationAdmin):
    list_display = ("title", "text",)

class ServicePhotoInline(admin.TabularInline):
    model = ServicePhoto
    extra = 1

class ServiceAdmin(TranslationAdmin):  # Use TranslationAdmin here
    inlines = [ServicePhotoInline,]

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicePhoto)

class PortfolioPhotoInline(admin.TabularInline):
    model = PortfolioPhoto
    extra = 1

class PortfolioVideoInline(admin.TabularInline):
    model = PortfolioVideo
    extra = 1

class PortfolioAdmin(TranslationAdmin):  # Use TranslationAdmin here
    inlines = [PortfolioPhotoInline, PortfolioVideoInline]

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioPhoto)
admin.site.register(PortfolioVideo)

@admin.register(Testimonials)
class TestimonialsAdmin(TranslationAdmin):
    list_display = ("title_name", "img", "text")

@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ("name", "img", "facebook", "instagram", "telegram", "whatsapp")

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ("title", "text", "img")

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ("mirzoahmad_url", "najmiddin_url",)
