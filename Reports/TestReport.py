from fpdf import FPDF
from datetime import date
from datetime import datetime
import json as json
import os as os


class TestReport(FPDF):

    def __init__(self, orientation='P', unit='mm', format='A4', folder=None, test_name=None):
        super(TestReport, self).__init__(orientation, unit, format)
        self.folder = folder
        self.test_name = test_name
        self.file_name = None

    def meta_data(self):
        self.set_title("Test Report")
        self.set_author("Kemal Altwlkany")

    def header(self):
        # Logo
        self.image('etfsa_en.png', 10, 8, 25)
        # Arial bold 15
        self.set_font('Arial', 'B', 14)
        # Move to the right
        self.cell(40)
        # Title
        self.cell(80, 10, self.test_name, 1, 0, 'C')
        self.cell(10)
        self.set_font('Arial', '', 10)
        self.cell(60, 10, datetime.now().strftime("%A, %d. %B %Y.  %H:%M:%S"))
        # Line break
        self.ln(20)

    def add_from_txt(self):
        self.add_page()
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        try:
            os.chdir(self.folder)
        except OSError:
            print('Could not cwd to: ', self.folder)
            print('Exiting.')
            return

        entries = os.listdir(self.folder)
        test_ID = len(entries)//2
        self.file_name = "BK1_test_ID_" + str(test_ID)
        self.set_font('Arial', '', 10)
        with open(self.file_name + '.txt', 'r') as json_file:
            data = json.load(json_file)
        self.write(5, json.dumps(data, indent=4))

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def add_image(self):
        self.image(self.file_name + '.png', w=200)


cwd = os.getcwd()
pdf = TestReport(folder="/home/kemal/Programming/Python/Preference_Articulation/Reports/TestResults/LocalSearch/LS_apriori/BK1", test_name='Local Search Apriori, BK1')
pdf.alias_nb_pages()
pdf.add_from_txt()
pdf.add_image()
os.chdir(cwd)
pdf.output('firstReport.pdf', 'F')
