import argparse

def main():
    parser = argparse.ArgumentParser(description='Report generator')
    parser.add_argument('--files', type=str, nargs='+', help='path to the file')
    parser.add_argument('--report', type=str, help='set name for the report')

    args = parser.parse_args()
    
if __name__ == '__main__':
    main()