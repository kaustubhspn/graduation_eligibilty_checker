import pytest
from app_exceptions import *

from graduation_checker import GraduationCeremonyChecker

def test_invalid_acedemic_days():
    # Test if InvalidAcedemicDaysException is raised when no_of_acedemic_days is negative
    try:
        graduation_ceremony_checker = GraduationCeremonyChecker(-1, 0)
    except InvalidAcedemicDaysException:
        pass
    else:
        assert False, "InvalidAcedemicDaysException not raised for -(ve) no_of_acedemic_days"

    # Test if InvalidAcedemicDaysException is raised when no_of_acedemic_days is less than missing_days_threshold
    try:
        graduation_ceremony_checker = GraduationCeremonyChecker(5, 10)
    except InvalidAcedemicDaysException:
        pass
    else:
        assert False, "InvalidAcedemicDaysException not raised for no_of_acedemic_days less than missing_days_threshold"

def test_invalid_missing_days_count():
    # Test if InvalidMissingDaysCountException is raised when missing_days_threshold is negative
    try:
        graduation_ceremony_checker = GraduationCeremonyChecker(10, -1)
    except InvalidMissingDaysCountException:
        pass
    else:
        assert False, "InvalidMissingDaysCountException not raised for -(ve) missing_days_threshold"

@pytest.fixture(params=[
    (10, 4, "372/773"),   
    (5, 4, "14/29")
])
def checker(request):
    no_of_acedemic_days, missing_days_threshold, expected_output = request.param
    return GraduationCeremonyChecker(no_of_acedemic_days, missing_days_threshold), expected_output

def test_solve(checker):
    gc_checker, expected_output = checker
    assert gc_checker.solve() == expected_output