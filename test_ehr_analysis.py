"""
Test the ehr_analysis module part 1. No particular function is needed to test
the parse_data function because it is used in the other two test functions.
"""
from ehr_analysis import (
    parse_labs,
    parse_patients,
    num_older_than,
    sick_patients,
    first_age,
)


def test_num_older_than():
    """Test the num_older_than function."""
    assert num_older_than(23, parse_patients("patient_test.txt")) == 5
    assert num_older_than(25, parse_patients("patient_test.txt")) == 4
    assert num_older_than(30, parse_patients("patient_test.txt")) == 0


def test_sick_patients2():
    """Test the sick_patients function."""
    assert sick_patients("METABOLIC: GLUCOSE", ">", 1, parse_labs("lab_test.txt")) == [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"
    ]
    assert sick_patients(
        "CBC: RED BLOOD CELL COUNT", ">", 5, parse_labs("lab_test.txt")
    ) == ["DB22A4D9-7E4D-485C-916A-9CD1386507FB"]


def test_first_age():
    """Test the first_age function."""
    assert (
        first_age(
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            parse_patients("patient_test.txt"),
            parse_labs("lab_test.txt"),
        )
        == 3
    )
