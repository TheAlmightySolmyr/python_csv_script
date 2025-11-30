import pytest
import csv
from unittest.mock import mock_open, patch
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


def test_read_csv_invalid_format():
    invalid_csv_content = "name,position\nvalue1,value2,value3\n"
    
    with patch('builtins.open', mock_open(read_data=invalid_csv_content)):
        with patch('csv.DictReader') as mock_reader:
            mock_reader.side_effect = csv.Error("CSV format error")
            
            with pytest.raises(ValueError, match="Error reading CSV file"):
                read_csv(['test.csv'])


def test_read_csv_empty_file():
    empty_content = ""
    
    with patch('builtins.open', mock_open(read_data=empty_content)):
        with patch('csv.DictReader') as mock_reader:
            mock_reader.return_value = []
            
            result = read_csv(['empty.csv'])
            assert result == []