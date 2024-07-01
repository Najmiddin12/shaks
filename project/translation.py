from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Carousel)
class CarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'process_work')

@register(Testimonials)
class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('title_name', 'text',)

@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
