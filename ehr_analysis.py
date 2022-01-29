# Part 1
"""Fill this in later"""
from datetime import date


def parse_data(filename: str) -> dict:
    """Read data and create dictionary."""
    test = dict()
    file = open(filename)
    next(file)
    for line in file:
        items = line.split()
        key, values = items[0], items[1:]
        test.setdefault(key, []).extend(values)
    return test


patientdat = parse_data("C:/Users/jacks/BIOSTAT821/EHRProject/Patient.txt")
labdat = parse_data("C:/Users/jacks/BIOSTAT821/EHRProject/Lab.txt")


def num_older_than(age: float) -> int:
    """We assume the patient's date of birth is the third column."""
    count_older = 0
    age_in_days = age * 365.25
    today = date.today()
    for values in patientdat.values():
        year, month, day = values[1].split("-")
        patient_age = today - date(int(year), int(month), int(day))
        if patient_age.days > age_in_days:
            count_older += 1
    return count_older


print(num_older_than(51.2))

# def sick_patients(lab: str, gt_lt: str, value: str) -> list:
#      """Docstring"""

    gl = ">"
    word1 = "METABOLIC:"
    word2 = "ALBUMIN"
    count_sick = 0
    for line in labs.values():
        test = list(line)
        for i in range(len(test)):
            if test[i] == "METABOLIC:":
                if test[i + 1] == "ALBUMIN":
                    if gl == ">":
                        if float(test[i + 2]) > 4.0:
                            count_sick += 1
    print(count_sick)