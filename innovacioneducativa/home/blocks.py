# coding: utf-8

from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        #template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    encabezado = CharBlock(classname="title", required=True)
    nivel = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        #template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
    texto = TextBlock()
    nombre_autor = CharBlock(
        blank=True, required=False, label='e.g. Guy Picciotto')

    class Meta:
        icon = "fa-quote-left"
        #template = "blocks/blockquote.html"



class BlockParrafo(StructBlock):
    """
    Custom `StructBlock` clase del div y texto
    """
    clase = CharBlock(required=False, help_text="Clase del div para la hoja de estilos")
    texto = RichTextBlock(help_text="Texto del bloque")
    
    class Meta:
        icon = "fa-paragraph"
        #template="blocks/paragraph_block.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = BlockParrafo()
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="fa-s15",
        #template="blocks/embed_block.html"
        )
