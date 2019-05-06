import pytest
from assertpy import assert_that


from dollar import Dollar


#Test
def test_multiplication():
    five = Dollar(5)
    product =  five.times(2)
    assert Dollar(10).amount == product.amount
    product = five.times(3)
    assert Dollar(15).amount == product.amount



def test_equality():
    assert_that(Dollar(5).equals( Dollar(5) ) ).is_true()
    assert_that(Dollar(6).equals( Dollar(5) ) ).is_false()
