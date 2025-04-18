import pytest
import pickle
import os
from qa_automation_cource.calculator import BasicCalc, cache

class TestCache:
    def test_cache_positive(self):
        result = BasicCalc.factorial(100)
        with open('cache.pkl', 'rb') as file:
            cache = pickle.load(file)
        assert result == cache[100], "Doesn't take the value from the cach"


    def test_cache_negative(self):
        BasicCalc.factorial(5)
        with open('cache.pkl', 'rb') as file:
            cache = pickle.load(file)
        assert 1000000 not in cache, "Unexpected value found in cache"
