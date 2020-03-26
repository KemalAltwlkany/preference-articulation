from fpdf import FPDF
from datetime import date
from datetime import datetime
import json as json
import os as os
from TestReport import TestReport
import sys


class ReportGenerator():
    rel_path = "/home/kemal/Programming/Python/Preference_Articulation/Reports/TestResults"
    # this is where all test results are located. (the raw data, .txt and .png)

    def __init__(self, reportType=None, alg_family=None, alg_name=None, problem_name=None, save_folder=None):
        self.reportType = reportType
        self.alg_family = alg_family
        self.alg_name = alg_name
        self.problem_name = problem_name
        self.load_folder = ""
        self.save_folder = save_folder
        self.file_names = []

    def setupVariables(self):
        # This function prepares the data such as setting up load/save folder paths, and determining the files
        # to be processed
        # Find raw data folder
        self.load_folder = os.path.join(ReportGenerator.rel_path, self.alg_family, self.alg_name, self.problem_name)
        if not os.path.exists(self.load_folder):
            os.makedirs(self.load_folder)
        try:
            os.chdir(self.load_folder)
        except OSError:
            print('Could not cwd to: ', self.load_folder)
            print('Exiting.')
            sys.exit(1)

        # Create save_folder if it does not exist
        if self.save_folder is None:
            self.save_folder = os.path.join(ReportGenerator.rel_path, "Reports", self.alg_name, self.problem_name)
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)

        if self.reportType is "latest":
            # Reports have a unique ID. The latest report has the highest ID value.
            entries = os.listdir(self.load_folder)
            test_ID = len(entries) // 2
            self.file_names.append(self.problem_name + "_test_ID_" + str(test_ID))
        elif self.reportType is "all":
            entries = os.listdir(self.load_folder)
            n_tests = len(entries) // 2
            for test_ID in range(n_tests):
                self.file_names.append(self.problem_name + "_test_ID_" + str(test_ID))
        elif self.reportType is "new":
            entries = os.listdir(self.load_folder)
            n_tests = len(entries) // 2

            # we now check how many reports exist in the save folder
            n_reports = os.listdir(self.save_folder)
            n_reports = len(n_reports)
            for test_ID in range(n_reports-1, n_tests, 1):
                self.file_names.append(self.problem_name + "_test_ID_" + str(test_ID))

    def generateReports(self):
        for file_name in self.file_names:
            pdf = TestReport(raw_data_folder=self.load_folder, file_name=file_name)
            pdf.alias_nb_pages()
            pdf.add_from_txt()
            pdf.add_image()
            os.chdir(self.save_folder)
            pdf.output("r_" + file_name + '.pdf', 'F')


if __name__ == '__main__':
    x = ReportGenerator(reportType="new", alg_family="LocalSearch", alg_name="LS_apriori", problem_name="BK1")
    x.setupVariables()
    x.generateReports()

