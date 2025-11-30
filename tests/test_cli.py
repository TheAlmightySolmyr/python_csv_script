import pytest

from csv_script.cli import validate_files


def test_validate_files_with_real_file():
    validate_files(['tests/test_data.csv'])


def test_validate_files_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        validate_files(['file_which_does_not_exist.csv'])


def test_validate_files_with_directory():
    with pytest.raises(ValueError):
        validate_files(['tests/'])


def test_validate_files_empty_list():
    validate_files([])


def test_validate_files_multiple_real_files():
    validate_files(['tests/test_data.csv', 'tests/test_data.csv'])