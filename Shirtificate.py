
from fpdf import FPDF

class PDF(FPDF):
#piyushgopal
    def header(self):
        # Setting image location pox (x/y), width/height,
        self.image("shirtificate.png", 10, 65, 190, 190)
#piyushgopal
        # text styling
        self.set_font("helvetica", "B", 45)
#piyushgopal
        # text alignment
        self.text(45, 45, "CS50 Shirtificate")
#piyushgopal
    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255,255,255)
        self.text(72, 140, name + " took CS50")

# creating and output of pdf
name = input("what's your name? ")
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
