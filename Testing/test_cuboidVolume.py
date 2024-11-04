import unittest
from src.cuboidVolume import * 

class TestCuboid(unittest.TestCase):
    
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2), 8) 
        self.assertAlmostEqual(cuboid_volume(1), 1) 
        self.assertAlmostEqual(cuboid_volume(0), 0) 
        self.assertAlmostEqual(cuboid_volume(5), 125)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cuboid_volume("two")
        
        with self.assertRaises(TypeError):
            cuboid_volume([2, 3, 4])  # Test with a list
        
        with self.assertRaises(TypeError):
            cuboid_volume(None)  # Test with None

if __name__ == '__main__':
    unittest.main(verbosity=2)
