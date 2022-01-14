import webbrowser

from filestack import Client
from fpdf import FPDF
import os

class PdfReport:
    """
    object that displays filename and generates split bill for 2 flatmates
    """

    def __init__(self, filename):
        self.filename=filename

    def generate(self,flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # border
        border=0

        #Add Image
        pdf.image('files/house.png', w=30, h=30)

        #Add title
        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=border, align='C', ln=1)

        #Add data
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=200, h=40, txt='Period:', border=border)
        pdf.cell(w=200, h=40, txt=bill.period, border=border, ln=1)

        # Add name and due amount of first flatmate1
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=200, h=25, txt=flatmate1.name, border=border)
        pdf.cell(w=200, h=25, txt=flatmate1_pay, border=border, ln=1)

        # Add name and due amount of first flatmate2
        pdf.cell(w=200, h=25, txt=flatmate2.name, border=border)
        pdf.cell(w=200, h=25, txt=flatmate2_pay, border=border, ln=1)

        pdf.output(f'files/{self.filename}')

        os.chdir('files')

        webbrowser.open(self.filename)

class FileSharer:
    def __init__(self, filepath, api_key = 'A02VK8NlFQEOKTKNf5bhbz'):
        self.filepath = filepath
        self.api_key = api_key

    def upload(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath = self.filepath)
        return new_filelink.url