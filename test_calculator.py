#!/usr/bin/python3

"""
Unit test for calculator
"""

import calculator

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add_two_numbers(2,2)

    def test_sub(self):
        assert 2 == calculator.substract_two_numbers(4,2)

