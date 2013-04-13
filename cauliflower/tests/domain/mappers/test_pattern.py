import unittest
import cauliflower.domain.pattern as pattern
import os

thedir = os.path.abspath(
    os.path.dirname(__file__) + "../../../mocks/uploads"
)


class TestPatternXMLMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = pattern.XMLMapper()

    def test_iterator_finds_items(self):
        filepath = thedir + '/dummy_import.xml'
        xs = self.mapper.iterator(filepath)
        self.assertEqual(len(xs), 3)

    def test_iterator_finds_nothing(self):
        filepath = thedir + '/empty_import.xml'
        xs = self.mapper.iterator(filepath)
        self.assertEqual(len(xs), 0)

    def test_iterator_finds_items(self):
        filepath = thedir + '/dummy_import.xml'
        xs = self.mapper.iterator(filepath)
        self.assertEqual(len(xs), 3)
