from pydoc import classname
from tempfile import template
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from .blocks import CardsBlock, TwoColumnBlock, ThreeColumnBlock, CardsBlock, Card  

class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    max_count = 1

    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text='Sous-titre'
        )
    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Lien optionnel',
        on_delete=models.SET_NULL,
        )
    button_text = models.CharField(
        max_length=50,
        default='En savoir plus',
        blank=False,
        help_text='Texte du Bouton',
        )
    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Image de la banière',
        on_delete=models.SET_NULL,
        )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(
            label='Paragraphe', features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr']
        )),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('cards', CardsBlock()),
        ('large_image', ImageChooserBlock(
            help_text='Cette image va être rognée de 1400px par 300px',
            template="blocks/large_image_block.html"
        )),
        ('small_image', ImageChooserBlock(
            help_text='Cette image va être rognée de 1400px par 300px',
            template="blocks/small_image_block.html"
        )),
        
    ], verbose_name='Contenu', null=True)

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel('body', classname="full"),
    ]
    

class ClassicPage(Page):
    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        help_text='Image de la banière',
        on_delete=models.SET_NULL,
        )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(
            label='Paragraphe', features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr']
        )),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('cards', CardsBlock()),
        
    ], verbose_name='Contenu')

    content_panels = Page.content_panels + [
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = "Page classique"