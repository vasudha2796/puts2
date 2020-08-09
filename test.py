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

    def test_median(self):
        # when A contains integer values and even digits
        response_data = self.app.get('/median?A=5,3,10,15')
        self.assertEqual(b'7.500 \n', response_data.data)

        # when A contains float values and even digits
        response_data = self.app.get('/median?A=4.2,3.1,1.4,15.3')
        self.assertEqual(b'3.650 \n', response_data.data)

        # when A contains both integer and float values and having even digits
        response_data = self.app.get('/median?A=5,3.2,10.5,15')
        self.assertEqual(b'7.750 \n', response_data.data)

        # when A contains integer values and odd digits
        response_data = self.app.get('/median?A=5,3,1,10,15')
        self.assertEqual(b'5 \n', response_data.data)

        # when A contains float values and odd digits
        response_data = self.app.get('/median?A=4.2,3.1,1.4,11.2,15.3')
        self.assertEqual(b'4.200 \n', response_data.data)

        # when A contains both integer and float values and having odd digits
        response_data = self.app.get('/median?A=5,3.2,1.4,10,15')
        self.assertEqual(b'5 \n', response_data.data)

        # When A is non number type
        response_data = self.app.get('/median?A=5,3.2,c,n,1.4,10,15')

    def test_avg(self):
        # when A contains integer values
        response_data = self.app.get('/avg?A=5,3,1,10,15')
        self.assertEqual(b'6.800 \n', response_data.data)

        # when A contains float values and result is round off to three decimals
        response_data = self.app.get('/avg?A=4.2,3.1,1.4,11.2,15.3')
        self.assertEqual(b'7.040 \n', response_data.data)

        # when A contains both integer and float values and result is round off to three decimals
        response_data = self.app.get('/avg?A=5,3.2,1.4,10,15')
        self.assertEqual(b'6.920 \n', response_data.data)

        # When A is non number type
        response_data = self.app.get('/avg?A=5,3.2,a,aa,1.4,10,15')
        self.assertEqual(b"Enter numbers in the correct format", response_data.data)

    def test_mean(self):
        # when A contains integer values
        response_data = self.app.get('/mean?A=9,3,2,11,15')
        self.assertEqual(b'8 \n', response_data.data)

        # when A contains float values
        response_data = self.app.get('/mean?A=4.2,3.1,1.4,11.2,15.3')
        self.assertEqual(b'7.040 \n', response_data.data)

        # when A contains both integer and float values
        response_data = self.app.get('/mean?A=5,3.2,1.4,10,15')
        self.assertEqual(b'6.920 \n', response_data.data)
        # When A is non number type
        response_data = self.app.get('/mean?A=5,3.2,a,10,15')
        self.assertEqual(b"Enter numbers in the correct format", response_data.data)

    def test_average(self):
        # when A contains integer values
        response_data = self.app.get('/average?A=5,3,1,10,15')
        self.assertEqual(b'6.800 \n', response_data.data)

        # when A contains float values and result is round off to three decimals
        response_data = self.app.get('/average?A=4.2,3.1,1.4,11.2,15.3')
        self.assertEqual(b'7.040 \n', response_data.data)

        # when A contains both integer and float values and result is round off to three decimals
        response_data = self.app.get('/average?A=5,3.2,1.4,10,15')
        self.assertEqual(b'6.920 \n', response_data.data)
        # When A is non number type
        response_data = self.app.get('/average?A=5,3.2,b.4,10,15')

        self.assertEqual(b"Enter numbers in the correct format", response_data.data)


if __name__ == '__main__':
    unittest.main()
