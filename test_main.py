from main import linear_search
from main import binary_search
from main import compare_search
from main import *
import tabulate


def test_linear_search():
	""" done. """
	assert linear_search([1, 2, 3, 4, 5], 5) == 4
	assert linear_search([1, 2, 3, 4, 5], 1) == 0
	assert linear_search([1, 2, 3, 4, 5], 6) == -1


def test_binary_search():
	assert binary_search([1, 2, 3, 4, 5], 5) == 4
	assert binary_search([1, 2, 3, 4, 5], 1) == 0
	assert binary_search([1, 2, 3, 4, 5], 6) == -1
	assert binary_search([1, 2, 3, 4, 5, 7, 8, 11, 20, 23, 31, 42], 23) == 9
	assert binary_search([1, 2, 3, 4, 5, 7, 8, 11, 20, 23, 31, 42], 8) == 6
	assert binary_search([1, 2, 3, 4, 5, 7, 8, 11, 20, 23, 31, 42], 21) == -1
	### TODO: add two more tests here.

	###


def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
