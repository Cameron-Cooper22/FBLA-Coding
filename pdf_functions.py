# with help from geeksforgeeks.org https://www.geeksforgeeks.org/creating-pdf-documents-with-python/

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

class PDF:

    file_name: str
    document_title: str
    title: str
    sub_title: str
    text_lines: list[str]
    pdf: canvas.Canvas

    def __init__(self, file_name, document_title, title, sub_title, text_lines):
        self.file_name = file_name
        self.document_title = document_title
        self.title = title
        self.sub_title = sub_title
        self.text_lines = text_lines

    def create_pdf(self):
        self.pdf = canvas.Canvas()
        self.pdf.setTitle(self.document_title)
        self.pdf.setFont("Courier", 36)
        self.pdf.drawCentredString(300, 770, self.title)
        self.pdf.setFont("Courier-Bold", 24)
        self.pdf.drawCentredString(290, 720, self.subTitle)
        self.pdf.line(30, 710, 550, 710)
        text = self.pdf.beginText(40, 680)
        text.setFont("Courier", 18)
 
        for line in self.text_lines:
            text.textLine(line)
     
        self.pdf.drawText(text)
