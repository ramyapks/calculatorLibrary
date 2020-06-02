#!/usr/bin/python3

"""
Unit test for calculator
"""

import calculator

class TestCalculator:

    def test_addition(self):
        if(4 != calculator.add_two_numbers(2,2)):
            raise Exception('Failed addition')

    def test_sub(self):
        if(2 != calculator.substract_two_numbers(4,2)):
            raise Exception('Failed substraction')

