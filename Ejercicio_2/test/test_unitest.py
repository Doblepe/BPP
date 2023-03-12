import unittest

class PruebasUnitarias(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sum(12,2), 14)
    def test_resta(self):
        self.assertEqual(resta(12,2), 10)
    def test_multiplicar(self):
        self.assertEqual(multiplicar(12, 2),24)
    def test_is_greather_than(self):
        self.assertGreater(66, 55)
    def test_is_same_num(self):
        self.assertTrue(is_same_num(55, 55))

      

def sum(x, y):
    return x+y
def resta(x,y):
    return x-y
def multiplicar(x,y):
    return (x *y)
# def is_greather_than(x,y):
#     if(x>y):
#         return True
#     else:
#         return False
def is_same_num(x,y):
    if (x == y):
        return True
    else:
        return False

unittest.main()