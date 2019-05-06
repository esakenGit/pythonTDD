import pytest
from assertpy import assert_that


from dollar import Dollar


#Test
def test_multiplication():
    five = Dollar(5)
    product =  five.times(2)
    assert 10 == product.amount
    product = five.times(3)
    assert 15 == product.amount



def test_equality():
    assert_that(Dollar(5).equals( Dollar(5) ) ).is_true
