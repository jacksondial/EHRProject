"""
I chose a dictionary for this assignment because the first function
'num_older_than' can be computed in O(N) time. Though in the second
function, the 'sick_patients' function, using a dynamic array I
BELIEVE I could achieve O(N) instead of O(N^2), the dictionary made
more sense to me when creating each of the functions, so I went with
that.
"""
from datetime import date


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
    1 + 1 + 1 + N(1 + 1 + 1) + 1 = 3N + 4 = N
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
            )
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
        # labvisits: list[Lab],
    ):
        """Initialize."""
        self.subjid = subjid
        self.gender = gender
        self.dob = dob
        self.race = race
        self.marital = marital
        self.language = language
        self.pop_below_pov = pop_below_pov
        # self.labvisits = labvisits

    @property
    def age(self):
        """Compute age."""
        dob_year, dob_month, dob_day = self.dob.split("-")
        patient_age = date.today() - date(int(dob_year), int(dob_month), int(dob_day))
        return int(patient_age / 365.25)
        # Do I need to return this value as self.age or something like that?


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
        if Patient.age > age:
            count_older += 1
    return count_older


# def num_older_than(age: float, patient_dict: dict[str, list[str]]) -> int:
#     """
#     Parse data and count the number of patients older than given age.
#     We assume the patient's date of birth is the third column.
#     This function operates in time as follows:
#     1 + 1 + 1 + N(3 + 3 + 1 + 1) + 1 = 8N + 4 = N
#     O(N)
#     """
#     count_older = 0  # O(1)
#     age_in_days = age * 365.25  # O(1)
#     today_date = date.today()  # O(1)
#     for values in patient_dict.values():  # O(N)
#         year, month, day = values[1].split("-")  # O(3)
#         patient_age = today_date - date(int(year), int(month), int(day))  # O(3)
#         if patient_age.days > age_in_days:  # O(1)
#             count_older += 1  # O(1)
#     return count_older  # O(1)


def sick_patients(
    lab_name: str, gl: str, lab_value: float, labs: list[Lab]
) -> list[str]:
    """
    Return the IDs of any patients with a lab value greater than or
    less than a given value for a given test.
    """
    patient_list = []
    for lab in labs:
        if Lab.subjid not in patient_list:
            if gl == ">":
                if Lab.labname == lab_name and Lab.labvalue > lab_value:
                    patient_list.append(Lab.subjid)
            elif gl == "<":
                if Lab.labname == lab_name and Lab.labvalue < lab_value:
                    patient_list.append(Lab.subjid)
            else:
                raise ValueError(f"Unexpected character: {gl}")
    return patient_list


# def sick_patients(
#     lab: str, gl: str, value: float, lab_dict: dict[str, list[str]]
# ) -> list[str]:
#     """
#     Parse data and return the patient ID's of any with a test value above
#     or below a given value for a given test measurement.
#     O(N^2)
#     """
#     patient_list = dict()  # O(1)
#     lab_name = lab.split()  # O(1)
#     num_words = len(lab_name)  # O(1)
#     for key, values in lab_dict.items():  # O(N)
#         test = list(values)  # O(1)
#         for i in range(len(test)):  # O(N)
#             if test[i : (i + num_words)] == lab_name:  # O(1)
#                 if gl == ">":  # O(1)
#                     if float(test[i + num_words]) > value:  # O(1)
#                         patient_list[key] = key  # O(1)
#                 elif gl == "<":  # O(1)
#                     if float(test[i + num_words]) < value:  # O(1)
#                         patient_list[key] = key  # O(1)
#                 else:
#                     raise ValueError(f"Unexpected character: {gl}")
#     return list(patient_list.keys())  # O(1)


def first_age(patient_id: str, patients: list[Patient], labs: list[Lab]) -> int:
    """Compute the age of a given patient at first admission."""
    for patient in patients:
        if Patient.subjid == patient_id:
            pass  # add in something like where lab.subjid is patinet_id,
        # compute the age for each of those values and then find the minimum of
        # each of those and return


# def first_age(
#     patient_id: str, patient_dict: dict[str, list[str]], lab_dict: dict[str, list[str]]
# ) -> int:
#     """
#     Compute the age of given patient at first admission.
#     It is assumed that the first recorded lab record for a patient is their
#     first in the file. We also assume the date is in the format of
#     YYYY-MM-DD. The date item for the patient file is assumed
#     to be the second in the list that is the items in a dictionary,
#     and the date item for the labs file is assumed to be the second
#     from the last item
#     """
#     patient_dob = patient_dict.get(patient_id)[1]
#     visit_day = lab_dict.get(patient_id)[-2]
#     dob_year, dob_month, dob_day = patient_dob.split("-")
#     ad_year, ad_month, ad_day = visit_day.split("-")
#     age_at_admission = date(int(ad_year), int(ad_month), int(ad_day)) - date(
#         int(dob_year), int(dob_month), int(dob_day)
#     )
#     return int(age_at_admission.days / 365.25)
