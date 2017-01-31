#!python

from anagrams import generate_anagram
import unittest

class GenerateAnagramTest(unittest.TestCase):
    def test_anagram(self):
        assert generate_anagram() == 'Hello World'
