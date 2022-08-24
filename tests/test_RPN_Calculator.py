
from ..RPN_Calculator import convert_rpn_string, process_math_operation, Execute_RPN_Calculation

import pytest

# Convert RPN String Tests
def test_crs_passed_list():
    with pytest.raises(TypeError):
        convert_rpn_string([1,3,'+',2,'/'])


def test_crs_passed_valid_string():
    assert convert_rpn_string('1 3 + 2 /') == [1.0,3.0,'+',2.0,'/']


def test_crs_passed_decimal_number():
    assert convert_rpn_string('2 3.4 + 2 /') == [2.0,3.4,'+',2.0,'/']


# Process Math Operation Tests
def test_pmo_passed_invalid_symbol():
    with pytest.raises(ValueError):
        process_math_operation('^',5,2)


def test_pma_passed_string_as_a_or_b():
    with pytest.raises(TypeError):
        process_math_operation('*','a',5)
        process_math_operation('*',3,'b') 


# Execute RPN Calculation Tests
def test_erc_passed_incorrect_number_of_symbols():
    with pytest.raises(ArithmeticError):
        Execute_RPN_Calculation('9 4 3 6 + *')


def test_erc_symbols_in_wrong_places():
    with pytest.raises(ArithmeticError):
        Execute_RPN_Calculation('+ 9 4 3 -')