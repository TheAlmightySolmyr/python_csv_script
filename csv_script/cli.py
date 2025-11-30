import argparse

from tabulate import tabulate

from csv_script.csv_decomposer import read_csv
from csv_script.report_generator.generator import ReportGenerator

CHOICES = ['performance']


def cli_main():
    parser = argparse.ArgumentParser(description='Report generator')
    parser.add_argument('--files', type=str, nargs='+', required=True, 
                        help='path to the csv file')
    parser.add_argument('--report', type=str, required=True, 
                        choices=CHOICES,
                        help='metric of the report')
    args = parser.parse_args()
    read = read_csv(args.files)
    report = ReportGenerator(read).choose_rep_type(args.report)
    print(tabulate(report, headers='keys', showindex=range(1, len(report) + 1)))

    