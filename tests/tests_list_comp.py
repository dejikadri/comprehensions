import unittest
import list_comp


class TestComp(unittest.TestCase):
    file_path = '..'

    def test_dict_when_file_exists(self):
        file_ext = 'py'
        self.assertEqual(['dict_comp.py', 'list_comp.py', 'set_comp.py'],
                         list_comp.list_file(self.file_path, file_ext))

    def test_dict_when_file_not_exists(self):
        file_ext = 'pyx'
        self.assertEqual([], list_comp.list_file(self.file_path, file_ext))


