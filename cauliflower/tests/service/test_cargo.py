import unittest
import os

from cauliflower.service.cargo import CargoService
import cauliflower.errors as errors

import cauliflower.domain.abstract as abstract
from cauliflower.domain.pattern import XMLMapper

p = os.path
thedir = p.abspath(p.dirname(__file__) + "/../mocks/uploads/")


class MockedDataMapper(abstract.DataMapper):
    def __init__(self):
        self.filepath = ""


class MockedMapper(abstract.Mapper):
    "note: No external layer to map here"

    def save(self, x):
        pass

    def create(self, x):
        pass


class TestCargoXML(unittest.TestCase):

    def setUp(self):
        self.cargo = CargoService(thedir)

        mapper = MockedMapper()
        mapper.dataMapper = XMLMapper()
        self.cargo.pattern_mapper = mapper

    def test_import(self):
        self.cargo.do_import('dummy_import.xml')
        self.assertEqual(self.cargo.size, 3)

    def test_patterns_loaded_by_import(self):
        self.cargo.do_import('dummy_import.xml')
        pattern = self.cargo.patterns[0]
        self.assertEqual(pattern.name, "BuilderPattern")
        self.assertEqual(pattern.problem, "problem1 dork")
        self.assertEqual(pattern.solution, "solution1 dork")
        self.assertEqual(pattern.context, "creational")
        self.assertEqual(pattern.consequences, "consequences1 dork")
        self.assertEqual(pattern.image, "foobar.png")


class TestFileChecks(unittest.TestCase):

    def setUp(self):
        self.cargo = CargoService(thedir)
        self.cargo.pattern_mapper = MockedDataMapper()

    def test_do_import_valid_filetypes_returns_true(self):
        self.assertTrue(self.cargo.do_import('dummy_import.xml'))
        self.assertTrue(self.cargo.do_import('dummy_import.json'))

    def test_do_import_unsupported_filetypes_raises(self):
        with self.assertRaises(errors.ValidationError):
            self.cargo.do_import('dummy_import.doc')

    def test_do_import_screams_filenotfound(self):
        with self.assertRaises(IOError):
            self.assertTrue(self.cargo._checkfile('rickrolled.xml'))
