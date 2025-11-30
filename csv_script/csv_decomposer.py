import csv


def read_csv(file_paths: list[str]):
    result = []
    for path in file_paths:
        try:
            with open(path) as file:
                dict_csv = csv.DictReader(file)
                result.extend(list(dict_csv))
        except csv.Error as e:
            raise ValueError(f'Error reading CSV file {path}: {e}')
    return result