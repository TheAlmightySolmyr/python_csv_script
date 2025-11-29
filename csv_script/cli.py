import argparse

CHOICES = ['performance']


def cli_main():
    parser = argparse.ArgumentParser(description='Report generator')
    parser.add_argument('--files', type=str, nargs='+', required=True, 
                        help='path to the csv file')
    parser.add_argument('--report', type=str, required=True, 
                        choices=CHOICES,
                        help='metric of the report')
    args = parser.parse_args()

    return args