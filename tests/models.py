from django.test import TestCase


class SampleTest(TestCase):
    """ Sample test case """

    def test_first(self):
        self.assertEqual(1, 2)