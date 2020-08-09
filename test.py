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

    def test_min(self):
        # when A contains integer values
        response_data = self.app.get('/min?A=5,3,1,10,15')
        self.assertEqual(b'1 \n', response_data.data)

        # when A contains float values
        response_data = self.app.get('/min?A=5.2,3.3,8.8,10.6,15.12')
        self.assertEqual(b'3.300000 \n', response_data.data)

        # when A contains integer values and float values
        response_data = self.app.get('/min?A=-5,3,1.9,10.5,15')
        self.assertEqual(b'-5 \n', response_data.data)

        # When A is non number type
        response_data = self.app.get('/min?A=5,3.2,1.4,e,r,15')
        self.assertEqual(b"Enter numbers in the correct format", response_data.data)


if __name__ == '__main__':
    unittest.main()
