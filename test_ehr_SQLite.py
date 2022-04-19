"""Test EHR_SQLite.py."""

from ehr_SQLite import (
    num_older_than,
    sick_patients,
    first_age,
)


def test_num_older_than():
    """Test the num_older_than function."""
    assert num_older_than(23) == 5
    assert num_older_than(25) == 4
    assert num_older_than(30) == 0


def test_sick_patients():
    """Test the sick_patients function."""
    assert sick_patients("METABOLIC: GLUCOSE", ">", 1) == [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    ]
    assert sick_patients("CBC: RED BLOOD CELL COUNT", ">", 5) == [
        "DB22A4D9-7E4D-485C-916A-9CD1386507FB"
    ]


def test_first_age():
    """Test the first_age function."""
    assert first_age("1A8791E3-A61C-455A-8DEE-763EB90C9B2C") == 3
