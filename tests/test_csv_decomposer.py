import pytest
from csv_script.csv_decomposer import read_csv


def test_read_csv_returns_list_of_dicts():
    result = read_csv(['tests/test_data.csv'])
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)
    assert len(result) == 3


def test_read_csv_expected_columns():
    result = read_csv(['tests/test_data.csv'])
    expected_columns = ['name', 'position', 'completed_tasks', 'performance', 'skills', 'team', 'experience_years']
    assert all(col in result[0] for col in expected_columns)


def test_read_csv_multiple_files():
    result = read_csv(['tests/test_data.csv', 'tests/test_data2.csv'])
    assert len(result) == 7


def test_read_csv_returns_correct_data():
    result = read_csv(['tests/test_data.csv'])
    assert result[0]['name'] == 'David Bowie'
    assert result[0]['position'] == 'Frontend Developer'