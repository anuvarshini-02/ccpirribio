import unittest
from irribio.model import generate,recommendation
class ModelTests(unittest.TestCase):
    def test_deterministic_generation(self):
        self.assertEqual(generate(10,42),generate(10,42))
    def test_range(self):
        _,y=generate(500)
        self.assertTrue(all(0<=v<=100 for v in y))
    def test_recommendations(self):
        self.assertIn('Consider irrigation',recommendation(20))
        self.assertIn('Monitor',recommendation(45))
        self.assertIn('Avoid',recommendation(70))
if __name__=='__main__':unittest.main()
