import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_miroir(self):
        self.assertEqual(funcs.miroir("WeAreTheChampion", 3),"WeArrAeW")
        self.assertEqual(funcs.miroir("WeAreTheChampion", 6),"WeAreThhTerAeW")
        self.assertEqual(funcs.miroir("a", 1),"aa")

    def test_derive(self):
        self.assertEqual(funcs.derive([1.0, 2.0], 2.0), [0.5])
        self.assertEqual(funcs.derive([1.0, 2.0, 4.0], 2.0), [0.5, 1.0])
        self.assertEqual(funcs.derive([1.0, 2.0, 4.0, 10.0, 20.0 ], 4.0), [0.25, 0.5, 1.5, 2.5])
        self.assertEqual(funcs.derive([1.0], 2.0), False)
        self.assertEqual(funcs.derive([], 2.0), False)


    def test_derive2(self):
        self.assertEqual(funcs.derive2([1.0, 2.0, 4.0], 2.0) ,[0.25])
        self.assertEqual(funcs.derive2([1.0, 2.0, 4.0, 10.0, 20.0], 4.0),[0.0625, 0.25, 0.25])
        self.assertEqual(funcs.derive2([1.0, 2.0], 2.0) ,False)
        self.assertEqual(funcs.derive2([1.0], 2.0) ,False)


    def test_appro_derive(self):
        self.assertEqual(funcs.appro_derive(funcs.func_x2, 1.2, 0.1), 1.4) 
        self.assertEqual(funcs.appro_derive(funcs.func_x2, 1.2, 1), 1) 
        self.assertEqual(funcs.appro_derive(funcs.func_polynomial, 1.2, 0.01), 9.21)
        self.assertEqual(funcs.appro_derive(funcs.func_x_1, 3.1, 0.001), 0.323)
        self.assertEqual(funcs.appro_derive(funcs.func_sin, 2, 0.0001), 0.9093)

if __name__ == '__main__':
	unittest.main()