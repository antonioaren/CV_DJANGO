from wagtail.blocks import StructBlock, CharBlock, TextBlock, StreamBlock


class ParagraphBlock(StructBlock):
    title = CharBlock(max_length=255)
    description = TextBlock()


class Paragraph(StructBlock):
    content = StreamBlock(
        [("media", ParagraphBlock())],
        min_num=2,
        max_num=2,
        label="Paragraph",
    )

    class Meta:
        template = "blocks/paragraph.html"
        label = "paragraph"
        help_text = "This a paragraph to add info"


class HomeBlocks(StreamBlock):
    paragraph = Paragraph()
