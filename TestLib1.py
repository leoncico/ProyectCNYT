import Libreria1 as lc
import unittest
import math

class Test_Libreria1_cplx(unittest.TestCase):

    def test_sumacplx(self):
        self.assertEqual(lc.sumacplx((3,-1),(1 , 4)), (4,3))

    def test_productcplx(self):
        self.assertEqual(lc.productocplx((3,-1),(1 , 4)), (7,11))

    def test_restacplx(self):
        self.assertEqual(lc.restacplx((-8 , 5) , (1,5)),(-9,0))

    def test_divisioncplx(self):
       self.assertEqual(lc.divisioncplx((5.3,-2),(3.5,1)), (1.2490566037735849, -0.9283018867924528))

    def test_modulocplx(self):
       self.assertEqual(lc.modulocplx((-9,13)), 15.811388300841896)

    def test_conjugadocplx(self):
       self.assertEqual(lc.conjugadocplx((6,-13)), (6,13))

    def test_conversion(self):
        self.assertEqual(lc.conversion_polar_cartesianas((2,1), (math.sqrt(5)),(0.4636), ),('Polares: (2.23606797749979, 0.4636476090008061)', 'Cartesianas: (2.0, 1.0)'))

    def fasecplx(self):
        self.assertEqual(lc.fase(2,1),0.4636476090008061)

if __name__ == '__main__':
    unittest.main()