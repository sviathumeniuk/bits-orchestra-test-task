import unittest
from Tests.test_google_registration import TestGoogleRegistration

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestGoogleRegistration))
    
    unittest.TextTestRunner(verbosity=2).run(test_suite)