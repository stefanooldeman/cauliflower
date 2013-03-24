import unittest
import os

from cauliflower.service.cargo import CargoService


class TestCargo(unittest.TestCase):

    def setUp(self):
        thedir = os.path.abspath(os.curdir + "../mocks/uploads/")
        print thedir
        self.my_upload_dir = thedir

    def test_import(self):
        cargo = CargoService(self.my_upload_dir)
        cargo.filename = 'dummy_file.xml'
        cargo.do_import()
        self.assertEqual(cargo.size, 3)