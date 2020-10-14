 
import unittest
from sub import subs
# import sub

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(sub(8,7), 1)
        
        
if __name__ == '__main__':
    unittest.main()
