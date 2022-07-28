from cProfile import label
from email.mime import image
from re import template
from tkinter import Image
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50, 
        default='More details'
    )
    internal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )
        
class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100, 
        help_text="Bold title text for this card. Max length of 100 characters.",
    )
    text = blocks.TextBlock(
        max_length=255, 
        help_text="Optional text for this card. Max length is 255 characters",
        required=False
    )
    image = ImageChooserBlock(
        help_text="Images will be automatically cropped 570px by 370px",
    )
    link = Link(
        help_text="Enter a link or select a page"
    )
 

class CardsBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        Card()
    )

    class Meta: 
        template = "blocks/cards_block.html"
        icon = "image"
        label = "Standard Card"
        help_text = "Card with title and text"

"""
class Card(blocks.StructBlock):
    paragraph = blocks.RichTextBlock(label='Paragraphe')
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/card.html'
        icon = 'placeholder'
        label = 'Card'
"""
class ColumnBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock(label='Paragraphe')
    image = ImageChooserBlock()
    # card = Card()

    class Meta:
        template = 'blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):
    position = blocks.ChoiceBlock(choices=[
        ('left', '70%-30%'),
        ('middle', '50%-50%'),
        ('right', '30%-70%')
    ], label="Disposition des colonnes")
    left_column = ColumnBlock(icon='arrow-left', label='Colonne de gauche')
    right_column = ColumnBlock(icon='arrow-right', label='Colonne de droite')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Deux Colonnes'


class ThreeColumnBlock(blocks.StructBlock):
    left_column = ColumnBlock(icon='arrow-left', label='Colonne de gauche')
    middle_column = ColumnBlock(label='Colonne centrale')
    right_column = ColumnBlock(icon='arrow-right', label='Colonne de droite')

    class Meta:
        template = 'blocks/three_column_block.html'
        icon = 'placeholder'
        label = 'Trois Colonnes'
