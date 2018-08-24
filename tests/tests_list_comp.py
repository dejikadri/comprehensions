import unittest
import list_comp


class TestComp(unittest.TestCase):
    file_path = '..'

    def test_dict_when_country_exists(self):
        self.assertEqual(['dict_comp.py', 'list_comp.py', 'set_comp.py'],
                         list_comp.list_file(self.file_path))


