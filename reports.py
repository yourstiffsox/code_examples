from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

def generate_report(attatchment, title, paragraph):
    report = SimpleDocTemplate(attatchment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['h1'])
    body = Paragraph(paragraph, styles['BodyText'])
   
    report.build([report_title, body])
