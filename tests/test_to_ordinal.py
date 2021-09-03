import pytest

from to_ordinal import to_ordinal, __version__


def test_version():
    assert __version__ == '0.1.1'


@pytest.mark.parametrize(
    ('test_input','expected'),
    [
        (0, '0th'),
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        (5, '5th'),
        (6, '6th'),
        (7, '7th'),
        (8, '8th'),
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th'),
        (13, '13th'),
        (20, '20th'),
        (21, '21st'),
        (22, '22nd'),
        (23, '23rd'),
        (100, '100th'),
        (101, '101st'),
        (102, '102nd'),
        (103, '103rd'),
        (111, '111th'),
        (112, '112th'),
        (113, '113th'),
    ]
)
def test_to_ordinal(test_input, expected):
    assert to_ordinal(test_input) == expected
