import unittest
from io import StringIO
from unittest.mock import patch
from p4a import main as p4a

class TestP4a(unittest.TestCase):    
    def test_p4a(self):
        results = []
        for i in range(1,1000):
            with patch('sys.stdout', new = StringIO()) as fake_out:
                p4a()
                results.append(fake_out.getvalue())
                # self.assertEqual(fake_out.getvalue(), 'I love dogs\n')
        
        # print(results)
        duplicates = dict((i, results.count(i)) for i in results)
        print(duplicates)

        
if __name__ == '__main__':
    unittest.main()