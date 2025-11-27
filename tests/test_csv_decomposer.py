from csv_script import csv_decomposer as cr
import pytest


class TestCsvDecomposer:
    def test_one_csv_file(self):
        assert len(cr.read_csv(['tests/test_data.csv'])) == 3
        assert cr.read_csv(['tests/test_data.csv'])[0]['name'] == 'David Bowie'
