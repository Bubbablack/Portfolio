import pytest
import sys
sys.path.append('../src')

import  calculator


def test_calculator_nun():
    calculate = calculator.add("")
    assert calculate == 0


def test_calculator_one():
    calculate = calculator.add("1")
    assert calculate == 1

def test_calculator_multiple():
    calculate = calculator.add("3,2,4")
    assert calculate == 9

def test_calculator_newline():
    calculate = calculator.add("3\n3,2")
    assert calculate  == 8

def test_calculator_deliminator():
    calculate = calculator.add("//k\n3k4k3k3")
    assert calculate == 13


def test_calculator_deliminator():
    calculate = calculator.add("//[kja][rag]\n3kja4rag3kja3")
    assert calculate  == 13