"""Module for registering model fields for translation, for use by django-modeltranslation."""

from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from home.translation_helper import add_language_content_panels
from .models import HomePage, StandardPage


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = HomePage.translation_fields


add_language_content_panels(HomePage)


@register(StandardPage)
class StandardPageTR(TranslationOptions):
    fields = StandardPage.translation_fields


add_language_content_panels(StandardPage)
