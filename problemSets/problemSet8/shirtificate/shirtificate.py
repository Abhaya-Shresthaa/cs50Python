
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=50)
name = input("Name: ")
pdf.cell(0,25,text=f"CS50 Shirtificate", align="C")
page_width = pdf.w  # A4 is 210mm
image_width = 185
x = (page_width - image_width)/2
pdf.image("shirtificate.png", x=x, y=60, w= image_width)
pdf.set_text_color(255,255,255)
pdf.set_font('helvetica', size=25)
pdf.set_y(120) 
pdf.cell(0,10,text=f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")