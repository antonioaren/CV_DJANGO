from wagtail.blocks import StructBlock, CharBlock, TextBlock, StreamBlock, RichTextBlock


class ParagraphBlock(StructBlock):
    description = RichTextBlock("")


class Paragraph(StructBlock):
    content = StreamBlock(
        [("paragraph", ParagraphBlock())],
        label="Paragraph",
    )

    class Meta:
        template = "blocks/paragraph.html"
        label = "paragraph"
        help_text = "This a paragraph to add info"


class HomeBlocks(StreamBlock):
    paragraph = Paragraph()
