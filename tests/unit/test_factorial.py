import pytest
from ...factorial import Factorial

factorial_object = Factorial()

def test_positive_sample_1():
    
    number = 5
    expected_output = 120

    factorial_output = factorial_object.compute(number)

    assert factorial_output == expected_output

def test_zero():
    
    number = 0
    expected_output = 1

    factorial_output = factorial_object.compute(number)

    assert factorial_output == expected_output

def test_positive_sample_2():
    
    number = 7
    expected_output = 5040

    factorial_output = factorial_object.compute(number)

    assert factorial_output == expected_output

def test_non_integer_input():

    input = 'random_string'
    expected_output = -1 #This error has been explicitly handled in my funuction defination and -1 is returned as output in such cases

    factorial_output = factorial_object.compute(input)

    assert factorial_output == expected_output

def test_negative_input():

    number = -5
    expected_output = -2 #This error has been explicitly handled in my funuction defination and -2 is returned as output in such cases

    factorial_output = factorial_object.compute(number)

    assert factorial_output == expected_output

