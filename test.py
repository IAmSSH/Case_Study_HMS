from root import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure Login Page was set up correctly
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    # Ensure Register Page was set up correctly
    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    # Ensure Pharmacist Login Behaves Correctly
    def test_pharma(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(user_id="Vinayak0602", password="Vinayak0602"),
            follow_redirects=True
        )
        self.assertIn(b'Pharmacy Management', response.data)
    # Ensure Diagnostic Login Behaves Correctly
    def test_diagnos(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(user_id="Vinayak64512", password="Vinayak64512"),
            follow_redirects=True
        )
        self.assertIn(b'Ankit', response.data)
    # Ensure Authentication Behaves Correctly
    def test_auth(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(user_id="asdjkhq2hj232389", password="21321321321ascdW"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid Credentials', response.data)
    # Ensure Admin Login Behaves Correctly
    # def test_diagnos(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/login',
    #         data=dict(user_id="Vinayak64512", password="Vinayak64512"),
    #         follow_redirects=True
    #     )
    #     self.assertIn(b'Ankit', response.data)

if __name__ == '__main__':
    unittest.main()
