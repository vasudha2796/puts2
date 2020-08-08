import unittest
import main


class TestCaseForCalculator(unittest.TestCase):
    def setUp(self):
        """Sets up the app for testing"""

        main.app.testing = True
        self.app = main.app.test_client()

    def test_empty_page(self):
        response_data = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response_data.data)

    def test_max(self):
        # when A contains integer values
        response_data = self.app.get('/max?A=5,3,1,10,15')
        self.assertEqual(b'15 \n', response_data.data)

        # when A contains float values
        response_data = self.app.get('/max?A=5.2,3.5,15.5,10.1,15.2')
        self.assertEqual(b'15.500000 \n', response_data.data)

        # when A contains integer values and float values
        response_data = self.app.get('/max?A=5,3,1,10.2,15')
        self.assertEqual(b'15 \n', response_data.data)

        # When A is non number type
        response_data = self.app.get('/max?A=5,3.2,k,l,10,15')
        self.assertEqual(b"Enter numbers in the correct format", response_data.data)


if __name__ == '__main__':
    unittest.main()
