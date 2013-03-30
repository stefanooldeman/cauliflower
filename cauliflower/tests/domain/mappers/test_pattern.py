import unittest
import cauliflower.domain.mappers.pattern as pmap
import os

thedir = os.path.abspath(
    os.path.dirname(__file__) + "../../../mocks/uploads"
)


class TestPatternXMLMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = pmap.PatternXMLMapper()

    def test_iterator_finds_items(self):
        self.mapper.filepath = thedir + '/dummy_import.xml'
        xs = self.mapper.iterator()
        self.assertEqual(len(xs), 3)

    def test_iterator_finds_nothing(self):
        self.mapper.filepath = thedir + '/empty_import.xml'
        xs = self.mapper.iterator()
        self.assertEqual(len(xs), 0)
