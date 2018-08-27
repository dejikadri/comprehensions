import unittest
import set_comp


class TestComp(unittest.TestCase):
    csv_file = '../100000_Sales_Records.csv'

    def test_dict_when_country_exists(self):
        self.assertEqual(['Afghanistan', 'Albania'], set_comp.set_comp_countries(self.csv_file)[:2])


