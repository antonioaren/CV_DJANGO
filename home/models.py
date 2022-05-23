from django.db import models
from wagtail.admin.panels import StreamFieldPanel

from wagtail.core.models import Page
from wagtail.fields import StreamField

from home.blocks import HomeBlocks


class HomePage(Page):
    content = StreamField(
        HomeBlocks(),
        null=True,
        blank=True,
        verbose_name="Content",
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Home page"
