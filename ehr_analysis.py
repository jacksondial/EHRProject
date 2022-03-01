"""
I chose a dictionary for this assignment because the first function
'num_older_than' can be computed in O(N) time. Though in the second
function, the 'sick_patients' function, using a dynamic array I
BELIEVE I could achieve O(N) instead of O(N^2), the dictionary made
more sense to me when creating each of the functions, so I went with
that.
"""
from datetime import date, timedelta, datetime
import math as ma


class Lab:
    """Make a class that is a single visit/observation for a patient."""

    def __init__(
        self,
        subjid: str,
        admissionid: str,
        labname: str,
        labvalue: float,
        units: str,
        datetime: str,
    ):
        self.subjid = subjid
        self.admissionid = admissionid
        self.labname = labname
        self.labvalue = labvalue
        self.units = units
        self.datetime = datetime


def parse_labs(filename: str) -> list[Lab]:
    """
    Read data and create dictionary.
    This function operates in time as follows:
    O(N)
    """
    lab_list = []  # O(1)
    file = open(filename)  # O(1)
    next(file)  # O(1)
    for line in file:  # O (N)
        items = line.split("\t")  # O(1)
        lab_list.append(
            Lab(
                items[0],
                items[1],
                items[2],
                float(items[3]),
                items[4],
                items[5],
            )  # O(1)
        )

    return lab_list  # O(1)


class Patient:
    """Make a class object that is a single patient."""

    def __init__(
        self,
        subjid: str,
        gender: str,
        dob: str,
        race: str,
        marital: str,
        language: str,
        pop_below_pov: float,
    ):
        """Initialize."""
        self.subjid = subjid
        self.gender = gender
        self.dob = dob
        self.race = race
        self.marital = marital
        self.language = language
        self.pop_below_pov = pop_below_pov

    @property
    def age(self):
        """Setter for age."""
        my_date = datetime.strptime(self.dob[0:10], "%Y-%m-%d")
        patient_age = datetime.today().year - my_date.year
        return patient_age


def parse_patients(filename: str) -> list[Patient]:
    """
    Read data and create dictionary.
    This function operates in time as follows:
    1 + 1 + 1 + N(1 + 1 + 1) + 1 = 3N + 4 = N
    O(N)
    """
    patient_list = []
    file = open(filename)  # O(1)
    next(file)  # O(1)
    for line in file:  # O (N)
        items = line.split("\t")  # O(1)
        patient_list.append(
            Patient(
                items[0],
                items[1],
                items[2],
                items[3],
                items[4],
                items[5],
                float(items[6]),
            )
        )
    return patient_list


def num_older_than(age: float, patients=list[Patient]) -> int:
    """Count the number of patients older than a given age."""
    count_older = 0
    for patient in patients:
        if patient.age > age:
            count_older += 1
    return count_older


def sick_patients(
    lab_name: str, gl: str, lab_value: float, labs: list[Lab]
) -> list[str]:
    """
    Return the IDs of any patients with a lab value greater than or
    less than a given value for a given test.
    Used to be O(N**2)
    """
    patient_list = []
    for lab in labs:
        if lab.subjid not in patient_list:
            if gl == ">":
                if lab.labname == lab_name and lab.labvalue > lab_value:
                    patient_list.append(lab.subjid)
            elif gl == "<":
                if lab.labname == lab_name and lab.labvalue < lab_value:
                    patient_list.append(lab.subjid)
            else:
                raise ValueError(f"Unexpected character: {gl}")
    return patient_list


def first_age(patient_id: str, patients: list[Patient], labs: list[Lab]) -> int:
    """Compute the age of a given patient at first admission."""
    for patient in patients:
        if patient.subjid == patient_id:
            pat_dob = patient.dob
    admission_dates = []
    for lab in labs:
        if lab.subjid == patient_id and lab.admissionid == "1":
            admission_dates.append(lab.datetime.split()[0])
    ages = []
    dob_notime = datetime.strptime(pat_dob[0:10], "%Y-%m-%d")
    for each_date in admission_dates:
        ad_date = datetime.strptime(each_date[0:10], "%Y-%m-%d")
        age = ad_date - dob_notime

        ages.append(age)

    return ma.trunc(int(str(min(ages)).split()[0]) / 365.25)
