import sys, os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

from inst_driver_ex import INST
import pytest

inst = INST('GPIB0::1::INSTR')


def test_address_correct():
    assert inst.visa_resource == "GPIB0::1::INSTR"


def test_freq_setter_command():
    inst.Freq = 5e9
    assert inst._command == "SOUR:FREQ 5000000000.0"

def test_freq_getter_command():
    inst.Freq
    assert inst._command == "SOUR:FREQ?"