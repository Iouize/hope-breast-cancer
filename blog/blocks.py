from cProfile import label
from re import template
from tkinter import Image
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
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

