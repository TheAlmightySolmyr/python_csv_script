import argparse
import os

from tabulate import tabulate

from csv_script.csv_decomposer import read_csv
from csv_script.report_generator.generator import ReportGenerator

CHOICES = ['performance',
           'gdp']


def validate_files(file_paths):
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found")
        if not os.path.isfile(file_path):
            raise ValueError(f"'{file_path}' is not a file")
    return True


def cli_main():
    parser = argparse.ArgumentParser(description='Report generator')
    parser.add_argument('--files', type=str, nargs='+', required=True, 
                        help='path to the csv file')
    parser.add_argument('--report', type=str, required=True, 
                        choices=CHOICES,
                        help='metric of the report')
    args = parser.parse_args()
    validate_files(args.files)
    read = read_csv(args.files)
    report = ReportGenerator(read).choose_rep_type(args.report)
    print(tabulate(report, headers='keys', tablefmt='grid', 
                   showindex=range(1, len(report) + 1)))

    