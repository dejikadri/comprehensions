import unittest
import dict_comp


class TestComp(unittest.TestCase):
    cntry = ['Ghana']
    cap = ['Akra']

    def test_dict_when_country_exists(self):
        c_dict = dict_comp.country_cap(self.cntry, self.cap)
        self.assertEqual('Akra', c_dict.get('Ghana'))

    def test_dict_when_country_doesnt_exists(self):
        c_dict = dict_comp.country_cap(self.cntry, self.cap)
        self.assertEqual('No such Country', c_dict.get('UK', 'No such Country'))