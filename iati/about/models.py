from django.db import models

from wagtail.core.models import Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel

from modelcluster.fields import ParentalKey
from home.models import AbstractContentPage, AbstractIndexPage


class AboutPage(AbstractContentPage):
    """A model for the About landing page."""
    parent_page_types = ['home.HomePage']
    subpage_types = ['about.AboutSubPage', 'about.CaseStudiesIndexPage']


class AboutSubPage(AbstractContentPage):
    """A model for generic About subpages."""
    parent_page_types = ['about.AboutPage']
    subpage_types = []


class CaseStudiesIndexPage(AbstractIndexPage):
    """"A model for the Case Studies Index page."""
    parent_page_types = ['about.AboutPage']
    subpage_types = ['about.CaseStudyPage']

    @property
    def case_studies(self):
        """Get all CaseStudyPage objects that have been published."""
        case_studies = CaseStudyPage.objects.child_of(self).live()
        return case_studies


class CaseStudyPage(AbstractContentPage):
    """A model for Case Study pages."""
    parent_page_types = ['about.CaseStudiesIndexPage']
    subpage_types = []


class CaseStudyDocument(Orderable):
    page = ParentalKey(CaseStudyPage, related_name='case_study_documents')
    document = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.CASCADE,
        related_name='+'
    )
    panels = [
        DocumentChooserPanel('document'),
    ]
