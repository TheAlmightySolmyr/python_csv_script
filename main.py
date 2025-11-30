from csv_script.cli import cli_main
from csv_script.csv_decomposer import read_csv
from csv_script.report_generator.generator import ReportGenerator


def main():
    args = cli_main()
    read = read_csv(args.files)
    report = ReportGenerator(read).choose_rep_type(args.report)
    print (report)



if __name__ == '__main__':
    main()