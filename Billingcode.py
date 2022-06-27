from fpdf import FPDF

#gather bill data
windows = int(input("Number of windows "))
Entry_doors = int(input("Number of entry doors "))
french_doors = int(input("Number of french doors "))
sgd = int(input("Number of sliding glass doors "))
sgd_extra = int(input("Number of extra panels "))
extra_labor = int(input("Hours of extra work "))
receipts = int(input('Receipt total '))
if input('Measure fee? ') == 'yes':
    measure = 125
else:
    measure = 0
customer = input('Job name ')
file_name = customer + 'bill.pdf'
pdf = FPDF()
#create totals
win_total = windows * 125
entry_total = Entry_doors * 300
french_total = french_doors * 400
sgd_total = sgd * 300
extra_total = extra_labor * 80
sgd_extra_total = sgd_extra * 50
total = win_total + entry_total + french_total + sgd_total + extra_total + sgd_extra_total + measure + receipts
#make pdf
from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
top = pdf.y
offset = pdf.x + 40

def create_row(col_1, col_2, col_3, y):
    pdf.multi_cell(40,10, col_1,1,0)
    pdf.x = offset
    pdf.y = top + y
    pdf.multi_cell(40,10, str(col_2),1,0)
    pdf.x = offset + 40
    pdf.y = top + y
    pdf.multi_cell(40,10, str(col_3),1,0)

#create header
pdf.multi_cell(120,10, customer,1,0)
# create first row
create_row('Type', 'Number', 'Total', 10)
#create second row
create_row('windows', windows, win_total, 20)
#create third row
create_row('Entry doors', Entry_doors, entry_total, 30)
#create fourth row
create_row('French doors', french_doors, french_total, 40)
#create fith row
create_row('Sliding doors', sgd, sgd_total, 50)
#create sixth row
create_row('Extra panels', sgd_extra, sgd_extra_total, 60)
#create seventh row
create_row('Hours labor', extra_labor, extra_total, 70)
#create eighth row
create_row('Receipts', ' ', receipts, 80)
#create ninth row
create_row('Measure', ' ', measure, 90)
#create total row
pdf.x = offset + 40
pdf.multi_cell(40,10, str(total),1,0)

pdf.output(file_name)
