import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass
    
    def notest(self):
        pass
#jesli poczatek def nie ma nazwy test, jest pomijany, testy sa wykonywane alfabetycznie najpierw po klasach potem po metodach
class MyTestCase2(unittest.TestCase):
    def test_two(self):
        pass
    def test_three(self):
        pass
if __name__ == "__main__":
    unittest.main()